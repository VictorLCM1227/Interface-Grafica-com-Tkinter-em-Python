import tkinter as tk
from tkinter import ttk

janela = tk.Tk()
janela.title('Exemplo de pack')

btn1 = ttk.Button(janela, text='Top', width=10)
btn2 = ttk.Button(janela, text='Bottom', width=10)
btn3 = ttk.Button(janela, text='Left', width=10)
btn4 = ttk.Button(janela, text='Right', width=10)

btn1.pack(side='top', pady=5)
btn2.pack(side='bottom', pady=5)
btn3.pack(side='left', padx=15)
btn4.pack(side='right', padx=5)




janela.mainloop()