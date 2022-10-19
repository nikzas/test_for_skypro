
import random
import json


with open('morse-code.json', 'r') as mrz:
    mrz1 = json.load(mrz)


def main():
    input("Сегодня мы потренируемся расшифровывать морзянку.\n" 
              "Нажмите Enter и начнем")
    b = input("Добро пожаловать в игру!\n"
              "Введите Ваше имя:")
    name = b.upper()
    print(f"Привет, {name} , игра начинается! ")
    print(true_or_false())


def print_statistics(answers):
    return "Статистика не готова"


def true_or_false():
    """Вывод тру или фолс ответа"""
    count = 1
    stop = 0
    while count > stop:
        gen_word = get_word()
        gen_morze = morse_encode(gen_word)    #Генерация морзянки
        print(f"Слово {count} -", gen_morze)    #Вывод поз обозначения слова

        in_word = input("Введите ваш ответ:")   #Ввод слова пользователем

        verif = morse_encode(in_word.lower())   #Перевод слова в нижний регистр и проверка между морзянкой

        if verif == gen_morze:
            print(f"Верно, {in_word}! ")
        elif verif != gen_morze:
            print(f"Неверно, {gen_word}! ")
        count += 1





def morse_encode(text) -> str:
    """функция создания морзянки"""
    oth = list(text)
    result = list()
    for i in oth:
        result += mrz1[i].split()
    return ' '.join(result)


def get_word():
    """выбрасывание рандомных слов"""
    word = ["code", "bit", "list", "soul", "next"]
    return random.choice(word)
