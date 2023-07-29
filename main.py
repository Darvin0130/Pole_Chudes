import random as re

list_of_words = ['книга', 'мова', 'сонце', 'дім', 'садок', 'квітка', 'вода', 'душа', 'дірка', 'світло',
                 'літо', 'зима', 'місто', 'вогонь', 'річка', 'музика', 'дівчина', 'хлопець', 'край', 'море',
                 'звір', 'хмара', 'картка', 'пісня', 'рука', 'ключ', 'дерево', 'вітер', 'птиця', 'вікно'
                 ]

def choice_word(word):
    choice = re.choice(word)
    return choice


def number_of_attempts():
    attempts = int(input("Будь ласка введіть кількість спроб за які Ви хочете вгадати слово: "))
    return attempts


def guess_the_word():
    word = choice_word(list_of_words)
    masked_word = "*" * len(word)

    attempts = number_of_attempts()

    while attempts > 0 and "*" in masked_word:
        print(masked_word)
        letter_or_word = input("Введіть букву або слово: ")

        if len(letter_or_word) > 1:
            if letter_or_word == word:
                print("Я Вас вітаю Ви вгадали слово!!!")
                break
            else:
                print("Слово не вірне")
        else:
            if letter_or_word in word:
                updated_masked_word = ""
                for i in range(len(word)):
                    if letter_or_word == word[i]:
                        updated_masked_word += letter_or_word
                    else:
                        updated_masked_word += masked_word[i]
                masked_word = updated_masked_word
            else:
                print("Такої літери немає!!!")

            if letter_or_word not in word:
                attempts -= 1

            if "*" not in masked_word:
                print("Вітаю, ви вгадали слово!")
            elif attempts <= 0:
                print("Ви програли. Спробуйте ще раз!!!")


guess_the_word()
