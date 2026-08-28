import tkinter as tk

from tkinter import PhotoImage, ttk


def centralizar_imagem(event):
    largura_janela = janela.winfo.width()
    altura_janela = janela.winfo.height()
    largura_imagem = imagem.width()
    altura_imagem = imagem.height()

    posicao_x = (largura_janela - largura_imagem) // 2
    posicao_y = (altura_janela - altura_imagem) // 2

    lbl_imagem.place(x=posicao_x, y=posicao_y)

janela = tk.Tk()
janela.title('Exibir Imagem')   
janela.geometry('400x250')

'''
Imagem de <a href="https://pixabay.com/pt/users/larchick-186124/?utm_source=link-attribution&utm_medium=referral&utm_campaign=image&utm_content=1136234">Lara Larina</a> por <a href="https://pixabay.com/pt//?utm_source=link-attribution&utm_medium=referral&utm_campaign=image&utm_content=1136234">Pixabay</a>
'''

imagem = PhotoImage(file='logo.png')

lbl_imagem = ttk.Label(janela, image=imagem)

janela.bind("<Configure>", centralizar_imagem)

lbl_imagem.pack()

janela.mainloop()