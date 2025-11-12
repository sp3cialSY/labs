from string import ascii_letters, digits
from random import randint

def make_zero(s: str, s0: str) -> str:
    if not s0 in s:
        return s
    
    for i in range(len(s) - len(s0) + 1):
        valid = True
        for j in range(len(s0)):
            if s[i+j] != s0[j]:
                valid = False
                break
        if valid:
            pos = i
            break
    
    new_s = ''
    for i in range(len(s)):
        if not (pos <= i < pos + len(s0)):
            new_s += s[i]

    return new_s

def task1(s: str, s0: str) -> str:
    if not s or not s0:
        return ValueError("Values must be not none")
    if not s0 in s:
        return s
    # return s.replace(s0, "", 1)
    return make_zero(s, s0)

def task2(text: str) -> bool:
    letters = "абвгдеёжзийклмнопрстуфхцчшщъьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЬЭЮЯ" + ascii_letters
    num_count = 0
    letters_count = 0
    for s in text:
        if s in letters:
            letters_count += 1
        elif s in digits:
            num_count += 1
    return letters_count > num_count

def maxx(l: list) -> int:
    if len(l) == 0:
        raise ValueError("Empty list!")
    m = l[0]
    for elem in l:
        if elem > m:
            m = elem
    return m

def task3(l: list, a: int, b: int) -> int:
    start_len = len(l)
    new_l = []
    for elem in l:
        if not (a <= abs(elem) <= b):
            new_l.append(elem)
    while len(new_l) < start_len:
        new_l.append(0)
    return new_l



if __name__ == "__main__":
    print("Задание 1")
    s = input("Введи строку S\n")
    s0 = input("Введи подстроку s0 для удаления из s:\n")
    if s or s0:
        print(task1(s, s0))
    else:
        print("Значение строк не должно быть пустым!")
        
    
    print("Задание 2")
    text = input("Введи текст для проверки: \n")
    if text:
        valid = task2(text)
        res = ">" if valid else "<"
        print(f"В данном тексте букв {res} цифр")
    else:
        print("Текст не должен быть пустым!")
    
    print("Задание 3")
    try:
        l = int(input("Введи длину списка: "))
        a = int(input("Введи начало интервала: "))
        b = int(input("Введи конец интервала: "))
        
        if l <= 0:
            print("Длина списка должен быть больше нуля!")
        elif a > b:
            print("Конец интервала должен быть больше его начала!")
        else:
            elems = [randint(-100, 100) for _ in range(l)]
            print(f"Изначальный список: {elems}")
            print(f"Максимальный элемент: {maxx(elems)}")
            print(f"Список после удаления элементов принадлежащих [{a}, {b}]: {task3(elems, a, b)}")
    except:
        print("Ты ввёл не число!")
    
    