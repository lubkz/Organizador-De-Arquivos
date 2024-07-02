import os
from pathlib import Path
import tkinter as tk
from tkinter import ttk

Estilos = {"1": "Padrão : Nome_Função_Id; Função_Nome_Id; Nome_Id_Função; Etc; (Ex: JoséMedinaFerreira_Atividade1_2312312)",
           "2": "Customizado : CustomNome_CustomNome_CustomNome"}

Formatos = {"1": "Primeira parte. (Aqui_Pasta_Pasta)",
            "2": "Segunda parte. (Pasta_Aqui_Pasta)",
            "3": "Terceira parte. (Pasta_Pasta_Aqui)"
}

# Variáveis responsáveis pelo Formato Padrão
def definir_formato(EstiloEscolhido):
    if EstiloEscolhido == "1":
        print(Formatos)
        print("O estilo padrão escolhe, por padrão, o nome das pastas pelo nome escrito nos arquivos.")
        print("Dessa forma, ele vai escolher o primeiro e o ultimo nome do arquivo, separado com '_', para a Pasta Principal e a Sub Pasta, respectivamente.")
        decidir_formato = input("Caso, porém, deseje que seus arquivos sejam nomeados em outra ordem, digite 'Trocar'. Caso deseje manter, digite 'Manter': ")
        decidir_formato = decidir_formato.lower()
        if decidir_formato == "trocar":
            # Definir o formato em que as pastas serão organizadas.
            print(Formatos)
            primeira_pasta = eval(input("Qual parte dos textos dos arquivos você deseja que seja o nome da sua Primeira leva de pastas?: "))
            print(Formatos)
            segunda_pasta = eval(input("Qual parte dos dos textos dos arquivos você deseja que seja o nome da sua Segunda leva de pastas?: "))
            primeira_pasta -= 1
            segunda_pasta -= 1
            return primeira_pasta, segunda_pasta
        else:
            print("Ok! Você escolheu manter o formato padrão.")
            return 0, 2
    else:
        print("Eu e casca de bala")
        return 0, 2

def organizar_arquivos(diretorio_base, EstiloEscolhido, primeira_pasta, segunda_pasta):
    if EstiloEscolhido == "2":
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
        contador = 0

        for item in diretorio_base.glob('*'):
            nome_pasta = item.name.split("_")[primeira_pasta]
            diretorio_base_inicial = diretorio_base / "".join(nome_pasta)
            diretorio_base_inicial.mkdir(parents=True, exist_ok=True)

            contador += 1
            nome_sub_pasta = item.name.split("_")[segunda_pasta]
            nome_sub_pasta_completo = f"{nome_sub_pasta}{contador}"
            diretorio_base_sub_inicial = diretorio_base_inicial / "".join(nome_sub_pasta_completo)
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
    print(EstiloEscolhido)
    estilo_confirmacao = input("Você confirma sua escolha? S/N: ")
    if estilo_confirmacao == "s" or "sim":
        pass
    else:
        questionario()

    # Definindo os valores do Formatos de cada pasta.
    primeira_pasta, segunda_pasta = definir_formato(EstiloEscolhido)

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
                organizar_arquivos(diretorio_base, EstiloEscolhido, primeira_pasta, segunda_pasta)

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
                    organizar_arquivos(caminho_completo, EstiloEscolhido, primeira_pasta, segunda_pasta)
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
