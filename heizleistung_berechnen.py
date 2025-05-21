def eingabe_der_werte():
    breite = float(input("Breite des Raumes (m):"))
    laenge = float(input("Breite des Raumes (m):"))
    hoehe = float(input("Höhe des Raumes (m)?"))
    t_innen = float(input("Innentempertatur (C°):"))
    t_außen = float(input("Außentemperatur (C°):"))

    volumen = breite * laenge * hoehe
    dt = t_innen - t_außen
    return volumen, dt

def berechne_heizleistung(volumen, dt):
    ergebnis= volumen * dt * 0.024
    return ergebnis

volumen, dt = eingabe_der_werte()


if dt < 0: 
    print(f"Achtung die Temperaturdifferenz ist kleiner als {dt}°C")

heizleistung = berechne_heizleistung(volumen, dt)
print(f"benötigte Heizleistung beträgt {heizleistung}kw")
    
