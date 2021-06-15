with open('D:\\У(ч)еба\\Шифр сдвига\\encrypt_text.txt', mode='r', encoding='utf-8') as encrypt_file:
    encrypt_text = encrypt_file.read().lower()

alphabet_lower = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с',
                  'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я', ' ']

count = 0
for item in alphabet_lower:
    for i in range(len(encrypt_text)):
        if item == encrypt_text[i]:
            count += 1

frequency = {item: count / len(encrypt_text) for item in alphabet_lower}



with open('D:\\У(ч)еба\\Шифр сдвига\\frequency.txt', mode='w', encoding='utf-8') as frequency_file:
    frequency_file.write(str(frequency))