import tkinter as tk

def abrir_segunda_janela():
    segunda_janela = tk.Toplevel()
    segunda_janela.title('Segunda Janela')
    segunda_janela.config(bg='#20EE70')

    largura_janela = 300
    altura_janela = 200

    largura_tela = segunda_janela.winfo_screenwidth()
    altura_tela = segunda_janela.winfo_screenwidth()

    x = (largura_tela - largura_janela) // 2
    y = (altura_tela - altura_janela) // 2

    segunda_janela.geometry(f'{largura_janela}x{altura_janela}+{x}+{y}')

janela_principal = tk.Tk()
janela_principal.title('Janela Principal')
janela_principal.geometry('600x500')

janela_principal.bind('<Button-1>', lambda event: abrir_segunda_janela())

janela_principal.mainloop()