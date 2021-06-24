# wavtomp3

## Converts a choosen folder with wav files into an mp3
### Optionally will also save additional metadata to the mp3 like Artwork, Release Title and Genre

### Packages used
- id3 tags: https://github.com/nicfit/eyeD3
- conversion: https://github.com/jiaaro/pydub

### Prereqs
the pydub package uses <b>ffmpeg</b> for the conversion, so you'll <b>need to install</b> it:

- [mac](https://github.com/fluent-ffmpeg/node-fluent-ffmpeg/wiki/Installing-ffmpeg-on-Mac-OS-X)
- [windows](https://windowsloop.com/install-ffmpeg-windows-10/)
- [linux](https://linuxize.com/post/how-to-install-ffmpeg-on-debian-9/)

### Default settings
- files are expected in format "artist - tracktitle.wav"
- the file name will be used as minimal configuration metadata for the id3 tags
- bitrate is hard coded to 320k
- files will be exported to the same directory as the wav file location
- Default genre when choosing Metadata is Drum & Bass (because I like it ;-))

### Download, Execute App (MacOS)
 
[Download & Unarchive](#download_unarchive)  
[Allow App to Execute](#allow_app)  
[Execute App](#execute_app)  

<a name="download_unarchive"/></a>
#### Download & Unarchive

<img src="https://github.com/carlos-lehmann/wavtomp3/blob/main/readme-content/Download-Unarchive.gif?raw=true" alt="Download & Unarchive" />

<a name="allow_app"/></a>
#### Allow App to Execute

    sudo spctl --master-disable

<img src="https://github.com/carlos-lehmann/wavtomp3/blob/main/readme-content/Allow-Executable.gif?raw=true" alt="Allow App to Execute" />

<a name="execute_app"/></a>
#### Execute App

<img src="https://github.com/carlos-lehmann/wavtomp3/blob/main/readme-content/Execute-App.gif?raw=true" alt="Execute App" />

### App Flow

[Choose Folder](#choose_folder)  
[Add Metadata (Yes/No)](#add_metadata) 

<b>Yes</b>
 
    [Choose Release Title](#choose_title)
    [Choose Artwork](#choose_artwork) 
    [Pick Genre](#pick_genre) 
    
<b>No</b>

<a name="choose_folder"/></a>
#### Choose Folder

<img src="https://github.com/carlos-lehmann/wavtomp3/blob/main/readme-content/Choose-Wav-Folder.gif?raw=true" alt="Choose Folder" />

<a name="add_metadata"/></a>
#### Add Metadata (Yes/No)

Choosing No will start conversion immediately and save the mp3 with the file name information

<img src="https://github.com/carlos-lehmann/wavtomp3/blob/main/readme-content/Add-Metadata.gif?raw=true" alt="Add Metadata" />

<a name="choose_title"/></a>
##### Release Title

<img src="https://github.com/carlos-lehmann/wavtomp3/blob/main/readme-content/Add-Release-Title.gif?raw=true" alt="Release Title" />

<a name="choose_artwork"/></a>
##### Choose Artwork

<img src="https://github.com/carlos-lehmann/wavtomp3/blob/main/readme-content/Choose-Artwork.gif?raw=true" alt="Choose Artwork" />

<a name="pick_genre"/></a>
##### Pick Genre

<img src="https://github.com/carlos-lehmann/wavtomp3/blob/main/readme-content/Pick-Genre.gif?raw=true" alt="Pick Genre" />

##### 3d. Reuse Metadata (Yes/No)

If there's more than 1 files in the folder, You'll be asked if you want to reuse the metadata for each track. If any of the above Metadata changes, please press No and go through the same process again.

<img src="https://github.com/carlos-lehmann/wavtomp3/blob/main/readme-content/Reuse-Metadata.gif?raw=true" alt="Reuse Metadata" />

### Convert & Save MP3

<img src="https://github.com/carlos-lehmann/wavtomp3/blob/main/readme-content/Convert-Save-MP3.gif?raw=true" alt="Convert & Save" />

### Result

<img src="https://github.com/carlos-lehmann/wavtomp3/blob/main/readme-content/Finished-Conversion.png?raw=true" alt="Result" />

### Don't forget to undo your changes for the executable

    sudo spctl --master-enable
