from random import randint
arithmoi = [[0 for x in range(100)] for z in range(5)]
for i in range(0, 100):
    for j in range(0, 5):
        a = int(input("Dose arithmo metaksi 0-80  "))
        while True:
            if 0 <= a <= 80:
                x = 0
                while x <= 5:
                    if a != arithmoi[i][x]:
                        arithmoi[i][j] = a
                        x = x+1
                        break
                    else:
                        print("Dose allo arithmo")
                        break
            break
sinolo = 0
for arithmos_paixnidion in range(0, 1000):
    arithmos_paixnidion = 0
    c = []
    while True:
        tim = randint(0, 80)
        b = False
        for z in range(0, len(c)):
            if c[z] == tim:
                b = True
        if b:
            print("O arithmos " + tim + " vgike")
        else:
            c.append(tim)
            arithmos_paixnidion += 1
        sosto = [0 in range(100)]
        for i in range(0, 100):
            for j in range(0, 5):
                if tim == arithmoi[i][j]:
                    sosto[i] += 1
        for i in range(0, 100):
            if sosto[i] == 5:
                print("WIN")
                sinolo += arithmos_paixnidion
                break
mo = sinolo/1000
print("O mesos oros ton arithmon:" + mo)
