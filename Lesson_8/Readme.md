### Learning goals:
* Work with file directory  - os Lib
* Imageio Lib
* Create GIF with mimsave
* Convert text to voice with gtts Lib
* Play Sounds with vlc Lib
________________________________________________

## Exercise program:

### Create GIF
OS:
The OS module in Python provides functions for creating and removing a directory (folder), fetching its contents, changing and identifying the current directory, etc.

Imageio:
Imageio is a Python library that provides an easy interface to read and write a wide range of image data, including animated images, volumetric data, and scientific formats. 

In this exercise, we are going to read some images from the desired directory, then create a gif file from the sorted list of these images.

Example output:

<img src="gif_maker/output.gif" />
__________________________________________________________________________

### Convert text to audio
Adding the ability to convert the translated text (in the previous lesson) to audio and play it
gTTS:
gTTS (Google Text-to-Speech), a Python library and CLI tool to interface with Google Translate's text to speech API. Writes spoken mp3 data to a file, a file-like object (bytestring) for further audio manipulation, or stdout. It features flexible pre-processing and tokenizing.

VLC:
The VLC media player is an open-source and free media player software that is portable and can be used on multiple platforms. 
We can utilize the VLC media player with the help of Python as well. For this we need to install the python-vlc module
