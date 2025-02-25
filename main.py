from pytubefix import YouTube
from pytubefix.cli import on_progress
from tkinter import *

def baixar_video():
    url = entrada.get()
    destino = "downloads"

    yt = YouTube(url, on_progress_callback=on_progress)
    print("\n", yt.title)

    ys = yt.streams.get_highest_resolution()

    ys.download(output_path=destino)
    print("\n \n Download Concluído!")


janela = Tk()
janela.title('Downloader de Vídeos do YouTube')
texto = Label(janela, text='Insira abaixo a URL do Vídeo:')
texto.grid(row=1, column=1)

entrada = Entry(janela, width=50)
entrada.grid(row=3, column=1)

btn = Button(janela, text='Baixar vídeo', command=baixar_video)
btn.grid(row=5, column=1)

Tk.mainloop(janela)