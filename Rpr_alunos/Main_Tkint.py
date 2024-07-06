import os
from pathlib import Path
import tkinter as tk
from tkinter import ttk
from tkinter import Label
from tkinter import Entry, Button, Frame
from PIL import Image, ImageTk

# Variáveis globais
EstiloEscolhido = None
FormatoEscolhido = None
primeira_pasta = None
segunda_pasta = None
caminho_completo = None
diretorio_base = None

Estilos = {"1": "Padrão : Nome_Função_Id; Função_Nome_Id; Nome_Id_Função; Etc; (Ex: JoséMedinaFerreira_Atividade1_2312312)",
           "2": "Customizado : CustomNome_CustomNome_CustomNome (Ainda não está pronto!)"}

Estilos_form = {"Padrão": ": 'Texto_Texto_Texto'",
                "Customizado": ": CustomNome_CustomNome_CustomNome (Ainda não está pronto!)"}

Formatos = {"1": "Primeira parte. (Aqui_Pasta_Pasta)",
            "2": "Segunda parte. (Pasta_Aqui_Pasta)",
            "3": "Terceira parte. (Pasta_Pasta_Aqui)"}


def apresentacao_estilo():
    # Exibição do estilos na Janela.
    for label in Estilos.values():
        texto_label = Label(frame_principal, text=label)
        texto_label.pack()

    # Primeira pergunta:
    resposta_estilo = Label(frame_principal, text="Qual estilo de organização você prefere?: ")
    entrada.pack()
    botao_enviar = Button(frame_principal, text="Enviar", command=lambda: [limpar_frame_principal(), DefinirEstilo()])
    botao_enviar.pack()


def DefinirEstilo():
    global EstiloEscolhido

    resposta_estilo = entrada.get()
    for palavra_chave, resposta in Estilos.items():
        for palavra in palavra_chave:
            if palavra in resposta_estilo:
                for chave, valor in Estilos_form.items():
                    texto_label = Label(frame_principal, text=f"Você escolheu o estilo {chave}.", wraplength=500)
                    texto_label.pack()
                    texto_label = Label(frame_principal, text=f"Seus arquivos estarão no formato{valor}", wraplength=500)
                    texto_label.pack()
                    print("Deu certo")
                    break

                EstiloEscolhido = palavra
                print(EstiloEscolhido)
                questionario()
            else:
                break


    return "Desculpe, não entendi o que quis dizer."


def questionario():
    global EstiloEscolhido

    entrada.delete(0, "end")

    if EstiloEscolhido in {"1", "2"}:
        texto_label = Label(frame_principal, text=f"Tenha em mente que o formato precisa ser como foi especificado nos estilos.", wraplength=500)
        texto_label.pack()

        texto_label = Label(frame_principal, text="A máquina usa como base o formato 'example_example_example', então mantenha o formato e não use mais do que dois '_'", wraplength=500)
        texto_label.pack()

        texto_label = Label(frame_principal, text="Você confirma sua escolha? S/N: ", wraplength=500)
        texto_label.pack()

        botao_sim = Button(frame_principal, text="Sim", command=lambda: [limpar_frame_principal(),definir_formato()])
        botao_sim.pack()
        botao_nao = Button(frame_principal, text="Não", command=lambda: [limpar_frame_principal(), apresentacao_estilo()])
        botao_nao.pack()
    else:
         print("Estilo escolhido não reconhecido.")


# Variáveis responsáveis pelo Formato Padrão
def definir_formato():
    global EstiloEscolhido
    global FormatoEscolhido

    entrada.delete(0, "end")

    if EstiloEscolhido == "1":
        print("EstiloEscolhido")
        texto_label = Label(frame_principal, text=f"{Formatos}", wraplength=500)
        texto_label.pack()

        texto_label = Label(frame_principal, text=f"O estilo padrão escolhe, por padrão, o nome das pastas pelo nome escrito nos arquivos.", wraplength=500)
        texto_label.pack()

        texto_label = Label(frame_principal, text=f"Dessa forma, ele vai escolher o primeiro e o ultimo nome do arquivo, separado com '_', para a Pasta Principal e a Sub Pasta, respectivamente.", wraplength=500)
        texto_label.pack()

        texto_label = Label(frame_principal, text=f"Caso, porém, deseje que seus arquivos sejam nomeados em outra ordem, digite 'Trocar'. Caso deseje manter, digite 'Manter': ", wraplength=500)
        texto_label.pack()

        entrada.pack()

        botao_enviar = Button(frame_principal, text="Enviar", command=lambda: [limpar_frame_principal(), definir_formato2()])
        botao_enviar.pack()
    else:
        print("nao estou fincionad bapai")


def definir_formato2():
    global primeira_pasta
    global segunda_pasta

    resposta_formato = entrada.get()

    entrada.delete(0, "end")

    resposta_formato = resposta_formato.lower()
    if resposta_formato == "trocar":
        # Definir o formato em que as pastas serão organizadas.
        texto_label = Label(frame_principal, text=f"{Formatos}")
        texto_label.pack()

        texto_label = Label(frame_principal, text="Qual parte dos textos dos arquivos você deseja que seja o nome da sua Primeira leva de pastas?: ")
        texto_label.pack()

        entrada.pack()

        botao = Button(frame_principal, text="Enviar", command=lambda: [limpar_frame_principal(), definir_formato3()])
        botao.pack()
    elif resposta == "manter":
        texto_label = Label(frame_principal, text="Ok! Você escolheu manter o formato padrão.")
        texto_label.pack()

        primeira_pasta = 0
        segunda_pasta = 1

        definir_pasta()


def definir_formato3():
    global primeira_pasta

    primeira_pasta = entrada.get()
    primeira_pasta = int(primeira_pasta)
    print(primeira_pasta)

    entrada.delete(0, "end")

    texto_label = Label(frame_principal, text="Qual parte dos textos dos arquivos você deseja que seja o nome da sua Segunda leva de pastas?: ")
    texto_label.pack()

    entrada.pack()

    botao = Button(frame_principal, text="Enviar", command=lambda: [limpar_frame_principal(), definir_formato4()])
    botao.pack()


def definir_formato4():
    global primeira_pasta
    global segunda_pasta

    segunda_pasta = entrada.get()
    segunda_pasta = int(segunda_pasta)
    print(segunda_pasta)

    entrada.delete(0, "end")

    primeira_pasta -= 1
    segunda_pasta -= 1

    print(primeira_pasta, segunda_pasta)

    definir_pasta()



def definir_pasta():
    # Saber se o usuário já possui uma pasta:
    texto_label = Label(frame_principal,text="Você já possui uma pasta para a organização do projeto? S/N: ")
    texto_label.pack()

    entrada.pack()

    botao = Button(frame_principal, text="Enviar", command=lambda: [limpar_frame_principal(), definir_pasta2()])
    botao.pack()


def definir_pasta2():
    possui_pasta = entrada.get()

    entrada.delete(0, "end")

    possui_pasta = possui_pasta.lower()
    if possui_pasta in {"s", "sim"}:
        texto_label = Label(frame_principal, text="Digite o caminho da sua pasta (ex: Images/.../PastaDoArquivo): ")
        texto_label.pack()

        entrada.pack()

        botao = Button(frame_principal, text="Enviar", command=lambda: [limpar_frame_principal(), definir_pasta3()])
        botao.pack()

    elif possui_pasta in {"n", "nao", "não"}:
        texto_label = Label(frame_principal, text="Deseja criar uma pasta?" "S/N: ")
        texto_label.pack()

        entrada.pack()

        botao = Button(frame_principal, text="Enviar", command=lambda: [limpar_frame_principal(), criar_pasta_nova()])
        botao.pack()


def definir_pasta3():
    global diretorio_base

    caminho = entrada.get()
    diretorio_base = Path.home() / Path(caminho)

    entrada.delete(0, "end")

    if diretorio_base.exists():
        texto_label = Label(frame_principal, text="Pasta encontrada.")
        texto_label.pack()

        texto_label = Label(frame_principal, text="Ela será usada para organizar os arquivos que já estão dentro dela.")
        texto_label.pack()

        texto_label = Label(frame_principal, text="Se todos os arquivos ainda não estão dentro dela, por favor, coloque-os agora e logo depois digite 'Ok': ")
        texto_label.pack()

        botao = Button(frame_principal, text="Ok", command=lambda: [limpar_frame_principal(), organizar_arquivos()])
        botao.pack()

def criar_pasta_nova():
        criar_pasta = entrada.get()
        criar_pasta = criar_pasta.lower()

        if criar_pasta in {"s", "sim"}:
            texto_label = Label(frame_principal, text="Qual será o nome de sua pasta? Obs: Essa pasta será usada para armazenar e organizar todos os arquivos que você envia: ")
            texto_label.pack()

            entrada.pack()

            botao = Button(frame_principal, text="Enviar", command=lambda: [limpar_frame_principal(), criar_pasta_nova2()])
            botao.pack()

        elif criar_pasta in {"n", "nao"}:
            texto_label = Label(frame_principal, text="Tudo bem. Se não acredita que o processo seja confiável, você pode criar uma pasta você mesmo e reiniciar o programa para utiliza-la.")
            texto_label.pack()

            texto_label = Label(frame_principal, text="Deseja reiniciar o programa? S/N: ")
            texto_label.pack()

            entrada.pack()

            botao = Button(frame_principal, text="Enviar", command=lambda: [limpar_frame_principal(), reiniciar_prog()])
            botao.pack()

def reiniciar_prog():
    reiniciar = entrada.get()
    reiniciar = reiniciar.lower()
    if reiniciar == ("s" or "sim"):
        texto_label = Label(frame_principal, text="Bem vindo, novamente!")
        texto_label.pack()

        questionario()
    else:
        tk.Tk().destroy()


def criar_pasta_nova2():
    global caminho_completo

    nome_pasta = entrada.get()

    caminho_documents = Path.home() / "Documents"
    caminho_completo = caminho_documents / nome_pasta

    texto_label = Label(frame_principal, text="Por padrão, a pasta será criada no diretório 'Documents', mas você pode trocar a pasta de lugar depois que os arquivos estiverem todos organizados dentro dela. Você permite a criação dessa pasta?: ")
    texto_label.pack()

    entrada.pack()

    botao = Button(frame_principal, text="Enviar", command=lambda: [limpar_frame_principal(), criar_pasta_nova3()])
    botao.pack()

def criar_pasta_nova3():
    permissao = entrada.get()
    permissao = permissao.lower()

    if permissao in {"s", "sim"}:
        texto_label = Label(frame_principal, text="Ótimo!")
        texto_label.pack()

        arquivo_verif()

        texto_label = Label(frame_principal, text="Agora resta apenas organizar os arquivos dentro dela.")
        texto_label.pack()

        texto_label = Label(frame_principal, text="Copie e cole, ou mova, todos os arquivos para a nova pasta criada.")
        texto_label.pack()

        texto_label = Label(frame_principal, text="Após todos os arquivos estárem lá dentro, digite 'Ok': ")
        texto_label.pack()

        entrada.pack()

        botao = Button(frame_principal, text="Enviar", command=lambda: cria_pasta_nova4())
        botao.pack()


def cria_pasta_nova4():
    resposta1 = entrada.get()
    resposta1 = resposta1.lower()

    if resposta1 == "ok":
        organizar_arquivos()
    else:
        pass


def organizar_arquivos():
    global diretorio_base
    global EstiloEscolhido
    global caminho_completo
    global primeira_pasta
    global segunda_pasta

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
        # Contador foi aposentado
        # contador = 0

        for item in diretorio_base.glob('*'):
            nome_pasta = item.name.split("_")[primeira_pasta]
            diretorio_base_inicial = diretorio_base / "".join(nome_pasta)
            diretorio_base_inicial.mkdir(parents=True, exist_ok=True)

            # Contador aposentado clt
            #contador += 1
            nome_sub_pasta = item.name.split("_")[segunda_pasta]

            # Contador aposentado clt
            #nome_sub_pasta_completo = f"{nome_sub_pasta}{contador}"
            nome_sub_pasta_completo = f"{nome_sub_pasta}"
            diretorio_base_sub_inicial = diretorio_base_inicial / "".join(nome_sub_pasta_completo)
            diretorio_base_sub_inicial.mkdir(parents=True, exist_ok=True)

            novo_caminho = diretorio_base_sub_inicial / item.name
            item.rename(novo_caminho)

            #texto_label = Label(frame_principal, text=f"{item.name}")
            #texto_label.pack()
    else:
        pass

    texto_label = Label(frame_principal, text="Pronto!")
    texto_label.pack()

    texto_label = Label(frame_principal, text="Seu arquivos estão organizados de acordo com o estilo esscolhido.")
    texto_label.pack()

    texto_label = Label(frame_principal, text="Aprecie o trabalho árduo de quase nada.")
    texto_label.pack()

    texto_label = Label(frame_principal, text="E obrigado por usar!")
    texto_label.pack()

    congrats = Image.open("congrats.jpg")
    congrats_tk = ImageTk.PhotoImage(congrats)
    label_imagem = tk.Label(frame_abaixo, image=congrats_tk)
    label_imagem.image = congrats_tk
    label_imagem.pack()


# Função para verificiar se existe
def arquivo_verif():
    global caminho_completo

    # Verifica se a pasta existe
    if caminho_completo.exists():
        print("A pasta já existe.")
    else:
        # Cria a pasta se ela não existir
        caminho_completo.mkdir(parents=True, exist_ok=True)
        print(f"A pasta '{caminho_completo}' foi criada.")


# Função principal que executa o código.




# Criação rápida de pastas para testes.
def criar_pastas():
    caminho_documents = Path.home() / "Documents" / "alu"
    nome_pasta = input("Digite o nome: ")
    caminho_completo = caminho_documents / nome_pasta
    caminho_completo.mkdir(parents=True)

# Função para limpar o frame principal antes de adicionar novos elementos
def limpar_frame_principal():
    for widget in frame_principal.winfo_children():
        widget.pack_forget()

# Início da produção do Tkinter e janelas.
janela_principal = tk.Tk()
janela_principal.title("Página Inicial")
largura_x = 720
largura_y = 500
janela_principal.geometry(f"{largura_x}x{largura_y}")

frame_principal = Frame(janela_principal)
frame_principal.pack(expand=True, fill='both')

frame_abaixo = Frame(janela_principal)
frame_abaixo.pack(expand=True)

entrada = Entry(frame_principal)

botao_iniciar = Button(frame_principal, text="Iniciar avaliação", command=lambda: [limpar_frame_principal(), apresentacao_estilo()])
botao_iniciar.pack()

janela_principal.mainloop()