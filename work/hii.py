from pytube import YouTube
from tkinter.filedialog import *
from tkinter.messagebox import*
from tkinter import *
from threading import*
font=('verdana', 20)
file_size =0
def completedownload(stream=None, file_path=None):
    print("download completed")
    showinfo("mesage","file has been downloaded...")
    downloadBtn['text']="download video"
    downloadBtn['state']="active"
    urlfield.delete(0, END)

def progressDownload(stream=None, chunk=None, bytes_remaining=None):
    percent = (100 *((file_size - bytes_remaining)/file_size))
    downloadBtn['text'] = "{:00.0f}% download ". format(percent)


def startDownload(url):
    global file_size
    path_to_save = askdirectory()
    if path_to_save is None:
        return

    try:
        yt =YouTube(url)
        st = yt.streams.first()

        yt.register_on_complete_callback(completedownload)
        yt.register_on_progress_callback(progressDownload)

        file_size = st.filesize
        st.download(output_path=path_to_save)
    except Exception as e:
        print(e)
        print("something went worng")

def btnclicked():
    try:
        downloadBtn['text'] = "please wait..."
        downloadBtn['state'] = 'disabled'
        url = urlfield.get()
        if url =='':
            return
        print(url)
        thread = Thread(target=startDownload, args=(url,))
        thread.start()
    except Exception as e:
        print(e)

root=Tk()
root.title("youtube downloader")
root.geometry("500x600")

urlfield = Entry(root,font=font,justify=CENTER)
urlfield.pack(side=TOP,fill=X,padx=10)
urlfield.focus()

downloadBtn=Button(root,text="download video",font=font, relief='ridge',command=btnclicked)
downloadBtn.pack(side=TOP,pady=20)

root.mainloop()

    
