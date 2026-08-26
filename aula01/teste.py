import tkinter as tk

janela = tk.Tk()
janela.title('Primeiro App')
janela.geometry('300x100+20+20')

lblMsg = tk.Label(janela, text='Eu te amo muito!')
lblMsg.pack()

janela.mainloop()