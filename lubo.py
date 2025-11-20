print("velkommen til prosjekt Erling.\n")


print("---------------------------------------------")


konflikt = ""
print("Det har blitt en uenighet i gruppa mellom Silje og Sivert om teknologi og design valg.")
print("Hva gjør du?\n")
print("A) Du ignorer det, og ser om det løser seg med tiden.\nB) Du har et felles møte med de to og løser problemet.\n")


valg = input("Hva gjør du?")

konflikt = ""

if valg == "A":
    konflikt = "Høy"
    print("Du ignorerte problemet og det blir bare verre.\n")
elif valg == "B":
    konflikt = "Lav"
    print("Møtet virket og problemet er løst.\n")

else:
    konflikt = "Høy"
    print("ugyldig valg, du velger automatisk valg A.")


print("---------------------------------------------")


Samarbeid = ""
print("Det har skjedd en ny konlifkt mellom Jabir og Hamdi angående prototypen.")
print("Hva velger du?\n")
print("A) De lager hver sin prototype og kombinerer dem.\nB) De lager en felles prototype.\n")

valg1 = input("Hva gjør du?\n") 

if valg1 == "A":
    Samarbeid = "Lav"
    print("Samarbeidet i gruppen faller og problemet utvikler seg bare for verre.\n")
elif valg1 == "B":
    Samarbeid = "Høy"
    print("De lager en felles prototype og problemet fikser seg.\n")
else:
    Samarbeid = "Lav"
    print("Ugyldig valg, du velger automatisk valg A.")


print("---------------------------------------------")


Trivsel = ""
print("Hvordan kan Erling holde på trivselen i teamet?.")
print("Hva skal du gjøre?\n")
print("A) Relasjonsbygging i teamet.\nB) Prioritere femdrift i prosjektet")

valg2 = input("Hva gjør du?")

if valg2 == "A":
    Trivsel = "Høy"
    print("Gruppens trivsel øker og prosjektet blir bedre.")

elif valg2 == "B":
    Trivsel = "Lav"
    print("fremdriften går ned og prosjektet blir dårligere.")

else:
    Trivsel = "Høy"
    print("Ugyldig valg, du velger automatisk valg A.")


print("---------------------------------------------")

print("Resultatet av valgene dine ga følgende resultat.\n")


if Samarbeid == "Høy" and konflikt == "Høy" and Trivsel == "Høy":
    print("Teamet fungerer bra og prosjektet blir levert til tiden.\n")
elif Samarbeid == "Lav" and konflikt == "Lav" and Trivsel == "Lav":
    print("Prosjekter har lite konflikter, men samtidig lite trivsel og samarbeid, noe som fører til et dårlig levert prosjekt\n")
elif Samarbeid == "Høy" and konflikt == "Lav" and Trivsel == "Høy":
    print("Prosjekter går på skinner og de leverer over forventning.\n")
elif Samarbeid == "Lav" and konflikt == "Høy" and Trivsel == "Lav":
    print("Ingen samarbeider og konfliktene er store i gruppa.\n")
elif Samarbeid == "Høy" and konflikt == "Høy" and Trivsel == "Lav":
    print("fyll noe.\n")
elif Samarbeid == "Lav" and konflikt == "Lav" and Trivsel == "Høy":
    print("fyll inn.\n")
elif Samarbeid == "Lav" and konflikt == "Høy" and Trivsel == "Høy":
    print("fyll inn.\n")
elif Samarbeid == "Høy" and konflikt == "Lav" and Trivsel == "Lav":
    print("fyll inn.\n")
else:
    print("Her var du dumm, prøv på nytt:)") 