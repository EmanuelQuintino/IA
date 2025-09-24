import tkinter as tk
from tkinter import messagebox

def somar():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        resultado = num1 + num2
        label_resultado.config(text=f"Resultado: {resultado}")
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira números válidos.")

# Criar a janela principal
janela = tk.Tk()
janela.title("Calculadora de Soma")

# Criar os widgets
tk.Label(janela, text="Número 1:").grid(row=0, column=0, padx=10, pady=10)
entry_num1 = tk.Entry(janela)
entry_num1.grid(row=0, column=1, padx=10, pady=10)

tk.Label(janela, text="Número 2:").grid(row=1, column=0, padx=10, pady=10)
entry_num2 = tk.Entry(janela)
entry_num2.grid(row=1, column=1, padx=10, pady=10)

botao_somar = tk.Button(janela, text="Somar", command=somar)
botao_somar.grid(row=2, column=0, columnspan=2, pady=10)

label_resultado = tk.Label(janela, text="Resultado: ")
label_resultado.grid(row=3, column=0, columnspan=2, pady=10)

# Iniciar o loop da interface
janela.mainloop()