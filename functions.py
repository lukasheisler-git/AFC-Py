from pydub import AudioSegment
import os

#convert Audio file 
def convert_file(name, format="wav", inplace=False):

    try:
        file_name, file_extension = os.path.splitext(name)
    except Exception as X:
        print(X)
        print("File extension missing ")
        return

    #import audio file
    src = AudioSegment.from_file(name)
    dst = file_name + "." + format 

    try:
        #convert to wav
        src.export(dst, format=format)
    except Exception as X:
        print(X)
        print("File cannot be converted to " + format)
    
    if(inplace):
        os.remove(name)

#convert folder of Audio files
def convert_folder(dir, format="wav", inplace=True, recursive=True):
    print("Test")




