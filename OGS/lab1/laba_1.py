
def var_1(subsequence):
    vowels_lower_ru = 'аеёиоуыэюя'
    vowels_upper_ru = vowels_lower_ru.upper()
    vowels_lower_en = 'aeiouy'
    vowels_upper_en = vowels_lower_en.upper()
    all_vowels = vowels_lower_ru + vowels_upper_ru + vowels_lower_en + vowels_upper_en

    result = '' 
    for symbol in subsequence:
        if symbol not in all_vowels:
            result += symbol
    return result


def var_2(subsequence):
    #Удалили пробелы но не страшно
    result = ''
    for symbol in subsequence:
        if symbol.isalpha():
            result += symbol
    return result


def var_3(subsequence):
    result = ''
    for char in subsequence:
        if not char.isupper():
            result += char
    return result


def var_4(subsequence):
    consonants_lower_ru = 'бвгджзклмнпрстфхцчшщ'
    consonants_upper_ru = consonants_lower_ru.upper()
    consonants_lower_en = 'bcdfghjklmnpqrstvwxyz'
    consonants_upper_en = consonants_lower_en.upper()
    all_consonant = consonants_lower_ru + consonants_upper_ru + consonants_lower_en + consonants_upper_en

    result = '' 
    for symbol in subsequence:
        if symbol not in all_consonant:
            result += symbol
    return result


subsequence = input('Введите подпоследовательность: ')
print(var_4(subsequence))