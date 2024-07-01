import os
from pathlib import Path
import tkinter as tk
from tkinter import ttk

Estilos = {"1": "Nome_Função_Id (Ex: JoséMedinaFerreira_Atividade1_2312312)",
           "2": "Função_Nome_Id (Ex: Planilhas_RobertoFerreira_2312312)",
           "3": "CustomNome_CustomNome_CustomNome"}

def organizar_arquivos(diretorio_base, EstiloEscolhido):
    if EstiloEscolhido == "3":
        pasta_nome = input("Digite um nome para a Pasta Principal: ")

        pasta_sub_nome = input("Digite um nome para a sua Sub Pasta: ")


        contador = 0

        for item in diretorio_base.glob("*"):
            contador = contador + 1

            pasta_nome_completo = f"{pasta_nome}{contador}"
            diretorio_base_inicial = diretorio_base / pasta_nome_completo
            diretorio_base_inicial.mkdir(parents=True, exist_ok=True)

            pasta_sub_nome_completo = f"{pasta_sub_nome}{contador}"
            diretorio_sub_base_inicial = diretorio_base_inicial / pasta_sub_nome_completo
            diretorio_sub_base_inicial.mkdir(parents=True, exist_ok=True)


            novo_caminho = diretorio_sub_base_inicial / item.name
            item.rename(novo_caminho)
            print(item.name)

    elif EstiloEscolhido == "1":
        for item in diretorio_base.glob('*'):
            nome_pasta = item.name.split("_")[0]
            diretorio_base_inicial = diretorio_base / "".join(nome_pasta)
            diretorio_base_inicial.mkdir(parents=True, exist_ok=True)

            nome_sub_pasta = item.name.split("_")[1]
            diretorio_base_sub_inicial = diretorio_base_inicial / "".join(nome_sub_pasta)
            diretorio_base_sub_inicial.mkdir(parents=True, exist_ok=True)

            novo_caminho = diretorio_base_sub_inicial / item.name
            item.rename(novo_caminho)
            print(item.name)
    else:
        pass


    print("Pronto!")
    print("Seu arquivos estão organizados de acordo com o estilo esscolhido.")
    print("Aprecie o trabalho árduo de quase nada.")
    print("E obrigado por usar!")


# Documents/alu


# Função para verificiar se existe
def arquivo_verif(caminho_completo):
    # Verifica se a pasta existe
    if caminho_completo.exists():
        print("A pasta já existe.")
    else:
        # Cria a pasta se ela não existir
        caminho_completo.mkdir(parents=True, exist_ok=True)
        print(f"A pasta '{caminho_completo}' foi criada.")

"""# Descontinuada por enquanto porque eu TO DE SACO CHEIO DESSA POH
# todo - Função para construir o caminho da pasta.
def construir_caminho_completo(diretorio_base, tokens_caminho):
    # Começa com o diretório base fornecido pelo usuário
    caminho_base = Path(diretorio_base)

    # Junta os tokens para formar o caminho completo
    caminho_completo = caminho_base
    for token in tokens_caminho:
        caminho_completo /= token
    return caminho_completo
"""

def DefinirEstilo():
    print(Estilos)
    resposta_estilo = input("Qual estilo de organização você prefere?: ")
    for palavra_chave, resposta in Estilos.items():
        for palavra in palavra_chave:
            if palavra in resposta_estilo:
                print(f"Você escolheu o estilo {palavra_chave}. Seus arquivos estarão no formato '{resposta}'.")
                return palavra_chave
            else:
                break
    return "Desculpe, não entendi o que quis dizer."


#todo - Função principal que executa todo o código.
def questionario():
    EstiloEscolhido = DefinirEstilo()
    print("Tenha em mente que o formato precisa ser como foi especificado nos estilos.")
    print("A máquina usa como base o formato 'example_example_example', então mantenha o formato e não use mais do que dois '_'")
    estilo_confirmacao = input("Você confirma sua escolha? S/N: ")
    if estilo_confirmacao == "s" or "sim":
        pass
    else:
        questionario()


    #Saber se o usuário já possui uma pasta:
    possui_pasta = input("Você já possui uma pasta para a organização do projeto? S/N: ")
    possui_pasta.lower()
    if possui_pasta == "s":
        diretorio_base = Path.home() / Path(input("Digite o caminho da sua pasta (ex: Images/.../PastaDoArquivo): "))
        if diretorio_base.exists():
            print("Pasta encontrada.")
            print("Ela será usada para organizar os arquivos que já estão dentro dela.")
            maldicao = input("Se todos os arquivos ainda não estão dentro dela, por favor, coloque-os agora e logo depois digite 'Ok': ")
            if maldicao == "Ok" or "ok":
                organizar_arquivos(diretorio_base, EstiloEscolhido)

        else:
            print("Pasta não encontrada.")

        # Verificando se ela existe mesmo.
    else:
        criar_pasta = input("Deseja criar uma pasta?" "S/N: ")
        criar_pasta.lower()

        if criar_pasta == ("s" or "sim"):
            nome_pasta = input("Qual será o nome de sua pasta? Obs: Essa pasta será usada para armazenar e organizar todos os arquivos que você envia: ")
            caminho_documents = Path.home() / "Documents"
            caminho_completo = caminho_documents / nome_pasta
            permissao = input("Por padrão, a pasta será criada no diretório 'Documents', mas você pode trocar a pasta de lugar depois que os arquivos estiverem todos organizados dentro dela. Você permite a criação dessa pasta?: ")
            permissao.lower()

            if permissao == ("s" or "sim"):
                print("Ótimo!")
                arquivo_verif(caminho_completo)
                print("Agora resta apenas organizar os arquivos dentro dela.")
                print("Copie e cole, ou mova, todos os arquivos para a nova pasta criada.")
                resposta1 = input("Após todos os arquivos estárem lá dentro, digite 'Ok':")
                if resposta1 == "ok":
                    organizar_arquivos(caminho_completo, EstiloEscolhido)
                else:
                    pass
            else:
                print("Tudo bem. Se não acredita que o processo seja confiável, você pode criar uma pasta você mesmo e reiniciar o programa para utiliza-la.")
                reiniciar = input("Deseja reiniciar o programa?: ")
                reiniciar.lower()
                if reiniciar == ("s" or "sim"):
                    print("Bem vindo, novamente!")
                    questionario()
                #codigo pra reiniciar o programa
                else:
                    pass
                    #Codigo pra sair do programa.
        else:
            pass



def criar_pastas():
    caminho_documents = Path.home() / "Documents" / "alu"
    nome_pasta = input("Digite o nome: ")
    caminho_completo = caminho_documents / nome_pasta
    caminho_completo.mkdir(parents=True)


while True:
    questionario()
    break
