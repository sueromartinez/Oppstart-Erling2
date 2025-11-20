print("velkommen til prosjekt Erling.\n")

print("---------------------------------------------")

konflikt = ""
print("Det har oppstått en uenighet mellom Silje og Sivert angående teknologi og design valg.")
print("Hva skal du gjøre?\n")
print("A) Du ignorer det, og ser om det løser seg med tiden.\nB) Du har et felles møte med de to og løser problemet.\n")

valg = input("Hva gjør du?")
konflikt = ""
if valg == "A": 
      konflikt = "Høy"
      print("Du ignorerte kranglingen og det har forverret seg.\n")
elif valg == "B":
      konflikt = "Lav"
      print("Møtet virket og problemet løste seg.\n")
else:
    konflikt = "Høy"
    print("ugyldig valg, du velger automatisk valg A.")


print("---------------------------------------------")

Samarbeid = ""
print("Det opptsår en konlfikt mellom Jabir og Hamid angående protypen.")
print("Hva skal du gjøre?\n")
print("A) De lager hver sin prototype og kombinerer dem.\nB) De lager en felles prototype.\n")

valg1 = input("Hva gjør du?\n")
if valg1 == "A": 
      Samarbeid = "Lav"
      print("Samarbeidet i gruppen forverer seg of prsjektet står på spill.\n")
elif valg1 == "B":
      Samarbeid = "Høy"
      print("De lager en felles prototype og Samrbeidet i gruppen forbedrer seg.\n")
else:
    Samarbeid = "Lav"
    print("Ugyldig valg, du velger automatisk valg A.")

print("---------------------------------------------")

Trivsel = ""
print("Hvordan kan Erling bevare Trivselen i teamet.")
print("Hva skal du gjøre?\n")
print("A) Relasjonsbygging i teamet.\nB) Prioritere femdrift i prosjektet")

valg2 = input("Hva gjør du?")
if valg2 == "A": 
      Trivsel = "Høy"
      print("Gruppens trivsel øker og prosjektet går riktig vei.")
elif valg2 == "B":
      Trivsel = "Lav"
      print("fremdriften stagnerer og triveslen i gruppen synker.")
else:
    Trivsel = "Høy"
    print("Ugyldig valg, du velger automatisk valg A.")


print("---------------------------------------------")

print("Resultatet av valgene dine ga følgende resultat:\n")

if Samarbeid == "Høy" and konflikt == "Høy" and Trivsel == "Høy":
      print("Teamet fungerer ok og prosjektet blir levert etter tidsfristen.\n")
elif Samarbeid == "Lav" and konflikt == "Lav" and Trivsel == "Lav":
      print("Teamet jobber dårlig sammen og prosjektet blir ikke levert.\n")
elif Samarbeid == "Høy" and konflikt == "Lav" and Trivsel == "Høy":
      print("Teamet jobber bra og prosjektet blir levert tidsnok.\n")
elif Samarbeid == "Lav" and konflikt == "Høy" and Trivsel == "Lav":
      print("Teamet jobber dårlig sammen og prosjketet blir ikke levert.\n")
elif Samarbeid == "Høy" and konflikt == "Høy" and Trivsel == "Lav":
      print("Teamet fungerer ok og prosjektet blir levert etter tidsfristen.\n")
elif Samarbeid == "Lav" and konflikt == "Lav" and Trivsel == "Høy":
      print("Teamet fungerer ok og prosjektet blir levert etter tidsfristen.\n")
elif Samarbeid == "Lav" and konflikt == "Høy" and Trivsel == "Høy":
      print("Teamet fungerer ok og prosjektet blir levert etter tidsfristen.\n")
elif Samarbeid == "Høy" and konflikt == "Lav" and Trivsel == "Lav":
      print("Teamet fungerer ok og prosjektet blir levert etter tidsfristen.\n")
else:
      print("Noe har gått galt venligst prøv igjen:)")
