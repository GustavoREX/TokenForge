# TokenForge

Neste programa, Você pode criar tokens de imagens, com ou sem bordas, possibilitando tambem a adição de boras perssonalisadas diretamente na pasta

Contando com uma ferramenta simples de remoção de fundo de imagem, você tambem pode criar tokens de imagens sem fundo.
Tenha caltela, ja que a ferramente é simples e funciona melgor em imagens da qual os detalhes de fundo e a personagem retratada são bem distintos
funionando muito melhor em imagens de fundo em cor solida bem distinta da personagem

O programa é simples mas faz o que promete sem muita complicação, basta selecionar a imagem, escolher o tipo de token que deseja criar e clicar em salvar


Esse codigo é a base crua, ou seja, é nescessario a compilação se quiser que ele funcione com um .EXE

Para aqueles que querem o .EXE, rode esse comando de compilação (é possivel que você tenha que baixar algumas bibliotecas Python para isso)

python -m PyInstaller --noconfirm --windowed --onedir --name TokenForge --icon token.ico --add-data "borders;borders" 
--collect-all rembg --collect-all onnxruntime --collect-all pymatting --copy-metadata pymatting --copy-metadata rembg 
--copy-metadata onnxruntime TokenForge.py

vou deixar os comandos para instalação das bibliotecas necessárias aqui, caso queira rodar o código sem compilar, ou queira compilar por conta própria


Blibliotecas basicas de interface grafica e manipulação de imagens
pip install pillow ttkbootstrap tkinterdnd2

Rembg (a ferramente que permite a remoção da BackGround das imagens)
pip install rembg
onnxruntime (basicamente um pacote de dados para a Rembg rodar local, ela é uma IA simples para remover o fundo das imagens então presisa do onnxruntime para rodar localmente)
pip install rembg onnxruntime

Pyistaller (que é para rodar o compilador)

pip install pyinstaller

talvez você encontre algumas outras bibliotecas que podem estar faltando, mas é so procurar como instar elas, o que geralmente vai ser algo como
pip install nome-da-biblioteca

