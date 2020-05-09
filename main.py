from tkinter import *
from pytube import YouTube
from tkinter.filedialog import *





file_size = 0

def startdownlod(url):
    global file_size
    try:

        path = askdirectory()

        ob = YouTube(url)

        # strms = ob.streams.all()

        # for s in strms:
        # print(s)
        strms = ob.streams.first()
        # print(strms.filesize)
        # print(strms.title)
        # print(ob.title)
        # print(ob.description
        strms.download(path)
        print("Done")

    except exception as e:
        print(e)
        print("error")

main = Tk()

main.title("youtube downloader")

main.iconbitmap('download.ico')

main.geometry('500x600')

file=PhotoImage(file ='download2.png')


class Lable(main,image):
    pass


headingIcon=Lable(main,image='file')
headingIcon.pack(side=top)

urlfield = Entry(main)
urlfield.pack(side=top)

main.mainloop()
