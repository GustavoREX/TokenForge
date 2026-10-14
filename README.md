# TokenForge Studio — revisão

Aplicativo Windows para criar tokens quadrados em PNG, com transparência, recorte circular e composição avançada de borda.

## Usar

Abra `dist\TokenForge.exe`. O Python não é necessário para executar o aplicativo compilado. A remoção de fundo usa o modelo U2Net; se não estiver no cache local, o rembg fará o download na primeira utilização. As ferramentas de composição não dependem desse download.

Para rodar pelos fontes, use `start.bat`. Para instalar as dependências em um ambiente virtual local, execute `setup.bat` uma vez.

## Criar um token com efeito de saída da borda

1. Importe a imagem. PNG com fundo transparente facilita o efeito; o botão **Remover fundo IA** também está disponível.
2. Na aba **Borda**, escolha uma das bordas ou importe um PNG/WebP. Ajuste o tamanho do anel para deixar espaço ao redor.
3. Ative **Modo avançado · 6 camadas**. A imagem passa a usar enquadramento livre, sem corte circular, e as abas de camadas ficam disponíveis.
4. Na aba **Camadas**, use **Ocultar pelo início** e **Ocultar pelo fim** para cada uma das quatro fatias. Os controles vão de 0 a 90 graus. A soma não pode ultrapassar 90 graus.
5. Desmarque **Mostrar fatia sobre a imagem** para ocultar a fatia inteira. **Mostrar todas** restaura os quatro intervalos completos; **Ocultar todas** coloca a imagem acima de toda a borda inferior.
6. Arraste a imagem na prévia para posicioná-la. A roda do mouse ajusta seu zoom. **Ajustar**, **Preencher** e **Centralizar imagem** estão na aba **Imagem**.
7. Na aba **Exportar**, escolha o lado do quadrado em pixels e exporte o PNG.

Ordem fixa, de baixo para cima:

- Borda completa.
- Imagem importada, com o enquadramento e o recorte escolhidos.
- Fatia 1: superior direita.
- Fatia 2: inferior direita.
- Fatia 3: inferior esquerda.
- Fatia 4: superior esquerda.

Os nomes dos quadrantes correspondem à rotação zero. A divisão pode ser girada de 0 a 90 graus; os números das guias acompanham essa rotação. Os ângulos são medidos no sentido horário a partir do topo. O fundo sólido, quando ativado, é o preenchimento da tela sob toda a composição.

As fatias usam máscaras não destrutivas da mesma borda e mantêm o centro e a escala da borda inferior. O PNG final é achatado; não é um arquivo de projeto com camadas reeditáveis.

## Recorte e exportação

- A prévia mostra o quadrado realmente exportado. Guias e xadrez são apenas auxiliares visuais.
- O token sempre é exportado com largura e altura iguais, entre 64 e 4096 pixels.
- Borda e recorte permanecem centralizados. A imagem pode ser deslocada de propósito; **Centralizar imagem** zera o deslocamento.
- **Ignorar margens transparentes** usa o conteúdo visível da imagem para ajustar o enquadramento.
- O modo simples usa recorte circular por padrão. No modo avançado, o padrão é quadrado livre, permitindo detalhes fora do anel; o recorte circular continua disponível.
- O editor de imagem também exporta quadrado por padrão. Desmarque **Exportar quadrado** para preservar o formato retangular da imagem. Seu campo numérico define o lado maior da saída.
- O overlay do editor mantém a mesma posição proporcional na prévia e na exportação.

## Bordas personalizadas

As 320 bordas originais estão incluídas. É possível adicionar arquivos em `borders` ao lado do executável ou em `%LOCALAPPDATA%\TokenForge\borders`, e usar **Atualizar biblioteca**. Arquivos do diretório do usuário têm preferência sobre bordas de mesmo nome distribuídas com o programa. O botão de importação também abre bordas diretamente de outras pastas, sem copiá-las.

## Compilar

```bat
setup.bat
build_tokenforge.bat
```

Saída: `dist\TokenForge.exe`, arquivo único, com ícone e bordas incorporadas. O modelo de IA não é incorporado ao EXE; permanece no cache do rembg.

Para reconstruir limpando o cache de compilação:

```bat
build_tokenforge.bat clean
```
