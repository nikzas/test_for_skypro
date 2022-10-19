
import random
import json


with open('morse-code.json', 'r') as mrz:
    mrz1 = json.load(mrz)


def start():
    a = input("Сегодня мы потренируемся расшифровывать морзянку.\n" 
              "Нажмите Enter и начнем")
    b = input("Добро пожаловать в игру!\n"
              "Введите Ваше имя:")
    aa = b.upper()
    name = input(f"Привет, {aa} , игра начинается! ")
    return



def morse_encode(text) -> str:
    oth = list(text)
    result = list()
    for i in oth:
        result += mrz1[i].split()
    return ' '.join(result)

def get_word():
    word = ["code", "bit", "list", "soul", "next"]


