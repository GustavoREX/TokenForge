# TokenForge

Neste programa, Você pode criar tokens de imagens, com ou sem bordas, possibilitando tambem a adição de boras perssonalisadas diretamente na pasta

## Atualizações


<ins>{estou modificando o programa para a adição de algumas features de edição de imagem, então estou migrando para uma base mais modular. no então estou mantendo o antigo codigo ainda presente no .old.py}</ins>

<ins>{ja esta com um editor de imagem simples que atualmente apenas permite a remoção por IA do fundo da imagem, mais features de edição serão adicionadas mais tarde}</ins>

*** Adicionado arquivos de "QUICK START" para facilitar o uso ainda em periodo de desenvolvimento ***
> para utilizar o programa sem um ambiente, apenas rode o start.bat, ele vai instalar as bibliotecas necessárias e rodar o programa, caso queira rodar o programa sem o .bat, basta seguir as instruções de instalação das bibliotecas mais abaixo

> é nessessario ter o Python 3 instalado para rodar o programa e conseguir baixar as dependencias pelo pip.

## Descrição

Contando com uma ferramenta simples de remoção de fundo de imagem, você tambem pode criar tokens de imagens sem fundo.
Tenha caltela, ja que a ferramente é simples e funciona melgor em imagens da qual os detalhes de fundo e a personagem retratada são bem distintos
funionando muito melhor em imagens de fundo em cor solida bem distinta da personagem

O programa é simples mas faz o que promete sem muita complicação, basta selecionar a imagem, escolher o tipo de token que deseja criar e clicar em salvar

### Bibliotecas extras e adendos para rodar o programa

Esse codigo é a base crua, ou seja, é nescessario a compilação se quiser que ele funcione com um .EXE

Para aqueles que querem o .EXE, rode esse comando de compilação (é possivel que você tenha que baixar algumas bibliotecas Python para isso)

 <kbd>python -m PyInstaller --noconfirm --windowed --onedir --name TokenForge --icon token.ico --add-data "borders;borders" --collect-all rembg --collect-all onnxruntime --collect-all pymatting --copy-metadata pymatting --copy-metadata rembg --copy-metadata onnxruntime TokenForge.py </kbd>

vou deixar os comandos para instalação das bibliotecas necessárias aqui, caso queira rodar o código sem compilar, ou queira compilar por conta própria


Blibliotecas basicas de interface grafica e manipulação de imagens

 <kbd>pip install pillow ttkbootstrap tkinterdnd2 </kbd>

Rembg (a ferramente que permite a remoção da BackGround das imagens)

 <kbd>pip install rembg </kbd>

onnxruntime (basicamente um pacote de dados para a Rembg rodar local, ela é uma IA simples para remover o fundo das imagens então presisa do onnxruntime para rodar localmente)

 <kbd>pip install rembg onnxruntime </kbd>

Pyistaller (que é para rodar o compilador)

 <kbd>pip install pyinstaller </kbd>

talvez você encontre algumas outras bibliotecas que podem estar faltando, mas é so procurar como instar elas, o que geralmente vai ser algo como
pip install nome-da-biblioteca

