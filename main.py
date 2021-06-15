import random
import ast
import string
import math

alphabet_lower = ['а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я', ' ']

#language_statistics1 = {' ': 0.175, 'о': 0.089, 'е': 0.072, 'а': 0.062, 'и': 0.062, 'н': 0.053, 'т': 0.053, 'с': 0.045, 'р': 0.040, 'в': 0.038, 'л': 0.035, 'к': 0.028, 'м': 0.026, 'д': 0.025, 'п': 0.023, 'у': 0.021, 'я': 0.018, 'ы': 0.016, 'ь': 0.014, 'г': 0.014, 'з': 0.014, 'б': 0.013, 'ч': 0.012, 'й': 0.010, 'х': 0.009, 'ж': 0.007, 'ш': 0.006, 'ю': 0.006, 'ц': 0.004, 'щ': 0.003, 'э': 0.003, 'ф': 0.002, 'ъ': 0.001}
language_statistics1 = {' ': 0.175, 'о': 0.089, 'е': 0.072, 'а': 0.062, 'Т': 0.062, 'И': 0.053, 'Р': 0.053, 'с': 0.045, 'Н': 0.040, 'в': 0.038, 'Д': 0.035, 'Л': 0.028, 'П': 0.026, 'К': 0.025, 'М': 0.023, 'у': 0.021, 'Ы': 0.018, 'Б': 0.016, 'Ч': 0.014, 'Х': 0.014, 'Я': 0.014, 'Й': 0.013, 'Г': 0.012, 'Ж': 0.010, 'Ь': 0.009, 'Ю': 0.007, 'З': 0.006, 'Щ': 0.006, 'Ш': 0.004, 'Ф': 0.003, 'Ц': 0.003, 'Э': 0.002, 'ъ': 0.001}

language_statistics_double_word = {'н':10, 'e':9, 'с':8, 'и':7}


def key_check(key_:dict):
    for k,v in key_.items():
        if v == k:
            key_alphabet = random.sample(alphabet_lower, len(alphabet_lower))
            key = {alphabet_lower[i]: key_alphabet[i] for i in range(len(alphabet_lower))}
            key_check(key)
        else:
            return key_

def key_generaion():

    key_alphabet = random.sample(alphabet_lower, len(alphabet_lower))
    key = {alphabet_lower[i]:key_alphabet[i] for i in range(len(alphabet_lower))}

    key = key_check(key)

    with open('D:\\У(ч)еба\\Шифр сдвига\\key.txt', mode='w', encoding='utf-8') as key_file:
        key_file.write(str(key))

def encrypt():

    with open('D:\\У(ч)еба\\Шифр сдвига\\key.txt', mode='r', encoding='utf-8') as key_file:
        key_str = key_file.read().lower()

    with open('D:\\У(ч)еба\\Шифр сдвига\\text.txt', mode='r', encoding='utf-8') as open_text:
        text = open_text.read().lower()

    text = text.replace('ё','е')

    key_dict = dict(ast.literal_eval(key_str))

    encrypt_text = ''

    for i in range(len(text)):
        if text[i] in key_dict.keys():
            encrypt_text += key_dict[text[i]]
        else:
            encrypt_text += text[i]


    with open('D:\\У(ч)еба\\Шифр сдвига\\encrypt_text.txt', mode='w', encoding='utf-8') as encrypt_file:
        encrypt_file.write(encrypt_text)

def decrypt():

    with open('D:\\У(ч)еба\\Шифр сдвига\\key.txt', mode='r', encoding='utf-8') as key_file:
        key_str = key_file.read().lower()

    with open('D:\\У(ч)еба\\Шифр сдвига\\encrypt_text.txt', mode='r', encoding='utf-8') as encrypt_file:
        encrypt_text = encrypt_file.read().lower()

    key_dict = dict(ast.literal_eval(key_str))
    key_dict_for_decr = dict((v,k) for k,v in key_dict.items())

    decrypt_text = ''

    for i in range(len(encrypt_text)):
        if encrypt_text[i] in key_dict.keys():
            decrypt_text += key_dict_for_decr[encrypt_text[i]]
        else:
            decrypt_text += encrypt_text[i]

    with open('D:\\У(ч)еба\\Шифр сдвига\\decrypt_text.txt', mode='w', encoding='utf-8') as decrypt_file:
        decrypt_file.write(decrypt_text)

def frequency_analysis():

    with open('D:\\У(ч)еба\\Шифр сдвига\\Лаб_1_Шифрограммы\\Вариант6.txt', mode='r') as encrypt_file:
        encrypt_text = encrypt_file.read().lower()

    spec_chars = string.punctuation + '\n\xa0«»\t—…' + string.digits
    encrypt_text = "".join([ch for ch in encrypt_text if ch not in spec_chars])

    frequency = {}
    frequency_double_letter = {}

    for i in range(len(encrypt_text)):
        if i+1 != len(encrypt_text):
            if encrypt_text[i] == encrypt_text[i+1]:
                if encrypt_text[i] in frequency_double_letter:
                    frequency_double_letter[encrypt_text[i]] = frequency_double_letter[encrypt_text[i]] + 1
                else:
                    frequency_double_letter[encrypt_text[i]] = 1
            else:
                if encrypt_text[i] in frequency:
                    frequency[encrypt_text[i]] = frequency[encrypt_text[i]] + 1
                else:
                    frequency[encrypt_text[i]] = 1

    frequency = {k: v for k, v in sorted(frequency.items(), reverse=True, key=lambda item: item[1])}  #сортировка по значению, если item[0], то по ключу
    frequency_double_letter = {k: v for k, v in sorted(frequency_double_letter.items(), reverse=True, key=lambda item: item[1])}  #сортировка по значению, если item[0], то по ключу

    for i in frequency:
        frequency[i] = frequency[i]/len(encrypt_text)

    entr = 0

    for v in frequency.values():
        entr += (-v) * math.log2(v)

    print(entr)

    with open('D:\\У(ч)еба\\Шифр сдвига\\frequency.txt', mode='w', encoding='utf-8') as frequency_file:
        frequency_file.write(str(frequency))

    with open('D:\\У(ч)еба\\Шифр сдвига\\frequency_double_letter.txt', mode='w', encoding='utf-8') as frequency_file:
        frequency_file.write(str(frequency_double_letter))

def lang_stat_key (letter_statistic, text, double_word):

    with open('D:\\У(ч)еба\\Шифр сдвига\\frequency.txt', mode='r', encoding='utf-8') as key_file:
        frequency = key_file.read()

    frequency = dict(ast.literal_eval(frequency))

    with open('D:\\У(ч)еба\\Шифр сдвига\\frequency_double_letter.txt', mode='r', encoding='utf-8') as key_file:
        frequency_double_letter = key_file.read()

    frequency_double_letter = dict(ast.literal_eval(frequency_double_letter))

    fk = ''
    sk = ''
    dfk = ''
    dsk = ''

    for k in frequency.keys():
        fk += k

    for k, v in letter_statistic.items():
        sk += k

    key_ = {fk[i]: sk[i] for i in range(len(fk))}

    if double_word == True: # флаг на использование биграмм
        key_double_word = {dfk[i]: dsk[i] for i in range(len(dsk))}

        for k in frequency_double_letter.keys():
            dfk += k

        for k in language_statistics_double_word.keys():
            dsk += k

        for k,v in key_.items():
            for dk, dv in key_double_word.items():
                if k == dk:
                    v = dv


    with open('D:\\У(ч)еба\\Шифр сдвига\\key_.txt', mode='w', encoding='utf-8') as key_file:
        key_file.write(str(key_))

    decrypt_text = ''

    for i in range(len(text)):
        if text[i] in key_.keys():
            decrypt_text += key_[text[i]]
        else:
            decrypt_text += text[i]

    return decrypt_text

def frequency_decrypt():

    with open('D:\\У(ч)еба\\Шифр сдвига\\Лаб_1_Шифрограммы\\Вариант6.txt', mode='r') as encrypt_file:
        encrypt_text = encrypt_file.read().lower()

    decrypt_text1 = lang_stat_key(language_statistics1, encrypt_text, False).lower()

    with open('D:\\У(ч)еба\\Шифр сдвига\\frequency_decrypt_text1.txt', mode='w', encoding='utf-8') as decrypt_file:
        decrypt_file.write(decrypt_text1)

if __name__ == '__main__':
    key_generaion()
    encrypt()
    decrypt()
    frequency_analysis()
    frequency_decrypt()
