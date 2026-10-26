def search_right(text, char):
    i = len(text) - 1
    while i >= 0:
        if text[i] == char:
            return i
        i -= 1
    return -1

print("ค้นหา 'o' จากขวาสุด:", search_right("BKKrotorKKB", "o"))