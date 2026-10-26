def search_left(text, char):
    i = 0
    while i < len(text):
        if text[i] == char:
            return i
        i += 1
    return -1

print("ค้นหา 'o' จากซ้ายสุด:", search_left("motor", "o"))

# def find_last_char(text, char):
#     index = len(text) -1
#     while index >= 0:
#         if text[index].lower() == char.lower():
#             return index
#         index -= 1
#     return -1

# print(" a b test")
# sample_text = "Thailand"
# target = "a"
# print(f"ข้อความ: '{sample_text}', หาตัว: '{target}'")
# print(f"ค้นหาจากซ้าย (First Index): {find_first_char(sample_text, target)}")
# print(f"ค้นหาจากขวา (Last Index): {find_last_char(sample_text, target)}")





# #ฟังก์ชัน countChar
# def countChar(target_char, text):
#     count = 0
#     for char in text.lower():
#         if char == target_char.lower():
#             count += 1
#     return count
# print(countChar("a", "aaaa"))





# #ฟังก์ชัน countVowels (เรียกใช้ countChar)
# def countVowels(text):
#     vowels = ['a', 'e', 'i', 'o', 'u']
#     total_vowels = 0
#     for v in vowels:
#         total_vowels += countChar(v, text)
#     return total_vowels
# print(countVowels("Bangkok"))



# #ฟังก์ชัน countWords
# def countWords(text):
#     words = text.split()
#     return len(words)

# print(countWords("Only AI can make mistakes lol"))