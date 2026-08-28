import tkinter as tk
from datetime import date

def mostar_data():
    hoje = date.today()
    texto_data.set(hoje.strftime('%d%m%Y'))

janela = tk.Tk()