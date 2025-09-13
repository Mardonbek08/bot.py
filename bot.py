# ascii_clock.py

import time
import os
from pyfiglet import Figlet
from datetime import datetime
from colorama import init, Fore, Style

# Ranglar funksiyasini ishga tushirish (Windowsda ishlashi uchun)
init(autoreset=True)


def clear_terminal():
    """
    Terminalni tozalaydi (Windows va Linux uchun mos)
    """
    os.system('cls' if os.name == 'nt' else 'clear')


def show_ascii_clock():
    """
    Har soniyada ASCII san’atda vaqt va rangli sana ko‘rsatadigan soat
    """
    figlet = Figlet(font='slant')  # Boshqa fontlar: 'big', 'block', 'standard', 'doom'

    try:
        while True:
            clear_terminal()

            # Joriy vaqt va sana
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            current_date = now.strftime("%d-%m-%Y, %A")  # Misol: 13-09-2025, Saturday

            # ASCII san’atda vaqt
            ascii_time = figlet.renderText(current_time)

            # Ekranga chiqarish
            print(Fore.GREEN + Style.BRIGHT + "📅 Sana: " + current_date + "\n")
            print(Fore.CYAN + ascii_time)
            print(Fore.YELLOW + Style.DIM + "⏱ Ctrl+C bosing — to‘xtatish uchun")

            # Kutish
            time.sleep(1)

    except KeyboardInterrupt:
        print(Fore.RED + "\n⛔ Soat to‘xtatildi. Xayr!")


if __name__ == "__main__":
    show_ascii_clock()
