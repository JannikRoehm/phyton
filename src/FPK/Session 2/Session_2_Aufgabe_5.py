x,y,z = 10,65,4

rechnung=int(input("Errechne schriftlich das Ergebnis von {}+{}-{}?".format(x, y, z)))
print("Meine Antwort lautet:", rechnung)

if rechnung == 71:
    print ("10 von 10!")
elif rechnung != 71:
    print ("Komm schon, so schwer isses net!")
