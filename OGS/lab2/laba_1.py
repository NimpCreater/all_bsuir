import tkinter as tk
from tkinter import messagebox

# Функция для быстрого сортирования списка
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    less = [x for x in arr[1:] if x <= pivot]
    greater = [x for x in arr[1:] if x > pivot]
    return quicksort(less) + [pivot] + quicksort(greater)

# Функция для линейного поиска
def linear_search(arr, target):
    for i, num in enumerate(arr):
        if num == target:
            return i
    return -1

# Обработчик кнопки сортировки
def sort_numbers():
    input_numbers = entry_numbers.get()
    # Преобразуем строку в список целых чисел
    try:
        numbers = list(map(int, input_numbers.split(',')))
    except ValueError:
        messagebox.showerror("Ошибка", "Введите правильные целые числа, разделенные запятыми.")
        return

    # Выполняем сортировку с использованием быстрого алгоритма
    sorted_numbers = quicksort(numbers)
    # Отображаем отсортированный список
    result_var.set(f"Отсортированный список: {sorted_numbers}")
    global sorted_list
    sorted_list = sorted_numbers

# Обработчик кнопки поиска
def search_number():
    # Получаем число для поиска
    try:
        target = int(entry_search.get())
    except ValueError:
        messagebox.showerror("Ошибка", "Введите корректное число для поиска.")
        return
    
    # Выполняем линейный поиск
    index = linear_search(sorted_list, target)
    if index != -1:
        messagebox.showinfo("Результат поиска", f"Число найдено на позиции {index}.")
    else:
        messagebox.showinfo("Результат поиска", "Число не найдено в списке.")

# Создание главного окна
root = tk.Tk()
root.title("Программа для сортировки и поиска чисел")

# Создаем элементы интерфейса
label_numbers = tk.Label(root, text="Введите числа (через запятую):")
label_numbers.pack(pady=5)

entry_numbers = tk.Entry(root, width=50)
entry_numbers.pack(pady=5)

button_sort = tk.Button(root, text="Сортировать", command=sort_numbers)
button_sort.pack(pady=5)

result_var = tk.StringVar()
label_result = tk.Label(root, textvariable=result_var)
label_result.pack(pady=5)

label_search = tk.Label(root, text="Введите число для поиска:")
label_search.pack(pady=5)

entry_search = tk.Entry(root, width=50)
entry_search.pack(pady=5)

button_search = tk.Button(root, text="Поиск", command=search_number)
button_search.pack(pady=5)

# Глобальная переменная для хранения отсортированного списка
sorted_list = []

# Запуск основного цикла
root.mainloop()
