import socket
from ip2geotools.databases.noncommercial import DbIpCity 
import pyshorteners
import os
def cls():
  os.system('cls' if os.name=='nt' else 'clear')
cls()
GREEN='\033[32m'
MAGENTA='\033[35m'
backgr = GREEN + f'''
 _____ _ _       _____                 
/  ___(_) |     /  ___|                
\ `--. _| |_ ___\ `--.  ___ __ _ _ __  
 `--. \ | __/ _ \`--. \/ __/ _` | '_ \ 
/\__/ / | ||  __/\__/ / (_| (_| | | | |
\____/|_|\__\___\____/ \___\__,_|_| |_|    
BY Pulatov Kamran
{MAGENTA}[1] Сканирование сайта
[2] Укоротить сссылку
'''
print(backgr)
func = input('Введите номер: ')
if func == 1:
  q = input('Введите домен>')
  try:
    siteip = socket.gethostbyname(q)
    print(f"Ip адрес сайта(цельный) {q}>>>{GREEN}{socket.gethostbyname(q)}") 
    response = DbIpCity.get(siteip, api_key='free')
    print(GREEN + "Город: "+ response.city+"\nСтрана: "+ response.country+"\nРегион: "+ response.region+"\nШирота: "+ str(response.latitude)+"\nДолгота: "+ str(response.longitude))
  except:
    print('[!] Произошла ошибка. Проверьте правильность дмена или интернета')
elif func == 2:
  url = input("Введите URL: ")
  print(pyshorteners.Shortener().tinyurl.short(url))
  
