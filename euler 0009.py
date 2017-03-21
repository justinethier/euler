
# m = 1; n = 2; 2 * m * n ; (m**2) - (n**2) ; (m**2) + (n**2)
#print ("m = " + str(m) + " n = " + str(n))
#print ("a = " + str(a) + " b = " + str(b) + " c = " + str(c))

for m in range(15, 21):
    for n in range(1, 20):
        a = 2 * m * n
        b = (m**2) - (n**2)
        c = (m**2) + (n**2)

        if (a+b+c == 1000):
            print (a*b*c)

