import os


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

   print(metadata_)
   


   
print_metadata("video.mp4")
