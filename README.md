# Organizador Automático de Arquivos

O Organizador Automático de Arquivos é uma ferramenta desenvolvida em Python para facilitar a organização  de arquivos baseada na nomenclatura de cada arquivo. O formato padrão requer que os arquivos sejam nomeados como "ExemploNome_ExNome_ExNome", com cada parte separada por dois underscores (_), idealmente contendo três partes distintas de texto.

## Funcionalidades Principais

- **Organização Automática**: Automatize a organização de arquivos com base na estrutura de nomes padronizada.
- **Flexibilidade de Nomenclatura**: Personalize o formato de nomeação escolhendo qual parte dos textos dos arquivos será utilizada para nomear a primeira e segunda pasta (Basicamente, você escolherá em qual fileira na nomenclatura dos arquivos - "1Fileira_2Fileira_3Fileira" - a máquina vai se basear pra criar as Pastas Principais e depois as Sub Pastas, que estarão dentro das primeiras, logo depois realocando os arquivos para suas respectivas nomenclaturas.)
- **Ideal para Professores e Gerentes**: Facilita a divisão de arquivos em diferentes pastas por nome, função ou identificação.
- **Interface Intuitiva**: Simples de configurar e utilizar, com opções claras para personalização.

## Como Usar

1. **Formato de Nomenclatura**: Certifique-se de que seus arquivos estejam nomeados conforme o formato "Name_Name_Name", garantindo consistência na organização.

2. **Personalização do Estilo**: Escolha um estilo para a organização. Existem atualmente apenas dois estilos. Padrão e Customizado(que por hora ainda não é tão funcional).
   
3. **Personalização da Organização**: Escolha qual parte dos textos dos arquivos será utilizada para nomear a Pasta Principal e a Sub Pasta, adaptando o sistema às suas necessidades específicas.

4. **Especificar Pasta**: Especifique o caminho até sua pasta no formato, "Image/gaucho/PastaComOsArquivosDentro", ou crie uma pasta com o próprio programa e coloque os arquivos dentro dela. 

5. **Execução do Programa**: Execute o programa para iniciar o processo de organização automática dos seus arquivos.


   ```
   python main.py
   ```

## Observações 

- Existen dois arwuivos. Um deles é executado nativamente no próprio Python e o outro possui uma interface simples e executável feita pelo Tkinter, mas ambos funcionam da mesma forma. Porém a versao feita pelo Tkinter, claro, é mais complexa.
  

## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para reportar bugs, sugerir melhorias ou enviar pull requests para aprimorar este projeto.
