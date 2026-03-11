def is_valid(isbn: str) -> bool:
    isbn_clean = isbn.replace("-", "")
    
    if len(isbn_clean) != 10:
        return False
    
    total = 0
    for i in range(10):
        char = isbn_clean[i]
        if i == 9 and char == 'X':
            value = 10
        elif char.isdigit():
            value = int(char)
        else:
            return False
        
        total += value * (10 - i)
    
    return total % 11 == 0