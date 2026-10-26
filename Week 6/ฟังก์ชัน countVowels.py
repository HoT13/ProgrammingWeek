def countVowels(text):
    vowels = "aeiouAEIOU"
    total_vowels = 0
    i = 0
    
    while i < len(vowels):
        total_vowels += countChar(vowels[i], text)
        i += 1
        
    return total_vowels

print("countVowels('Bangkok') :", countVowels("Bangkok"))