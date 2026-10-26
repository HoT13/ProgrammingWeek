def search_left(text, char):
    i = 0
    while i < len(text):
        if text[i] == char:
            return i
        i += 1
    return -1

print("ค้นหา 'o' จากซ้ายสุด:", search_left("motor", "o"))
