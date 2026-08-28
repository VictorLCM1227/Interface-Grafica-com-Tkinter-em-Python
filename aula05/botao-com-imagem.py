import tkinter as tk

janela = tk.Tk()
janela.title('Botão com Imagem')
janela.geometry('300x300')

def fechar_janela():
    janela.destroy()

imagem = tk.PhotoImage(file='botao.png')

botao_imagem = tk.Button(janela, image=imagem, command=fechar_janela)
botao_imagem.pack(pady=10)

janela.mainloop()