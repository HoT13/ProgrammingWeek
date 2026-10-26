def countChar(char, text):
    count = 0
    i = 0
    while i < len(text):
        if text[i] == char:
            count += 1
        i += 1
    return count

print("countChar('a', 'Thailand') :", countChar("a", "Thailand"))