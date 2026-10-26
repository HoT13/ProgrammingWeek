def is_palindrome(text):
    cleaned_text = ""
    i = 0
    while i < len(text):
        if text[i] != " ":
            cleaned_text += text[i].lower()
        i += 1

    left = 0
    right = len(cleaned_text) - 1
    while left < right:
        if cleaned_text[left] != cleaned_text[right]:
            return False
        left += 1
        right -= 1
        
    return True

print("Deed :", is_palindrome("Deed"))
print("An na :", is_palindrome("An na"))
print("BKKrotorKKB :", is_palindrome("BKKrotorKKB"))
print("25/8/52 :", is_palindrome("25/8/52"))