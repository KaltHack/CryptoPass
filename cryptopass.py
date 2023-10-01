import random
from colorama import *
import time as t

t.sleep(0.5)

print(Fore.GREEN + """
 ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
█─▄▄▄─█▄─▄▄▀█▄─█─▄█▄─▄▄─█─▄─▄─█─▄▄─█▀▀▀▀▀██▄─▄▄─██▀▄─██─▄▄▄▄█─▄▄▄▄█
█─███▀██─▄─▄██▄─▄███─▄▄▄███─███─██─█████████─▄▄▄██─▀─██▄▄▄▄─█▄▄▄▄─█
▀▄▄▄▄▄▀▄▄▀▄▄▀▀▄▄▄▀▀▄▄▄▀▀▀▀▄▄▄▀▀▄▄▄▄▀▀▀▀▀▀▀▀▄▄▄▀▀▀▄▄▀▄▄▀▄▄▄▄▄▀▄▄▄▄▄▀
""")

t.sleep(1)

t.sleep(1)
main = int(input(Fore.YELLOW + """
    ¿Qué cantidad de caracteres quieres para tu contraseña? 
                 Recomendado: 12-16
    > """))



min = "qwertyuiopasdfghjklñzxcvbnm"
may = "QWERTYUIOPASDFGHJKLÑZXCVBNM"
num = "0123456789"
sym = ".,!?;:()[]{}+-/=<>$@#&*"

str = min + may + num + sym 
length = main
password = "".join(random.sample(str,length))
t.sleep(1)

print(Fore.YELLOW + "Espera un momento, Se está creando tu contraseña!...")
t.sleep(2)
print(Fore.GREEN + """
    La contraseña generada es:
            """, Fore.YELLOW + password,
Fore.GREEN + """
    Vuelve a ejecutar si quieres una nueva contraseña! 
""")