import tkinter as tk
from pytube import YouTube
from tkinter import messagebox
import customtkinter
import datetime
import validators



def descarga():
    url = YouTube(str(link.get()))
    video = url.streams.first()
    video.download()
    #tk.Label(root, text="video descargado :v", font="arial 15").place(x=100, y=120)
    tk.messagebox.showinfo("descargador", "descarga terminada")
root = customtkinter.CTk()
root.title("descargador :v")
root.geometry('600x300')
root.resizable(width=False,height=False)
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")

link = tk.StringVar()
#tk.Label(root, text=" YouTube Download", font='arial 14 bold').pack()
#tk.Label(root, text="link enter", font='arial 17 bold').place(x=150, y=55)
#link_enter = tk.Entry(root, width=85, textvariable=link, font="arial 15 bold", bg="violet").place(x=30, y=85)
#tk.Button(root, text='Descargar', font='arial 16 bold' , padx=2, command=descarga).place(x=225, y=150)

frame = customtkinter.CTkFrame(master=root,
                               width=400,
                               height=230,
                               corner_radius=10,
                               fg_color=("white", "gray10"))
frame.pack(padx=80, pady=20)

entry = customtkinter.CTkEntry(master=frame,
                               placeholder_text="Ingrese el enlace :V",
                               width=300,
                               height=25,
                               border_width=2,
                               corner_radius=2)
entry.place(relx=0.5, rely=0.5, anchor=tk.S)
#entry.pack(padx=20, pady=10)
'''def verificacion():
    x = entry
    if x == str:
        messagebox.showinfo(message="URL valida", title="Título")
    else:
        messagebox.showinfo(message="URL no valida", title="Título")
'''

boton1 = customtkinter.CTkButton(master=root,
                                 width=10,
                                 height=30,
                                 border_width=0,
                                 corner_radius=4,
                                 #image="/c.png",
                                 text="Descargar",
                                 )
boton1.place(relx=0.6, rely=0.7, anchor=tk.SW)
boton2 = customtkinter.CTkButton(master=root,
                                 width=10,
                                 height=30,
                                 border_width=0,
                                 corner_radius=4,
                                 #image="/c.png",
                                 text="Comprobar",
                                 )
boton2.place(relx=0.4, rely=0.7, anchor=tk.SE)
boton3 = customtkinter.CTkButton(master=root,
                                 width=10,
                                 height=30,
                                 border_width=0,
                                 corner_radius=4,
                                 #image="/c.png",
                                 text="Calidad",
                                 )
boton3.place(relx=0.5, rely=0.7, anchor=tk.S)
text_var = tk.StringVar(value="YouTube Download")
label = customtkinter.CTkLabel(master=frame,
                               textvariable=text_var,
                               width=150,
                               height=30,
                               corner_radius=8,
                               #bg_color=("gray10"),
                               text_color=("white"),
                               text_font='arial 16 bold')
label.place(relx=0.5, rely=0.1, anchor=tk.N)

root.mainloop()






















'''from pytube import YouTube
url = "https://youtu.be/3IWBkDQG9D8" #url
yt = YouTube(url)
detalles = yt.title, yt.views, yt.author, yt.streams, yt.age_restricted, yt.description
print(detalles)
strm = (yt.streams.filter(file_extension='mp4'))
print(strm)
down = yt.streams.get_by_itag('18')
down.download()
print(':v')'''