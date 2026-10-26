football = 15
basketball = 20
volleyball = 10

print("จำนวนลูกบอลที่มี:")
print("Football:", football)
print("Basketball:", basketball)
print("Volleyball:", volleyball)
print("-" * 20)

# การเปรียบเทียบพื้นฐาน
if football >= basketball and football >= volleyball:
    print("Football มีจำนวนมากที่สุด")
elif basketball >= football and basketball >= volleyball:
    print("Basketball มีจำนวนมากที่สุด")
else:
    print("Volleyball มีจำนวนมากที่สุด")