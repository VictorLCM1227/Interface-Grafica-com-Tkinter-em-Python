import tkinter as tk
from tkinter import ttk

janela = tk.Tk()
janela.title('Exemplo de Grid Básico')
janela.geometry('300x100')

label1 = ttk.Label(janela, text='Widget 1', width=20, background='red')
label2 = ttk.Label(janela, text='Widget 2', width=20, background='green')
label3 = ttk.Label(janela, text='Widget 3', width=40, background='blue')

label1.grid(row=0, column=0)
label2.grid(row=0, column=1)
label3.grid(row=1, column=0, columnspan=2)

janela.mainloop()