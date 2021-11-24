import pytube
from tkinter import *
from tkinter import ttk
from tkinter import messagebox



def search_v(link):
    link_v.delete(0,"end")
    yt = pytube.YouTube(link)
    vid = yt.streams.filter(file_extension='mp4').order_by('resolution')
    l_vid.delete(0,'end')

    for i in vid:
        d_vid[f"{i.resolution}"] = i
        l_vid.insert(END,f"{i.resolution}")
    


def search_a(link):
    link_a.delete(0,"end")
    yt = pytube.YouTube(link)
    aud = yt.streams.filter(mime_type="audio/mp4")
    l_aud.delete(0,'end')

    for i in aud:
        d_aud[f"{i.abr}"] = i
        l_aud.insert(END,f"{i.abr}")




def download(obj):
    obj.download()
    messagebox.showinfo("Listo :D", "Video descargado con exito")

#global window_vd, window_aud
global d_vid, d_aud, l_vid, l_aud #datos de audios y videos
global link_v, link_a

x_l= 100#Coordx listas
y_l= 100#Coordy listas
d_vid = {}
d_aud = {}

wn = Tk()
wn.geometry("500x500")
wn.resizable(0,0)
wn.title("Descargador de videos de Youtube x Andrey BETA(v0.3)")

nt = ttk.Notebook(wn)
nt.pack(fill = 'both', expand="yes")
window_vd = ttk.Frame(nt)
window_aud = ttk.Frame(nt)
nt.add(window_vd, text= "Videos")
nt.add(window_aud, text= "Audio")

l_vid = Listbox(window_vd)
l_vid.place(x = x_l, y =y_l)
l_aud = Listbox(window_aud)
l_aud.place(x = x_l, y = y_l)

Label(window_vd, text="Resoluciones").place(x = 0, y = y_l + 50)
Label(window_aud, text="Peso").place(x = 0, y = y_l + 50)

link_v = Entry(window_vd)
link_v.place(x = 50, y = 50)
Button(window_vd, text = "Search", command = lambda: search_v(link_v.get())).place(x = 200, y = 50)
Button(window_vd, text = "Download", command = lambda: download(d_vid[l_vid.get(ACTIVE)])).place(x = 200, y = y_l + 200)


link_a = Entry(window_aud)
link_a.place(x = 50, y = 50)
Button(window_aud, text = "Search", command = lambda: search_a(link_a.get())).place(x = 200, y = 50)
Button(window_aud, text = "Download", command = lambda: download(d_aud[l_aud.get(ACTIVE)])).place(x = 200, y = y_l + 200)


wn.mainloop()












