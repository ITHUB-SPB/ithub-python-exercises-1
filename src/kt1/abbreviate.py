import re

def abbreviate(phrase: str) -> str:
    """
    Преобразует фразу в аббревиатуру.
    
    Правила преобразования:
    1. Все буквы приводятся к верхнему регистру.
    2. Дефисы внутри слов становятся разделителями.
    3. Другие знаки препинания игнорируются.
    """
    cleaned_phrase = re.sub(r'[^A-Za-z0-9\s\-]', '', phrase).upper()            #удаляем пункт и после в верх регистр
    
    words = re.findall(r'[A-Z]+', cleaned_phrase)
    
    abbreviation = ''.join(word[0] for word in words if word.strip())         #формир из 1ых букв
    
    return abbreviation