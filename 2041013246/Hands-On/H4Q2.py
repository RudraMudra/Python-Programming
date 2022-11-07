counter = 0
for i in range(100, 1000, 5):
    if i % 5 == 0 and i % 6 == 0:
        print(i, end=' ')
        counter += 1
        if counter == 10:
            print()
            counter = 0
