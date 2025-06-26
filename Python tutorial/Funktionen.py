
def begruessung():                              #Funktion mit dem Name "begruessung"
    print("Hallo, schön dass du hier bist!")    # definiert, dass die Funktion "Hallo, schön dass du hier bist!" ausgeben soll"
begruessung()                                   #Befehl zum ausführen der Funktion "begruessung"




def begruessung(name):                                       # name ist her der Parameter, welcher in der Funktion verwendet wird, und defniert werden kann
    return f"Hallo {name}, schön dass du hier bist!"         # wird von der Funktion wieder zurückgegeben, rturn f heißt, dass die Funktion übergeben wird, und nicht nur das Ergebnis der Funktion 

print(begruessung("Lena"))                                   #Lena ist hier das Argument, welches der Funktion übergeben wird, funktion wird ausgeführt; anschließend Ausgabe auf Konsole




def addieren(a, b):                     # funktion mit dem Name "addieren", welche die Variablen a und b verwenden soll
    return a + b                        # gibt das Ergebnis der Addition von a und b zurück

summe = addieren(a=20, b=5)             # definiert, dass die Variable "Summe" der beiden nun definierten Variablen a und b, das Ergebnis der Funktion "addieren" sein soll
print(summe)                            # gibt die Variable "Summe", also das Ergebnis der Funktion "addieren" mit a=20 und b=5 auf der Konsole aus
