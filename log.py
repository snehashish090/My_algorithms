listw = ["hello", "hi", "hey", "super", "snehashish", "yaju", "yes"]
emlis = []
word = input()

for i in listw:
    if word in i:
        emlis.append(i)

print(emlis)