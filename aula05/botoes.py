import tkinter as tk
from datetime import date

def mostrar_data():
    hoje = date.today()
    texto_data.set(hoje.strftime('%d/%m/%Y'))

janela = tk.Tk()
janela.title('Mostrar a Data')
janela.geometry('300x200')

texto_data = tk.StringVar()

label_data = tk.Label(janela, textvariable=texto_data, font=('Arial', 14))
label_data.pack(pady=20)

botao_data = tk.Button(janela, text='Mostrar Data', command=mostrar_data, bg='blue', fg='white')
botao_data.pack(pady=10)

janela.mainloop()