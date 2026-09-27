import math
def NumDiagram():

    def rounding(x):
        return math.floor(x + 0.5)

    with open('sequence.txt') as f:
        sequence = f.read()
    parted = sequence.split()
    numbers = [float(x) for x in parted]
    modules = [abs(x) for x in numbers]
    first = modules[125:] ## Первые 125 чисел
    second = modules[:125] ## Вторые 125 чисел
    firstMid = sum(first)/125 ## среднее из первых 125
    secondMid = sum(second)/125 ## среднее из вторых 125
    hundredPercent = firstMid + secondMid ## 100 процентов
    firstPercentage = firstMid / (hundredPercent * 0.01) ##процент первого числа
    secondPercentage = secondMid / (hundredPercent * 0.01) ##процент второго числа
    firstLen = rounding(firstPercentage) ## Длина первой полосы
    secondLen = rounding(secondPercentage) ## Длина Второй полосы
    print(f"\033[48;2;255;0;0m{' ' * firstLen}\033[0m")
    print(f"\033[48;2;0;0;255m{' ' * secondLen}\033[0m")




