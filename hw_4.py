# 4.Напишите программу, которая по заданному номеру четверти, 
# показывает диапазон возможных координат точек в этой четверти (x и y).

quart = int(input('Введите № четверти от 1 до 4: '))

if (quart == 1):
    print("Диапазон координат Х (0; +∞), У (0; +∞)")
elif (quart == 2):
    print("Диапазон координат Х (-∞; 0), У (0; +∞)")
elif (quart == 3):
    print("Диапазон координат Х (-∞; 0), У (-∞; 0)")
elif (quart == 4):
    print("Диапазон координат Х (0; +∞), У (-∞; 0)")