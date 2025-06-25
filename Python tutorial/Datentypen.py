#string (str) -> Zeichenkette, erlaubt kein Weiterrechnen


#Anführungszeichen müssen gesetzt werden!
x = "50"

x = "Hallo Welt"
 #   012345678910       ->Index, kann einzelne Buchstaben der Zeichenkette ausgeben, Zählung fängt bei 0 an, Leerzeichen werden mitgezählt
print(x)         # gibt "Hallo Welt" aus
print(x[1])      # gibt den Buchstaben "a" aus
print(x[6:10])   # gibt den String von Zeichen 6-10 aus (Slicing); -> "Welt"
print(x.upper()) # gibt den string in Großbuchstaben aus -> "HALLO WELT"
print(x.lower()) # gibt den String in kleinbuchstaben aus -> "hallo welt"
print(x.split()) # gibt String in einzelnen Wörtern aus -> "Hallo", "Welt"
print(x.split("e")) # String wird überall, wo ein "e" kommt, aufgeteilt -> "Hallo W", "lt"
print(x.find("Welt")) # gibt den Index an, an der das Wort Welt beginnt -> "6"


y = "Dieser Satz ist sehr lange, wie lange ist er?"
len(y) # Funktion zählt alle verwendeten Zeichen
print ("Der String mit der Variable y ist" ,len(y),"Zeichen lang")






#integer (int) -> Ganzzahl, für Berechnungen geeignet
x = -50 + 50

print (x)     # x = 0










#float (float) -> Gleitkommazahl, für Berechnungen geeignet
x = 50.5

#boolean (bool) -> Wahrheitswert, kann True oder False annehmen
x = True
y = False
