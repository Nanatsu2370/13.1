from os import getenv

# TELEGRAM
OWNER = int(getenv('6015655407'))
if OWNER is None:
    raise Exception("Por favor configura tu Telegram User ID") 

API_ID = int(getenv('21080457'))
if API_ID is None:
    raise Exception("Por favor configura el API_ID del Bot") 

API_HASH = getenv('6750c69ea23536737d68e8b9bcccdb92')
if API_HASH is None:
    raise Exception("Por favor configura el API_HASH del Bot") 

TELEGRAM_TOKEN = getenv('6381935149:AAFUi16_hdwF8jOLLpsJQusoxQCnl5BHV3Q')
if TELEGRAM_TOKEN is None:
    raise Exception("Por favor configura el TOKEN del Bot") 

# DATOS DEL MOODLE
HOST = getenv('https://cursad.jovenclub.cu/')
if HOST is None:
    raise Exception("Por favor configura la URL del Moodle") 

ACCOUNT = getenv('carlosdevss')
if ACCOUNT is None:
    raise Exception("Por favor configura tu nombre de usuario del Moodle") 

PASSWORD = getenv('Carlos060706*')
if PASSWORD is None:
    raise Exception("Por favor configura tu contraseña del Moodle") 

# CUENTA DE MEGA
PASS_MEGA = getenv('Carlos060706')
if PASS_MEGA is None:
    raise Exception("Por favor configura tu contraseña de GMAIL") 

GMAIL_MEGA = getenv('carlos2737daniel@gmail.com')
if GMAIL_MEGA is None:
    raise Exception("Por favor configura tu correo de GMAIL") 

# ARCHIVOS
MEGABYTES = int(getenv('50'))
if MEGABYTES is None:
    raise Exception("Por favor configura los MEGABYTES a los que se dividirán los archivos") 