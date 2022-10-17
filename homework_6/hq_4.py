''' Напишите программу, 
удаляющую из текста все слова, 
содержащие ""абв"".'''

# Уже былыло решено с помощью filter и lambda

print('введите текст>> ')
text = input()


def end_text(n_text):
    n_text = list(filter(lambda x: 'абв' not in x, n_text.split()))
    return " ".join(n_text)


text = end_text(text)
print(text)
