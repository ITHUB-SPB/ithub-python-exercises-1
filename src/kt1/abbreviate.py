def abbreviate(phrase: str) -> str:
    CorrectPhrase = phrase.replace('-', ' ').replace('_', ' ')
    
    result = ""
    for char in CorrectPhrase:
        if ('a' <= char <= 'z') or ('A' <= char <= 'Z') or char == ' ':
            result += char
    

    words = result.split()
    abbreviation = ""
    for word in words:
        if word:
            abbreviation += word[0].upper()
    
    return abbreviation