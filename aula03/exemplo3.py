import tkinter as tk
from tkinter import PhotoImage, ttk


def centralizar_imagem(event=None):
    largura_janela = janela.winfo_width()
    altura_janela = janela.winfo_height()

    largura_imagem = imagem.width()
    altura_imagem = imagem.height()

    posicao_x = (largura_janela - largura_imagem) // 2
    posicao_y = (altura_janela - altura_imagem) // 2

    lbl_imagem.place(x=posicao_x, y=posicao_y)


janela = tk.Tk()

janela.title('Exibir Imagem')
janela.geometry('400x250')


imagem = PhotoImage(file='logo.png')

imagem = imagem.subsample(32, 32)


lbl_imagem = ttk.Label(
    janela,
    image=imagem
)

janela.bind("<Configure>", centralizar_imagem)

lbl_imagem.pack()

centralizar_imagem()

janela.mainloop()