k = ''
with open(r'Test1.txt','r') as f:
    for text in f:
        if text != '\n':
            k+=text
    print(k)
