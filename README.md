# Sumário

- [Sumário](#sumário)
- [Discord Bot: Bot Motivacional](#discord-bot-bot-motivacional)
  - [Video de exemplo das funções](#video-de-exemplo-das-funções)
  - [To - Do List - Bot Motivacional](#to---do-list---bot-motivacional)
  - [To - Do List - Bot Gerente](#to---do-list---bot-gerente)
  - [Requerimentos](#requerimentos)
    - [Requerimentos Python](#requerimentos-python)
    - [Requerimentos Sites externos](#requerimentos-sites-externos)

# Discord Bot: Bot Motivacional

Este bot irá mandar frases motivacionais para os usuários através dos comandos:

```bash
/oi - O Bot se apresenta
/frase - Lista uma frase aleatória em inglês
/motiva - Lista uma frase aleatória em português

```

## Video de exemplo das funções

[![IMAGE ALT TEXT HERE](http://img.youtube.com/vi/9I16gP6x9gY/0.jpg)](http://www.youtube.com/watch?v=9I16gP6x9gY)

## To - Do List - Bot Motivacional

- [ ] Bot Motivacional
  - [x] importar bibliotecas primarias
  - [x] criar conta no developers discord
  - [x] fazer o bot iniciar
  - [x] fazer o bot responder a um comando fazer o bot verificar as conversas e mandar uma frase motivacional se houver uma palavra triste na frase
  - [x] upar o bot em algum serviço, para que ele fique sempre On-line
  - [ ] criar um comando 'Help' que lista os comandos e uma breve descrição sobre o que o comando faz

## To - Do List - Bot Gerente

- [ ] Bot Gerente
  - [x] importar bibliotecas primarias
  - [x] fazer o bot iniciar
  - [ ] fazer o bot responder a um comando fazer o bot verificar as conversas e mandar uma frase motivacional se houver uma palavra triste na frase
  - [ ] upar o bot em algum serviço, para que ele fique sempre On-line
  - [ ] criar um comando 'Help' que lista os comandos e uma breve descrição sobre o que o comando faz

## Requerimentos

### Requerimentos Python

Instale as seguintes dependencias para que o bot começe a funcionar:

```bash

pip install discord==1.0.1
pip install discord.py==1.5.1
pip install json5==0.9.5
pip install jsonschema==3.2.0
pip install requests==2.24.0
pip install requests-oauthlib==1.3.0
pip install requests-toolbelt==0.9.1
pip install requests2==2.16.0

```

### Requerimentos Sites externos

[Repl it](https://repl.it/) - Para rodar o bot se não funcionar no Windows

[Uptime robot](https://uptimerobot.com/) - Para ficar pingando o web service do bot para garantir que o Replit não fique off-lie
