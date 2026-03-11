def capitalize_title(title: str) -> str:
    words = title.split()
    capitalized_words = []
    
    for word in words:
            capitalized_word = word[0].upper() + word[1:].lower()
            capitalized_words.append(capitalized_word)
    
    return ' '.join(capitalized_words)


def check_sentence_ending(sentence: str) -> bool:
    answer = ""
    if sentence[-1] == '.':
        return True
    else:
        return False


def clean_up_spacing(sentence: str) -> str:
    start = 0
    end = len(sentence) - 1
    
    while sentence[start] == ' ':
        start += 1
    while sentence[end] == ' ':
        end -= 1

    return sentence[start:end+1]

def replace_word_choice(sentence: str, old_word: str, new_word: str) -> str:
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