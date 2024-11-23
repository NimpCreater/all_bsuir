#var = 4? 

def SumDigits(a,c,s):
     digits = list(map(int, str(a)))
     c = len(digits)
     s = sum(digits)
     return c, s


numbers = []
print("Введите пять положительных целых чисел:")
for smth in range(5):
    while True:
        try:
            num = int(input(f"Введите число {smth + 1}: "))
            if num > 0:
                numbers.append(num)
                break
            else:
                print("Число должно быть положительным.")
        except ValueError:
            print("Пожалуйста, введите целое положительное число.")

for num in numbers:
    count, digit_sum = SumDigits(num, 0, 0)
    print(f"Число: {num}, Количество цифр: {count}, Сумма цифр: {digit_sum}")