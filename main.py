import os
import cv2
import time
from tkinter.ttk import *
from tkinter import*
from tkinter import font
from tkinter import messagebox
from tkinter.scrolledtext import ScrolledText
import tkinter as tk
from tkinter.filedialog import askopenfilename
from tkinter.messagebox import showinfo
from os.path import exists
from exif import Image


root = Tk()

IMG_FILE = ""
img_data = []

class Convert:
    def __init__(self, master):
        self.master = master
        master.title("Single Button Event")
        master.geometry("1000x500")
        master.configure(bg="white")

                
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
        self.frame_left.columnconfigure(0, weight=1)

        #labelled frames - frame_left
        self.frame_left_one     =  LabelFrame(self.frame_left,text="Select Image",labelanchor="n",bg="white",bd=10,fg="red",font=self.label_frame_font)

        #frame grids
        self.frame_left_one.grid(row=0,column=0,sticky="nsew")

        #frame for componants for left fisrt labeled frame  
        self.frame_left_one.grid_rowconfigure(0, weight=1)
        self.frame_left_one.grid_rowconfigure(1, weight=1)
        self.frame_left_one.grid_rowconfigure(2, weight=1)
        self.frame_left_one.columnconfigure(0, weight=1)
        
        
        #componants for frame 1
        self.frame_left_btn1 = Button(self.frame_left_one,text="Choose Image",height = 3, width = 20,command=lambda:choose_image())
        self.frame_left_btn2 = Button(self.frame_left_one,text="Choose Video",height = 3, width =20,command=lambda:choose_video())
        self.frame_left_btn3 = Button(self.frame_left_one,text="Show Meatadata",height = 3, width =20,command=lambda:get_metadata())

        #componants grid for frame 1
        self.frame_left_btn1.grid(row=0,column=0,sticky="nsew")
        self.frame_left_btn2.grid(row=1,column=0,sticky="nsew")
        self.frame_left_btn3.grid(row=2,column=0,sticky="nsew")


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
            global img_data
            filename = select_file()
            temp_data = []
            self.scroll_text.insert(tk.INSERT,"Selected file is : " + filename +  "\n")
            if filename:
                IMG_FILE = filename
                try:
                    with open(IMG_FILE, 'rb') as img_file:
                        img = Image(img_file)
                        temp_data = [(tag,img.get(tag)) for tag in sorted(img.list_all())]
                except:
                    self.scroll_text.insert(tk.INSERT,"\nThis image has some problems!" + "\n")
                    
            if exists(IMG_FILE):
                for key,value in temp_data:
                    img_data.append(key + " : "  + str(value))
                                        

        def choose_video():
            filename = select_file()
            self.scroll_text.insert(tk.INSERT,"Selected file is : " + filename +  "\n")

                    
        def get_metadata():
            global img_data
            global IMG_FILE
            if len(img_data) < 1:
                self.scroll_text.insert(tk.INSERT,"\nNo metadata found!")
            else:
                 for lines in img_data:
                     self.scroll_text.insert(tk.INSERT,lines + "\n")
            img_data = []
            IMG_FILE = []
            

            

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


        def print_metadata(file_name):
            metadata_ = []
            cmd="exiftool "+ file_name
            metadata=os.popen(cmd).read()
            metadata=metadata.split('\n')
            
            for each in metadata:
                try:
                    data = each.split(':')
                    metadata_.append(data[0].rstrip() +" : "+ data[1])
                except:
                    pass


        


hack_gui = Convert(root)
root.mainloop()
