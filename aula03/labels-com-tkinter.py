import tkinter as tk

janela = tk.Tk()
janela.geometry('300x200')
janela.title('Uso de Labels')

label = tk.Label(janela, text='Aula de labels')

label.pack()

janela.mainloop()