from logging import exception

from pytube import YouTube
from tkinter.filedialog import *
from tkinter import *
from tkinter.messagebox import *
from threading import *

file_size = 0


def progress(stream=None, chunk=None, file_handel=None, remaining=None):
    file_downloaded = (file_size - remaining)
    per = (file_downloaded / file_size) * 100
    dBtn.config(text="{}% downloaded".format(per))


def startdownlod():
    global file_size
    try:
        url = urlfield.get()
        print(url)

        dBtn.config(text='please wait...')
        dBtn.config(state=DISABLED)

        path = askdirectory()
        print(path)

        ob = YouTube(url, on_progress_callback=progress)

        # strms = ob.streams.all()

        # for s in strms:
        # print(s)
        strms = ob.streams.first()
        file_size = strms.filesize
        print(file_size)
        # print(strms.filesize)
        # print(strms.title)
        # print(ob.title)
        # print(ob.description
        strms.download(path)
        print("Done")
        dBtn.config(text="done")
        dBtn.config(state=NORMAL)
        showinfo("download finished", "downloded")
        urlfield.delete(0, END)
    except exception as e:
        print(e)
        print("error")


def startdownloadthread():
    thread = Thread(target=startdownlod)
    thread.start()


main = Tk()

main.title("youtube downloader")

main.iconbitmap('download.ico')

main.geometry('500x600')

file = PhotoImage(file='download2.png')

headingIcon = Label(main, image=file)
headingIcon.pack(side=TOP)

urlfield = Entry(main, font=('verdana', 18), justify=CENTER)
urlfield.pack(side=TOP, fill=X, padx=10)

dBtn = Button(main, text="start download", font=("verdana", 18), command=startdownloadthread)
dBtn.pack(side=TOP, pady=10)

main.mainloop()
