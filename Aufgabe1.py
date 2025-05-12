kartenstapel = ["gr7", "gl2", "+4", "bl3"]
while kartenstapel.count != 0 :
    print(kartenstapel)
    kartenstapel.pop(0)
    aktuelleKarte = kartenstapel.pop(0)

    if aktuelleKarte == +4 :
        print("+4 kann gespielt werden.")
        break
print ("Stapel ist leer")