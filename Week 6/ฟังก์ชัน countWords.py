def countWords(text):
    word_count = 0
    in_word = False
    i = 0
    
    while i < len(text):
        if text[i] != " ":
            if not in_word:
                word_count += 1
                in_word = True
        else:
            in_word = False 
        i += 1
        
    return word_count

print("countWords('Human and AI can make mistakes') :", countWords("Human and AI can make mistakes"))