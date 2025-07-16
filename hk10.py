f = open("hk.txt", "x")
a = open("a.txt" , "x")
b = open("b.txt" , "x")
c = open("c.txt" , "x")
d = open("d.txt" , "x")
sum = 0
sum1 = 0
hk1 = []
hk2 = []
hk3 = []
hk4 = []
for x in range(10):
    f = open("hk.txt", "w")
    hoghogh = int(input("hoghogh ra vared konid ?"))
    hk1.append(hoghogh)
    f.write(str(hk1))
    hkint = int(hoghogh)
    if hkint > 5000000:
        a = open("a.txt" , "w")
        hk2.append(hoghogh)
        a.write(str(hk2))
    if hkint > 8000000:
        kasteh3 = hkint * 3 / 100
        kasteh2 = hkint * 2 / 100
        result1 = hkint - kasteh2 - kasteh3
        b = open("b.txt" , "w")
        hk3.append(result1)
        b.write(str(hk3))
    if hkint < 8000000:
        c = open("c.txt" , "w")
        sum = (sum + hkint)/10
    if hkint < 3000000:
        sum1 = (hkint * 7 / 100) + hkint
        result2 = (hkint * 2.5 / 100) + sum1
        d = open("d.txt" , "w")
        d.write(str(result2))
c.write(str(sum))