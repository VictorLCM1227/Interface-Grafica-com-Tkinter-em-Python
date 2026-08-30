import tkinter as tk
from tkinter import ttk

janela = tk.Tk()
janela.title('Exemplo de pack')

lbl1 = ttk.Label(janela, text='Label 1', background='green')
lbl2 = ttk.Label(janela, text='Label 2', background='orange')
lbl3 = ttk.Label(janela, text='Label 3', background='cyan')
lbl4 = ttk.Label(janela, text='Label 4', background='magenta')

lbl1.pack(side='top', expand=True, fill='x')
lbl2.pack(side='top', pady=20)
lbl3.pack(side='top', expand=True, fill='y')
lbl4.pack(side='top', expand=True, fill='both')




janela.mainloop()