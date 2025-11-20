print("Velkommen til prosjekt Erling.\n")
print("---------------------------------------------")

# KONFLIKT
print("Det har oppstått en konflikt mellom Silje og Sivert angående teknologi og designvalg.")
print("Hva skal du gjøre?\n")
print("A) Du ignorerer det, og ser om det ordner seg med tiden.")
print("B) Du har et felles møte med de to og løser problemet.\n")

valg = input("Hva gjør du? ")

if valg.upper() == "A":
    konflikt = "Høy"
    print("Du ignorerte konflitken og det har forverret seg.\n")
elif valg.upper() == "B":
    konflikt = "Lav"
    print("Møtet fungerte og problemet løste seg.\n")
else:
    konflikt = "Høy"
    print("Ugyldig valg, du velger automatisk valg A.\n")

print("---------------------------------------------")

# SAMARBEID
print("Det oppstår en konflikt mellom Jabir og Hamid angående prototypen.")
print("Hva skal du gjøre?\n")
print("A) De lager hver sin prototype og kombinerer dem.")
print("B) De lager en felles prototype.\n")

valg1 = input("Hva gjør du? ")

if valg1.upper() == "A":
    Samarbeid = "Lav"
    print("Samarbeidet i gruppen forverrer seg og prosjektet er i fare.\n")
elif valg1.upper() == "B":
    Samarbeid = "Høy"
    print("De lager en felles prototype og samarbeidet i gruppen forbedrer seg.\n")
else:
    Samarbeid = "Lav"
    print("Ugyldig valg, du velger automatisk valg A.\n")

print("---------------------------------------------")

# TRIVSEL
print("Hvordan kan Erling bevare trivselen i teamet?")
print("Hva skal du gjøre?\n")
print("A) Relasjonsbygging i teamet.")
print("B) Prioritere fremdrift i prosjektet.\n")

valg2 = input("Hva gjør du? ")

if valg2.upper() == "A":
    Trivsel = "Høy"
    print("Gruppens trivsel øker og prosjektet går riktig vei.\n")
elif valg2.upper() == "B":
    Trivsel = "Lav"
    print("Fremdriften stopper opp og trivselen i gruppen synker.\n")
else:
    Trivsel = "Høy"
    print("Ugyldig valg, du velger automatisk valg A.\n")

print("---------------------------------------------")

print("Resultatet av valgene dine ga følgende resultat:\n")

# RESULTATER
if Samarbeid == "Høy" and konflikt == "Høy" and Trivsel == "Høy":
    print("Teamet fungerer bra og prosjektet blir levert innen tidsfristen.\n")

elif Samarbeid == "Lav" and konflikt == "Lav" and Trivsel == "Lav":
    print("Prosjektet har få konflikter, men samtidig dårlig trivsel og samarbeid, noe som fører til et dårlig resultat.\n")

elif Samarbeid == "Høy" and konflikt == "Lav" and Trivsel == "Høy":
    print("Prosjektet går bra og de leverer på tiden.\n")

elif Samarbeid == "Lav" and konflikt == "Høy" and Trivsel == "Lav":
    print("Ingen samarbeider og konfliktene er store i gruppa.\n")

elif Samarbeid == "Høy" and konflikt == "Høy" and Trivsel == "Lav":
    print(".Samarbeidet i Teamet er høyt, men det er også konfliktnivået. Det gjør at triveslen er lav.\n" 
    "Prosjektet blir gjennomført, men kvaliteten blir påvirket av dårlig trivsel.\n")

elif Samarbeid == "Lav" and konflikt == "Lav" and Trivsel == "Høy":
    print("Trivselen i Teamet er bra, men samarbeidet er dårlig.\n"
    "Prosjektet blir levert, men samarbeidet i teamet kunne vært sterkere.\n")

elif Samarbeid == "Lav" and konflikt == "Høy" and Trivsel == "Høy":
    print("Teamet har en god trivsel, men samarbeidet er lav og konflikten er høy.\n" 
    "Prosjektet blir gjennomført på en ustrukturert måte.\n")

elif Samarbeid == "Høy" and konflikt == "Lav" and Trivsel == "Lav":
    print("Teamet samarbeider godt og har god konfliktshåndtering.\n" 
    "Trivselen er lav som leder til dårlig motivasjon i teamet.\n")

else:
    print("Noe har gått galt, vennligst prøv igjen :)\n")
print ("Takk for at du spilte spillet!")
