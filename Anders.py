#Erling har kommet videre i prosjektet, men det har opstått noen bagateller:

print("Velkommen til denne simulasjonen av konflikthåndteringen i prosjektet")

#Konflikt 1
Konflikt = ""
print("\nDet har oppstått en konflikt mellom Silje og Sivert. De er uenige om design og teknologivalg, og det har utviklet seg fra en sakskonflikt til en personkonflikt. Silje mener løsningen som Sivert foreslo vil låse brukeropplevelsen og hindre innovasjon. Sivert mener at Siljes forslag er urealistisk og kostbart.")
print("\nHva gjør du?")
print("\n(A)Du ignorerer dem og lar de fikse opp i problemet selv.")
print("\n(B)Du arrangeret et møte og dere løser opp i problemet sammen")

valg = input("\nHva gjør du?")

if valg =="A":
    Konflikt = "Høy"
    print("\nDe klarte ikke løse problemet selv og situasjonen forverret seg")
elif valg =="B":
    Konflikt ="Lav"
    print("\nMøtet mellom partene virket, konflikten løste seg og stemningen er god")

#Konflikt 2
Samarbeid = ""

print ("Det har oppstått en konflikt mellom Jabir og Hamdi. De er uenige om hvordan innbyggerne skal kunne delta i digitale folkemøter. Hamdi ønsker en kontrollert løsning gjennom kommunens eksisterende plattform. Jabir ønsker et mer åpent, dialogbasert system med rom for spontane innspill. Uenigheten er foreløpig behersket, men Erling merker at frustrasjonen vokser.")
print ("\nHva gjør du?")
print ("\n(A)De lager hver sin prototype og samarbeider, og senere kombinerer dem.")
print ("\n(B)De samarbeider og de lager prototypen sammen")

valg1 = input("\nHva gjør du?")
if valg1 =="A":
    Samarbeid = "Lav"
    print("De lager hver sin prototype og situasjonen og samarbeidet i gruppen forverrer seg")
elif valg1 =="B":
    Samarbeid = "Høy"
    print("De samarbeider og lager en felles prototype, og samarbeidet og stemningen i gruppen bedrer seg")

print("-------------------------------")
#Konflikt 3
Motivasjon = ""

print("Hvordan kan Erling forbedre motivasjonen og trivselen innad i gruppen?")
print("\nHva gjør du?")
print("\n(A)Du prioriterer teambuilding fremfor fremdrift. \n(B)Du prioriterer fremdrift ovenfor motivasjon i gruppen")

valg2 = input("\nHva gjør du?")
if valg2 == "A":
    Motivasjon = "Høy"
    print("\nMotivasjonen i gruppen øker, deltakerne trives og prosjektet går veldig bra.")
elif valg2 == "B":
    Motivasjon = "Lav"
    print("\nMotivasjonen, og dermed trivselen, reduseres og prosjektet går bra i en liten periode før det stagnerer helt")

print("\n-------------------------")

print ("\nBasert på valgene dine, ble stemningen i gruppen slik:")

if Samarbeid == "Høy" and Konflikt == "Lav" and Motivasjon == "Høy":
    print("\nMotivasjonen og samarbeidet i gruppen er svært høy, konfliktene er håndtert/lave og prosjektet går som smurt.")
elif Samarbeid == "Lav" and Konflikt == "Høy" and Motivasjon == "Lav":
    print ("\nSamarbeidet og motivasjonen er lav/dårlig, og dermed konfliktene spirer og prosjektet går dårlig.")
elif Samarbeid == "Høy" and Konflikt == "Lav" and Motivasjon == "Lav":
    print("Samarbeidet er bra, konfliktene er ikke-eksisterende, men motivasjonen er på bunnen. Prosjektet blir dermed ferdig, men det gikk veldig sakte.")
else:
    print("Noe gikk galt, prøv simulasjonen igjen.")

print("\nTakk for at du spilte")