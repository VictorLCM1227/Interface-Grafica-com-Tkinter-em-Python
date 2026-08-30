import tkinter as tk
from tkinter import ttk

janela = tk.Tk()
janela.title('Exemplo de pack')

btn1 = ttk.Button(janela, text='Botão 1')
btn2 = ttk.Button(janela, text='Botão 2')
btn3 = ttk.Button(janela, text='Botão 3')
btn4 = ttk.Button(janela, text='Botão 4')

btn1.pack(side='top')
btn2.pack(side='bottom')
btn3.pack(side='left')
btn4.pack(side='right')

janela.mainloop()