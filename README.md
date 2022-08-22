## :ledger: Telegram BOT / G1 - DF
Bot do Telegram que envia as últimas notícias do DF para um canal do Telegram, projeto desenvolvido usando Python e algumas bibliotecas! 
Imagens abaixo comparando as últimas noticias do site G1 com o canal do telegram.

## Notícias G1

![Noticias G1](./noticia.png)

## Canal Telegram

![Noticias G1](./telegram.png)

## Tecnologias Utilizadas

- Python;
- Telegram;
- Google Collab;
- Bibliotecas do Python
  - Beautifoul Soup
  - Telebot
  - Json
  - Requests
  
## Como Utilizar

Para quem está interessado vou demonstrar um tutorial mostrando como se deve fazer a configuração correta do bot e as modificações necessárias no código.

### Primeiro passo - Iniciar conversa com BotFather
No Telegram é necessário pesquisar pelo usuário BotFather e iniciar uma conversa.

### Segundo passo - Criação do bot no BotFather
Agora é importante passar alguns comandos para a criação do bot.

- /start  - Para começar o chat com o BotFather
- /newbot - Para criar um novo bot

Após o comando /newbot você irá definir o nome do seu bot, e depois o Username(@), é importante que o username termine com 'bot'.

Se tudo ocorreu corretamente, agora você ira receber o TOKEN do seu bot! Guarde esse TOKEN pois será importante.

Pronto! Seu bot agora está criado, entretanto ainda precisamos adicionar o bot em um grupo e definir o que o bot irá fazer, essas modificações serão feitas no código.

### Terceiro passo - Adicionando o bot em grupo
Crie um grupo no Telegram e adicione o seu bot! Será necessário o Username do bot, após isso o bot já estará no grupo.

Agora precisamos do ChatId, que será responsável por definir onde nosso bot irá enviar as mensagens.

No Telegram Web entre no grupo onde deseja que o bot envie as notícias (lembrando que o bot já deve estar adicionado no grupo) e na URL copie todos os caracteres após o caracter '#'.
### Último passo - Modificações no código
Agora baixe o código noticias_df_g1.py e use a IDE da sua preferência.
Precisamos fazer apenas duas alterações no código.
- Na linha 97 você deve inserir o TOKEN que recebeu do seu bot no Telegram no código connectTelegram('INSIRA AQUI O TOKEN')
- Na linha 100 você deve inserir o chatId no Telegram no código sendTelegram(bot, verificNoticias(noticiasDicionario()), INSIRA AQUI O CHATID)
