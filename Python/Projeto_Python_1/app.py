import tkinter as tk
from data import products
import pandas as pd


def get_product_by_id():
    result = []
    valor_entrada = entrada.get()

    for element in products:
        if element["id"] == int(valor_entrada):
            print(element)


janela = tk.Tk()
janela.title("projeto pranchas")
janela.geometry("1080x920")

titulo = tk.Label(janela, text="Bem vindo", font=("arial", 20, "bold"))
entrada = tk.Entry(janela)
botao = tk.Button(janela, text="buscar", command=get_product_by_id)

titulo.pack()
entrada.pack()
botao.pack()


janela.mainloop()
