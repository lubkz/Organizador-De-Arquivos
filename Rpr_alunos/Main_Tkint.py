import os
from pathlib import Path
import tkinter as tk
from tkinter import ttk

# Obtém o caminho para a pasta "Documents"
caminho_documents = Path.home() / "Documents"
nome_pasta = "Alunos_atividades"
caminho_completo = caminho_documents / nome_pasta

def arquivo_verif():
    # Verifica se a pasta existe
    if caminho_completo.exists():
        print("A pasta já existe.")
    else:
        # Cria a pasta se ela não existir
        caminho_completo.mkdir(parents=True)
        print(f"A pasta '{caminho_completo}' foi criada.")

janela_principal = tk.Tk()
janela_principal.title("Página Inicial")
janela_principal.geometry("720x500")

botao_iniciar = ttk.Button(text="Iniciar avaliação", command=arquivo_verif)
botao_iniciar.pack()

janela_principal.mainloop()