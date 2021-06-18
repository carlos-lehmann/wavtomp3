# wavtomp3

## Converts a choosen folder with wav files into an mp3 (same folder)
## Optionally will also save additional metadata to the mp3 like Artwork, Release Title or Genre

### special modules used
id3 tags: https://github.com/nicfit/eyeD3
conversion: https://github.com/jiaaro/pydub

### Prereqs
the pydub module uses ffmpeg for the conversion, so you'll need to install it:

[mac]: https://github.com/fluent-ffmpeg/node-fluent-ffmpeg/wiki/Installing-ffmpeg-on-Mac-OS-X
[windows]: https://windowsloop.com/install-ffmpeg-windows-10/
[linux]: https://linuxize.com/post/how-to-install-ffmpeg-on-debian-9/

### Default settings
- files are expected in format "artist - tracktitle.wav"
- file artist & tracktile will be used as minimal configuration metadata for the id3 tags
- bitrate is hard coded to 320k

### Flow

1.

> Choose a folder
> Test
> Choose whether to add additional metadata

2a. without metadata 

> conversion

2b. with metadata

> choose release title
> choose choose artwork
> choose genre

3b. for the next file you will be asked if you want to reuse the metadata

YES

> conversion

NO

> start again at 2b.
