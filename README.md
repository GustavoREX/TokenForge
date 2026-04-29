# TokenForge

Neste programa, você pode criar tokens a partir de imagens, com ou sem bordas, possibilitando também a adição de bordas personalizadas diretamente na pasta.



## Atualizações

<ins>{Estou modificando o programa para adicionar algumas features de edição de imagem, então estou migrando para uma base mais modular. No entanto, ainda estou mantendo o código antigo presente no arquivo .old.py}</ins>

<ins>{Já existe um editor de imagem simples, que atualmente permite apenas a remoção de fundo por IA. Mais features de edição serão adicionadas futuramente}</ins>

*** Arquivos de "QUICK START" adicionados para facilitar o uso durante o período de desenvolvimento ***

> Para utilizar o programa sem configurar um ambiente manualmente, basta executar o `start.bat`. Ele irá instalar as bibliotecas necessárias e rodar o programa. Caso queira executar sem o `.bat`, siga as instruções de instalação mais abaixo.

> É necessário ter o Python 3 instalado para rodar o programa e baixar as dependências via pip.



## Descrição

Contando com uma ferramenta simples de remoção de fundo, você também pode criar tokens de imagens já sem fundo.

Tenha cautela, pois a ferramenta é simples e funciona melhor em imagens nas quais o fundo e o personagem retratado sejam bem distintos.

Ela apresenta melhores resultados em imagens com fundo de cor sólida e bem diferente do personagem.

O programa é simples, mas faz o que promete sem muita complicação: basta selecionar a imagem, escolher o tipo de token que deseja criar e clicar em salvar.



## Bibliotecas extras e observações para rodar o programa

Este código é a base crua do projeto, ou seja, é necessária a compilação caso queira utilizá-lo como `.EXE`.

Para aqueles que querem o `.EXE`, rode o comando abaixo (é possível que você precise instalar algumas bibliotecas Python antes):

<kbd>python -m PyInstaller --noconfirm --windowed --onedir --name TokenForge --icon token.ico --add-data "borders;borders" --collect-all rembg --collect-all onnxruntime --collect-all pymatting --copy-metadata pymatting --copy-metadata rembg --copy-metadata onnxruntime TokenForge.py</kbd>

Vou deixar também os comandos para instalação das bibliotecas necessárias abaixo, caso queira rodar o código sem compilar ou compilar por conta própria.



### Bibliotecas básicas de interface gráfica e manipulação de imagens

<kbd>pip install pillow ttkbootstrap tkinterdnd2</kbd>


### Rembg

(A ferramenta que permite a remoção do background das imagens)

<kbd>pip install rembg</kbd>


### onnxruntime

(Basicamente um pacote necessário para o Rembg rodar localmente. Como ele utiliza uma IA simples para remover fundos, precisa do onnxruntime para funcionar.)

<kbd>pip install rembg onnxruntime</kbd>


### PyInstaller

(Usado para compilação do programa)

<kbd>pip install pyinstaller</kbd>

Talvez você encontre algumas outras bibliotecas faltando, mas geralmente basta procurar como instalá-las. Normalmente será algo como:

<kbd>pip install nome-da-biblioteca</kbd>