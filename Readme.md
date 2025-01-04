# TwitchBot

Twitch Bot para enviar mensajes relacionados con un canal de Twitch. Contiene una serie de comandos preintegrados que son configurables.

## Instalación

Para utilizar este bot, necesitaras tener instalado [Twitchio](https://twitchio.dev/en/stable/index.html) y tener un token de conexión [oauth con Twitch](https://dev.twitch.tv/docs/chat/authenticating/).

Necesitarás crear 3 variables de entorno ```TOKEN```, ```CLIENT_ID``` y ```CHANNELS``` para guardar el Token, el CLIENT_ID y el nombre del canal. 

**NOTA**: Puedes crear un fichero .env para crear las variables de entorno.

No olvides que para instalar las dependencia de twitchio, puedes usar la siguiente instrucción:

```bash
pip install twitchio
```

O puedes usar ```pipenv``` para instalar y ejecutar el bot.


```bash
pipenv install
```

## Ejecutar el Bot

Una vez creadas las variables e instaladas la dependencias, podemos ejecutar el Bot.

```bash
python twitchbot.py
```
En caso de utilizar pipenv, puedes utilizar un fichero .env para guardar las variables.

```bash
pipenv run startbot
```

### Docker

Se ha añadido un fichero Dockerfile para poder crear un contenedor con el Bot; para construir la imagen:

```bash
docker build -t mkgtwitchbot .
```

```bash
docker run --rm --env TOKE=<yourtoken> --env CLIENT_ID=<clientid> --env CHANNELS=<yourchannel> mkgtwitchbot
```
Ó Puedes usar un fichero ```.env```

```bash
docker run --rm --env-file=.env mkgtwitchbot
```

## Comandos

Todos los comandos empiezan por el prefijo ```!```. Los comandos disponibles son:

* horario
* redes
* discord
* especial
* web

### Horario

Muestra el horario actual de los Streams. Es un mensaje fijo (revisa el fichero python para más información).

### Redes

Muestra la lista de redes sociales; esta información se obtiene de un fichero json llamado ```redes.json```; tiene la siguiente estructura:

```json
{
    "twitter": "<direccion twitter/x>", 
    "Bsky":"<Dirección Bluesky>",
    "mastodon": "<Dirección Mastodon>",
    "discord": "<Dirección Discord>"
}
```

En cada propiedad poner la dirección que corresponda.

### Discord

Muestra un mensaje con la dirección de la invitación a la comunidad de discord. La información se obtiene del fichero ```redes.json```.

### Especial

Este comando muestra el mensaje del siguiente Stream especial. Obtiene la información de un fichero llamado ```especial.json```; que tiene la siguient estructura:

```json
{
    "fecha": "28-Nov",
    "tema": "Beatem'Up (SoR, Golden Axe, TMNT, etc.)"
}
```

Donde:

* fecha: Indica la fecha del siguiente Stream especial.
* tema: Indica la descripción de la temática del siguiente Stream especial.

### Web

Muestra información sobre una web del canal. Obtiene los datos desde el fichero ```redes.json```.