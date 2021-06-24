# wavtomp3

## Converts a choosen folder with wav files into an mp3
### Optionally will also save additional metadata to the mp3 like Artwork, Release Title and Genre

### Packages used
- id3 tags: https://github.com/nicfit/eyeD3
- conversion: https://github.com/jiaaro/pydub

### Prereqs
the pydub package uses ffmpeg for the conversion, so you'll need to install it:

- [mac](https://github.com/fluent-ffmpeg/node-fluent-ffmpeg/wiki/Installing-ffmpeg-on-Mac-OS-X)
- [windows](https://windowsloop.com/install-ffmpeg-windows-10/)
- [linux](https://linuxize.com/post/how-to-install-ffmpeg-on-debian-9/)

### Default settings
- files are expected in format "artist - tracktitle.wav"
- the above information will be used as minimal configuration metadata for the id3 tags
- bitrate is hard coded to 320k
- files will be exported to the same directory as the wav files

### Flow

1.

> Choose a folder

> Choose whether to add additional metadata

2a. without metadata 

> conversion starts & id3 tags are written (artist / tracktitle & year) to all files

> program finished!

2b. with metadata for the first file

> choose release title

> choose choose artwork

> choose genre

3b. for each next file you will be asked if you want to reuse the metadata

YES
> next file

NO

> start again at 2b.

4b. once all files metadata information is collected
> conversion starts & id3 tags are written

> program finished!
