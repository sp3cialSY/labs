from math import pi, atan
def num1() -> None:
    x = 2.0
    while x <= 5.0:      
        y = round(x - atan(x) - pi, 1)
        if y == 0:
            return x
        x = round(x + 0.1, 1)
        
def fib(orig_num: int, num: int = 1, prev: int = 0) -> bool:
    if orig_num == num:
        return True
    if num > orig_num:
        return False
    return fib(orig_num, num+prev, num)

def degrees() -> None:
    celsium = 15
    print("Таблица перевода градусов Фаренгейта в Цельсия")
    while celsium <= 30:
        f = round(1.8 * celsium + 32, 1)
        print(f"{celsium} °C = {f} F")
        celsium += 1.5
    


if __name__ == "__main__":
    print("Точка пересечения y = x - arctan(x) - π с осью X: ")
    print(f"Точка с координатами ({num1()}, 0)\n")
    try:
        f = int(input("Является ли числом элементом последовательности Фибоначчи?\nВведи целочисленное число: "))
        if f < 1:
            print("Число должно быть больше 1")
        else:
            is_fib = fib(f)
            valid = 'входит' if is_fib else "не входит"
            print(f"Число {f} {valid} в последовательность Фибоначчи")
    except:
        print("Ты ввёл не число!\n")
    degrees()
        
    