import eyed3
import os
import sys
from tkinter import filedialog,messagebox,simpledialog,StringVar,IntVar,OptionMenu,Button,Frame,BOTH,Label,Tk,Toplevel
from datetime import datetime
from pydub import AudioSegment

d = {}
counter = 1
genre_pick = ""
artwork_set = False
title_set = False
genre_set = False
all_metadata_set = False
cancelled = False
success_str = ""
root = Tk()
root.withdraw() # CLOSE BACKGROUND TKINTER WINDOW

### FUNCTION GET WORKING DIR WITH TKINTER ###

def workingdir_func():
    global root
    dirname = filedialog.askdirectory(parent=root,initialdir="/",title="Please select a directory")
    return dirname

def metadata_min_func(dirname,list_dir):
    global counter,d
    for file in list_dir:
        if os.path.isfile(dirname+"/"+file):
            if file.split(".")[1] == "wav":
                d[counter] = {}
                d[counter]['Path'] = dirname+"/"+file
                d[counter]['Artist'] = file.split(" - ")[0]
                d[counter]['Trackname'] = file.split(" - ")[1].split(".")[0]
                counter += 1
    return True

def genre_func():
    global genre_pick
    genre_pick = genre_var.get()
    ok_var.set(1)
    top.quit()

def update_id3_func_meta(file_name,artist,item_title,albumname,art_filename,mime_image,genre):    
    #edit the ID3 tag to add the title, artist, album, artwork, date, and genre
    audiofile = eyed3.load(file_name)
    audiofile.tag.artist = artist
    audiofile.tag.album = albumname
    audiofile.tag.title = item_title
    audiofile.tag.genre = genre
    audiofile.tag.release_date = datetime.now().year
    audiofile.tag.images.set(3,open(art_filename,'rb').read(),mime_image)
    audiofile.tag.save()

def update_id3_func(file_name,artist,item_title):    
    #edit the ID3 tag to add the title, artist, album, artwork, date, and genre
    audiofile = eyed3.load(file_name)
    audiofile.tag.artist = artist
    audiofile.tag.title = item_title
    audiofile.tag.release_date = datetime.now().year
    audiofile.tag.save()

def convert_func(dir_folder,file,input_format,output_format):
    global success_str
    song = AudioSegment.from_file(dir_folder+"/"+file+"."+input_format,input_format)
    export_song = song.export(dir_folder+"/"+file+"."+output_format, format=output_format, bitrate="320k")
    if export_song:
        success_str += file+"."+input_format+"\n"
        return True
    else:
        print("Something went wrong, with: "+file+" in directory: "+dir_folder)
        return False

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.pack(fill=BOTH, expand=1)
        
        text = Label(self, text="In Progress...")
        text.place(x=30,y=30)

messagebox.showinfo(title="Welcome!",message="Welcome to wavtomp3 converter!\n\nPlease choose the folder your wav files are placed for conversion!")

dirname = workingdir_func()
if not dirname:
    messagebox.showinfo(title="Failure getting directory",message="No directory was choosen!")
    cancelled = True
else:
    if len(dirname) > 0: # CHECK FOR DIRECTORY LENGTH 0/EMPTY NOT ALLOWED
        
        list_dir = os.listdir(dirname) # PUT ALL ENTRIES OF DIR INTO A LIST
        if ".wav" in str(list_dir):
            
            while True:

                if metadata_min_func(dirname,list_dir):

                    genre_list_file = resource_path("genre-list.txt")

                    MsgBox = messagebox.askyesnocancel('Metadata','Do you want to add Metadata: Artwork, Release Title and Genre?\n\n If you choose No, conversion will start with just Artist & Trackname')
                    
                    if MsgBox:

                        for x in d:
                            artist = d[x]['Artist']
                            trackname = d[x]['Trackname']
                            fulltrackname = artist+" - "+trackname
                            
                            if artwork_set and title_set and genre_set:
                                MsgBox = messagebox.askquestion('Metadata','Do you want to reuse the information provided for Track: '+fulltrackname+'?')
                                if MsgBox == 'yes':
                                    d[x]['Title'] = titlename
                                    d[x]['Artpath'] = art_filename
                                    d[x]['Mime-Type'] = mime_image
                                    d[x]['Genre'] = genre_pick
                                    d[x]['All-Metadata'] = True
                                else:            
                                    #ask for album name
                                    titlename = simpledialog.askstring(fulltrackname, "Enter Release Title please: ",parent=root)
                                    titlename_check = isinstance(titlename,str)
                                    if not titlename_check:
                                        messagebox.showinfo(title="Failure!",message="Cancelled on the release title! Program closed.")
                                        break
                                    else:
                                        d[x]['Title'] = titlename
                                        title_set = True

                                        messagebox.showinfo(title="Choose Artwork",message="Please choose artwork!")
                                        
                                        art_filename = filedialog.askopenfile(parent=root,initialdir=dirname,mode='r',title='Please choose artwork')
                                        if not art_filename:
                                            messagebox.showinfo(title="Failure!",message="Cancelled on the Artwork! Program closed.")
                                            break
                                        else:
                                            art_filename = art_filename.name
                                            
                                            #check mime-type of selected artwork
                                            art_filename_split = art_filename.split(".")[1]
                                            if art_filename_split == "png":
                                                mime_image = "image/png" # 'application/pdf'
                                                
                                                d[x]['Artpath'] = art_filename
                                                d[x]['Mime-Type'] = mime_image
                                                artwork_set = True
                                                
                                            elif art_filename_split == "jpg" or art_filename == "jpeg":
                                                mime_image = "image/jpeg" # 'application/pdf'
                                                
                                                d[x]['Artpath'] = art_filename
                                                d[x]['Mime-Type'] = mime_image
                                                artwork_set = True
                                                
                                            else:
                                                messagebox.showinfo(title="Failure!",message="Artwork is not a jpg or png! Program closed.")
                                                break
                                            
                                            if artwork_set and title_set:
                                                top = Toplevel(root)
                                                top.title("Pick A Genre:")
                                                genre_var = StringVar(top)
                                                ok_var = IntVar()

                                                with open(genre_list_file) as file_in:
                                                    genres = []
                                                    for line in file_in:
                                                        line = line.strip()
                                                        genres.append(line)
                                                        
                                                GenreMenu = OptionMenu(top, genre_var, *genres)
                                                GenreMenu.pack()
                            
                                                genre_var.set("Drum & Bass") # default value
                                                        
                                                OkButton = Button(top, text="OK", command=genre_func)
                                                OkButton.pack()
                                                
                                                top.wait_variable(ok_var)
                                                d[x]['Genre'] = genre_pick
                                                genre_set = True

                                                if genre_set:
                                                    d[x]['All-Metadata'] = True
                                                    top.destroy()
                            else:        
                                #ask for album name
                                titlename = simpledialog.askstring(fulltrackname, "Enter Release Title please: ",parent=root)
                                titlename_check = isinstance(titlename,str)
                                if not titlename_check:
                                    messagebox.showinfo(title="Failure!",message="Cancelled on the release title! Program closed.")
                                    break
                                else:
                                    d[x]['Title'] = titlename
                                    title_set = True

                                    messagebox.showinfo(title="Choose Artwork",message="Please choose artwork!")
                                    
                                    art_filename = filedialog.askopenfile(parent=root,initialdir=dirname,mode='r',title='Please choose artwork')
                                    if not art_filename:
                                        messagebox.showinfo(title="Failure!",message="Cancelled on the Artwork! Program closed.")
                                        break
                                    else:
                                        art_filename = art_filename.name
                                        
                                        #check mime-type of selected artwork
                                        art_filename_split = art_filename.split(".")[1]
                                        if art_filename_split == "png":
                                            mime_image = "image/png" # 'application/pdf'
                                            
                                            d[x]['Artpath'] = art_filename
                                            d[x]['Mime-Type'] = mime_image
                                            artwork_set = True
                                            
                                        elif art_filename_split == "jpg" or art_filename == "jpeg":
                                            mime_image = "image/jpeg" # 'application/pdf'
                                            
                                            d[x]['Artpath'] = art_filename
                                            d[x]['Mime-Type'] = mime_image
                                            artwork_set = True
                                            
                                        else:
                                            messagebox.showinfo(title="Failure!",message="Artwork is not a jpg or png! Program closed.")
                                            break
                                        
                                        if artwork_set and title_set:
                                            top = Toplevel(root)
                                            top.title("Pick A Genre:")
                                            genre_var = StringVar(top)
                                            ok_var = IntVar()

                                            with open(genre_list_file) as file_in:
                                                genres = []
                                                for line in file_in:
                                                    line = line.strip()
                                                    genres.append(line)
                                                    
                                            GenreMenu = OptionMenu(top, genre_var, *genres)
                                            GenreMenu.pack()
                        
                                            genre_var.set("Drum & Bass") # default value
                                                    
                                            OkButton = Button(top, text="OK", command=genre_func)
                                            OkButton.pack()
                                            
                                            top.wait_variable(ok_var)

                                            d[x]['Genre'] = genre_pick
                                            genre_set = True

                                            if genre_set:
                                                d[x]['All-Metadata'] = True
                                                top.destroy()
                        break
                    elif MsgBox is not None:                
                        for x in d:
                            d[x]['Title'] = None
                            d[x]['Artpath'] = None
                            d[x]['Mime-Type'] = None
                            d[x]['Genre'] = None
                            d[x]['All-Metadata'] = False
                        break
                    else:
                        cancelled = True
                        messagebox.showinfo(title="Cancelled",message="You pressed cancel. Program closed.")
                        break
                else:
                    cancelled = True
                    messagebox.showinfo(title="Failure!",message="Issue in collecting metadata. Program closed!")
        else:
            cancelled = True
            messagebox.showinfo(title="Failure!",message="No wav files in folder! Program closed!")
    else:
        cancelled = True
        messagebox.showinfo(title="Failure!",message="Problem fetching correct directory! Program closed!")

if not cancelled:
    parent = Toplevel(root)
    app = Window(parent)
    parent.wm_title("Conversion")
    parent.geometry("200x100")
    parent.update()

    for x in d:
        mp3_file_path = str(d[x]['Path'].split(".")[0])+".mp3"
        fulltrackname = str(d[x]['Artist'])+" - "+str(d[x]['Trackname'])

        if d[x]['All-Metadata']:
            metadata = "with"
            if convert_func(dirname,fulltrackname,"wav","mp3"):
                try:
                    update_id3_func_meta(mp3_file_path,d[x]['Artist'],d[x]['Trackname'],d[x]['Title'],d[x]['Artpath'],d[x]['Mime-Type'],d[x]['Genre'])
                except Exception as exp:
                    messagebox.showinfo(title="Failure during id3 update: ",message=exp)
                else:
                    pass
            else:
                messagebox.showinfo(title="Failure!",message="Issue in convert function!")
        else:
            metadata = "without"
            if convert_func(dirname,fulltrackname,"wav","mp3"):
                try:
                    update_id3_func(mp3_file_path,d[x]['Artist'],d[x]['Trackname'])
                except Exception as exp:
                    messagebox.showinfo(title="Failure during id3 update: ",message=exp)
                else:
                    pass
            else:
                messagebox.showinfo(title="Failure!",message="Issue in convert function!")

    parent.destroy()                 

    ### MESSAGEBOX END OF PROGRAM OUTPUT ###
    messagebox.showinfo(title="Convert to mp3",message="Successfully converted:\n"+success_str+" to mp3 "+metadata+" metadata")

root.destroy()
root.mainloop()