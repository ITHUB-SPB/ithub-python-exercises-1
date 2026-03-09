"""
Напишите вспомогательные функции для редактуры статей:

1. Все слова в названии статьи должны быть написаны с заглавных букв.
2. Каждое предложение должно завершаться точкой.
3. Лишние пробельные символы в начале и конце предложения должны быть удалены
4. Уметь заменять слова синонимами.
"""


def capitalize_title(title: str) -> str:
    """Форматирует название статьи.

    Форматирует строку, чтобы каждое слово начиналось с заглавной буквы.

    >>> capitalize_title("my hobbies")
    "My Hobbies"

    :param title: str - исходное название статьи для обработки.
    :return: str - форматированное название, каждое слово с заглавной буквы.
    """
    words = title.split()
    capitalized_words = []
    
    for word in words:
            capitalized_word = word[0].upper() + word[1:].lower()
            capitalized_words.append(capitalized_word)
    
    return ' '.join(capitalized_words)


def check_sentence_ending(sentence: str) -> bool:
    """Проверяет, завершается ли предложение точкой.

    >>> check_sentence_ending("I like to hike, bake, and read.")
    True

    :param sentence: str - одно предложение на проверку.
    :return: bool - True если пунктуация корректная, иначе False.
    """
    answer = ""
    if sentence[-1] == '.':
        return True
    else:
        return False


def clean_up_spacing(sentence: str) -> str:
    """Удаляет пробельные символы с начала и конца предложения.

    >>> clean_up_spacing(" I like to go on hikes with my dog.  ")
    "I like to go on hikes with my dog."

    :param sentence: str - одно исходное предложение.
    :return: str - предложение, очищенное от пробелов в начале и конце.
    """

    start = 0
    end = len(sentence) - 1
    
    while sentence[start] == ' ':
        start += 1
    while sentence[end] == ' ':
        end -= 1

    return sentence[start:end+1]

def replace_word_choice(sentence: str, old_word: str, new_word: str) -> str:
    """Заменяет слова на синонимы.

    >>> replace_word_choice("I bake good cakes.", "good", "amazing")
    "I bake amazing cakes."

    :param sentence: str - одно исходное предложение.
    :param old_word: str - слово, которое мы хотим заменить синонимом.
    :param new_word: str - синоним.
    :return: str - новое, преобразованное предложение.
    """
    words = sentence.split()
    result_words = []
    
    for word in words:
        if word == old_word:
            result_words.append(new_word)
        elif word == old_word + '.':
            result_words.append(new_word + '.')
        else:
            result_words.append(word)
    
    return ' '.join(result_words)