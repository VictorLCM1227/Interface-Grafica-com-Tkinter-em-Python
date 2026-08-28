import tkinter as tk

janela = tk.Tk()

janela.title('Janela Principal')
janela.geometry('500x400+200+100')
janela.config(bg='lightblue')

# janela.maxsize(800, 600)
# janela.minsize(300, 200)
# janela.resizable(False, False)
# janela.state('zoomed')
# janela.attributes('-alpha', 0.6)
janela.iconbitmap('favicon.ico')

janela.mainloop()