import tkinter as tk
from tkinter import messagebox

def somaButton():
    n1 = float(entry1.get())
    n2 = float(entry2.get())
    soma = n1 + n2
    label.config(text=f"Resultado: {soma}")

def subtracao():
    n1 = float(entry1.get())
    n2 = float(entry2.get())
    subtracao = n1 - n2
    label.config(text=f"Resultado: {subtracao}")

def multiplicacao():
    n1 = float(entry1.get())
    n2 = float(entry2.get())
    
    # Corrigindo a verificação para n1 e n2
    if n1 == 0 or n2 == 0:
        multiplicacao = 0
    else:
        multiplicacao = n1 * n2
    
    label.config(text=f"Resultado: {multiplicacao}")

def divisao():
    n1 = float(entry1.get())
    n2 = float(entry2.get())
    
  
    if n2 == 0:
        divisao = "Erro: Divisão por zero"
    else:
        divisao = n1 / n2
    
    label.config(text=f"Resultado: {divisao}")

root = tk.Tk()
root.title("Calculadora")
root.geometry("400x400")

label = tk.Label(root, text="Selecione uma Operação")
label.pack()

# Recebendo os Inputs
entry1 = tk.Entry(root)
entry1.pack(pady=5)

entry2 = tk.Entry(root)
entry2.pack(pady=2)

label = tk.Label(root, text="")
label.pack()

button = tk.Button(root, text="Soma", command=somaButton)
button.pack(pady=10)

button = tk.Button(root, text="Subtração", command=subtracao)
button.pack(pady=10)

button = tk.Button(root, text="Multiplicação", command=multiplicacao)
button.pack(pady=10)

button = tk.Button(root, text="Divisão", command=divisao)
button.pack(pady=10)

root.mainloop()
