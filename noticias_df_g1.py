!pip3 install pyTelegramBotAPI
!pip3 install --upgrade pyTelegramBotAPI
!pip3 install requests
!pip3 install json
!pip3 install BeautifulSoup

import telebot
import requests
import json
from bs4 import BeautifulSoup

// Estabelece a conexão do código com o TOKEN do bot
def connectTelegram(API_TOKEN):
  API_TOKEN = API_TOKEN
  bot = telebot.TeleBot(API_TOKEN)
  return bot

def noticiasDicionario():
  url = 'https://g1.globo.com/df/distrito-federal/ultimas-noticias/'
  # Faz uma requisição da página e armazena apenas o conteúdo na variável.
  content = (requests.get(url)).content

  # Converte o conteúdo para HTML com melhor visualização.
  site = BeautifulSoup(content, "html.parser")

  # Busca todas as notícia do site.
  noticias = site.findAll('div', attrs={"class": 'feed-post-body'})

  noticias_dicionario = {}
  i = 0

  # Percorre as notícias e retorna o título, resumo, imagem e link de cada uma.
  for noticia in noticias:
    titulo = noticia.find('a', attrs={"class": 'feed-post-link'})

    # Verifica se não possui a palavra "VÍDEO" no título e retorna o titulo, resumo e link da noticia.
    if((titulo.text).find("VÍDEO") == -1 ):

      i = i + 1
      resumo = noticia.find('div', attrs={"class": 'feed-post-body-resumo'})
      link = titulo['href']
      imagem = noticia.find('img', attrs={"class": 'bstn-fd-picture-image'})

      # Nem todas as notícias possuem imagem, as que não possuir imagem será atribuido uma imagem para elas
      if(imagem == None):
        imagem = (BeautifulSoup("<img src='https://s2.glbimg.com/PoRq4JTZFjj5lKuykrJ4zZYkkms=/540x304/top/smart/https://i.s3.glbimg.com/v1/AUTH_59edd422c0c84a879bd37670ae4f538a/internal_photos/bs/2022/B/8/8EugYKQ5efPwDuqPcXrg/52232492084-9a52f1aa27-k.jpg'")).img

      # .text retorna apenas o conteúdo dentro das TAG's HTML.
      # A cada iteração adiciona uma chave com o valor do Título, e dentro da chave possui o resumo, link e a imagem.
      noticias_dicionario['noticia' + str(i)] = [titulo.text, resumo.text, link, imagem['src']]
  return noticias_dicionario

def verificNoticias(noticias_dicionario):
  # Se não exisitr a noticias controle nos arquivos ela vai ser criada, e passada todas as notícias.
  noticias_telegram = {}
  try:
    with open('noticias_controle.json', 'r') as json_file:
      noticias_controle = json.load(json_file)

    # Faz a verificação as notícias armazenadas na variável com as noticias controle.
    # As notícias que não forem iguais irão para a noticias_telegram, onde serão diviguldas sem repetição.
    for i in range(len(noticias_dicionario)):
      if(noticias_dicionario['noticia' + str(i+1)][0] != noticias_controle['noticia' + str(i+1)][0]):
        noticias_telegram['noticia' + str(i+1)] = noticias_dicionario['noticia' + str(i+1)]
        # As que não forem repetidas irão ser inseridas em noticias_controle.
        noticias_controle['noticia' + str(i+1)] = noticias_dicionario['noticia' + str(i+1)]

    # Salva as novas notícias no arquivo.
    with open('noticias_controle.json', 'w') as json_file:
          json.dump(noticias_controle, json_file, indent = 4)
  except:
    with open('noticias_controle.json', 'w') as json_file:
      json.dump(noticias_dicionario, json_file, indent = 4)
    noticias_telegram = noticias_dicionario
  return noticias_telegram

# Cada iteração envia uma notícia para o telegram.
def sendTelegram(bot, noticias_telegram, chatId):
  for i in range(len(noticias_telegram)):
    titulo = noticias_telegram['noticia' + str(i+1)][0]
    resumo = noticias_telegram['noticia' + str(i+1)][1]
    link = noticias_telegram['noticia' + str(i+1)][2]
    imagem = noticias_telegram['noticia' + str(i+1)][3]

    bot.send_photo(
      # ID do chat que o BOT vai enviar as mensagens.
      chat_id = chatId,
      # Foto de cada notícia
      photo = noticias_telegram['noticia' + str(i+1)][3],
      # Texto de cada notícia
      caption = "<b>" + noticias_telegram['noticia' + str(i+1)][0] + "</b>\n\n" + noticias_telegram['noticia1'][1] + "\n\n" + noticias_telegram['noticia1'][2],
      # Permite "Adicionar" Tags HTML no texto.
      parse_mode = "HTML"
    )

# Finaliza a conexão com o Telegram.
bot = connectTelegram('5650155995:AAG9HM64roEuzdKNTNuK9GV4All_d1OV5JQ')

# Envia as noticias para o Telegram.
sendTelegram(bot, verificNoticias(noticiasDicionario()), -655568266)