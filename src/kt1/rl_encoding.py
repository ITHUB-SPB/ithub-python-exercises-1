def decode(encoded_string: str) -> str:
    result = ""
    i = 0
    while i < len(encoded_string):
        num = ""
        while i < len(encoded_string) and encoded_string[i].isdigit():
            num += encoded_string[i]
            i += 1
        if num:
            result += encoded_string[i] * int(num)
        else:
            result += encoded_string[i]
        i += 1
    return result


def encode(initial_string: str) -> str:
    if not initial_string:
        return ""
    
    result = ""
    count = 1
    for i in range(1, len(initial_string)):
        if initial_string[i] == initial_string[i - 1]:
            count += 1
        else:
            if count > 1:
                result += str(count)
            result += initial_string[i - 1]
            count = 1
    if count > 1:
        result += str(count)
    result += initial_string[-1]
    return result