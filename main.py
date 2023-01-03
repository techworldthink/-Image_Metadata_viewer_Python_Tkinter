from tkinter.ttk import *
from tkinter import*
from tkinter import font
from tkinter import messagebox
from PIL import Image, ImageDraw, ImageFont,ImageTk
import PIL
from tkinter.scrolledtext import ScrolledText
import tkinter as tk
from tkinter.filedialog import askopenfilename
from tkinter.messagebox import showinfo
from PIL import Image
from PIL.ExifTags import TAGS
import os
from os.path import exists


root = Tk()

IMG_FILE = os.getcwd() + "/images/demo_img.jpg"

class Convert:
    def __init__(self, master):
        self.master = master
        master.title("Single Button Event")
        master.geometry("1000x500")
        master.configure(bg="white")

        # Demo model certificate
        model = PIL.Image.open(IMG_FILE)
        newsize = (300, 150)
        model = model.resize(newsize)
        IMG_ = ImageTk.PhotoImage(model)


                
        #full window row configure
        master.grid_rowconfigure(0, weight=1)
   
        #full window column configure
        master.columnconfigure(0, weight=1)
        master.columnconfigure(1, weight=1)

        
        #Fonts
        self.label_frame_font = font.Font(family="Helvetica",size=10,weight="bold")
        self.frame2_font = font.Font(family="Franklin Gothic Medium",size=10)

        # MENU SECTION STARTED #####################################################
        self.menu_section = Menu(master)                                                              
        self.menu_section_file = Menu(self.menu_section,tearoff = 0)                         
        self.menu_section_file.add_command(label="About")
        self.menu_section_file.add_command(label="close")
        self.menu_section_file.add_separator()                                                           
        self.menu_section_file.add_command(label="Exit")
        master.config(menu = self.menu_section)                                                      
        self.menu_section.add_cascade(label="File", menu = self. menu_section_file)   

        #END MENU #####################################################################

        #labelled frames - master
        self.frame_left     =  LabelFrame(master,text="",labelanchor="n",bg="white",bd=10,fg="red",font=self.label_frame_font)
        self.frame_right    =  LabelFrame(master,text="Metadata",labelanchor="n",bg="white",bd=10,fg="red",font=self.label_frame_font)

        #frame grids
        self.frame_left.grid(row=0,column=0,sticky="nsew")
        self.frame_right.grid(row=0,column=1,sticky="nsew")
        
        #frame for componants for fisrt labeled frame  row configure  1
        self.frame_left.grid_rowconfigure(0, weight=1)
        self.frame_left.grid_rowconfigure(1, weight=1)
        self.frame_left.columnconfigure(0, weight=1)

        #labelled frames - frame_left
        self.frame_left_one     =  LabelFrame(self.frame_left,text="Select Image",labelanchor="n",bg="white",bd=10,fg="red",font=self.label_frame_font)
        self.frame_right_two    =  LabelFrame(self.frame_left,text="Add metadata",labelanchor="n",bg="white",bd=10,fg="red",font=self.label_frame_font)

        #frame grids
        self.frame_left_one.grid(row=0,column=0,sticky="nsew")
        self.frame_right_two.grid(row=1,column=0,sticky="nsew")

        #frame for componants for left fisrt labeled frame  
        self.frame_left_one.grid_rowconfigure(0, weight=1)
        self.frame_left_one.grid_rowconfigure(1, weight=1)
        self.frame_left_one.grid_rowconfigure(2, weight=1)
        self.frame_left_one.columnconfigure(0, weight=1)
        
        
        #componants for frame 1
        self.frame_left_img  = Label(self.frame_left_one,image=IMG_,text="image",padx=0,pady=0,bg="white",fg="black",height = 100,width=30)
        self.frame_left_img.image = IMG_
        self.frame_left_btn1 = Button(self.frame_left_one,text="Choose Image",height = 3, width = 20,command=lambda:choose_image())
        self.frame_left_btn2 = Button(self.frame_left_one,text="Get Meatadata",height = 3, width =20,command=lambda:get_metadata())
        #componants grid for frame 1
        self.frame_left_img.grid(row=0,column=0,sticky="nsew")
        self.frame_left_btn1.grid(row=1,column=0)
        self.frame_left_btn2.grid(row=2,column=0)


        #frame for componants for fisrt labeled frame  row configure  2
        self.frame_right.grid_rowconfigure(0, weight=1)   
        self.frame_right.columnconfigure(0, weight=1)
        #componants for frame 2
        self.scroll_text = ScrolledText(self.frame_right,bg="white",fg="green")
        #componants grid for frame 2
        self.scroll_text.grid(row=0,column=0)
                      
        self.scroll_text.insert(tk.INSERT,"-------------LOGS----------\nStarting...\n")

        


        def choose_image():
            global IMG_FILE
            filename = select_file()
            if filename:
                IMG_FILE = filename
                model = PIL.Image.open(filename)
                self.IMG_ = model
                self.IM_width, self.IM_height = model.size
                newsize = (300, 150)
                model_show = model.resize(newsize)
                IMG_T = ImageTk.PhotoImage(model_show)
                self.frame_left_img.configure(image=IMG_T)
                self.frame_left_img.image = IMG_T
                self.scroll_text.delete('1.0', END)
                self.scroll_text.insert(tk.INSERT,"\nImage selected...\n")
                self.scroll_text.insert(tk.INSERT,IMG_FILE + "\n")

        def get_metadata():
            global IMG_FILE
            print(IMG_FILE)
            self.scroll_text.delete('1.0', END)
            if exists(IMG_FILE):
                img = PIL.Image.open(IMG_FILE)
                img_exif = img.getexif()
                if img_exif:
                    exif = {
                        PIL.ExifTags.TAGS[k]: v
                        for k, v in img._getexif().items()
                        if k in PIL.ExifTags.TAGS
                    }

                    for key in exif:
                        print(key)
                        print(exif[key])
                        self.scroll_text.insert(tk.INSERT,str(key) + " : " + str(exif[key]) +"\n")
                else:
                    self.scroll_text.insert(tk.INSERT,IMG_FILE + "\n")
                    self.scroll_text.insert(tk.INSERT,"\nNo metadata found!")
            

        def select_file():
            filetypes = (
                ('All files', '*.*'),
                ('text files', '*.txt')
            )

            filename = askopenfilename(
                title='Open a file',
                initialdir='/',
                filetypes=filetypes)

            showinfo(
                title='Selected File',
                message=filename
            )

            return filename




hack_gui = Convert(root)
root.mainloop()
