
print("Prosjekt Erling 2.")
print("Du skal være prosjektleder,du skal ta tre viktige valg.")

#Du har 3 konflikter og 2 løsninger til hver konflikt
#Finn best utfall

#konflikt 1: Silje og Sivert

print("1 . Sivert og silje er uenig om design og teknologi")
print("Valg A : Skal han ta et felles møte med dem der,de for jobba sammen")
print("Valg B : Ta det opp i plenum, øker rom for åpenhet")
Choice1 = input("Hva skal du velge, enten (A/B):")

if Choice1 != "A" and Choice1 != "B":
    print("Ugyldig valg. Velg automtatisk A.")
    Choice1 = "A"
elif Choice1 == "B":
   print("Du har valgt B.")
else:
    print("Du har valgt A.")
   

#Konflikt 2:  Jabir og Hamdi
print("2 . Jabir og Hamdi er uenig om design av protype.")
print("Valg A :Jobbe delvis individuelt.")
print("Valg B : Avvente og gi ansvaret til partene.")
Choice2 = input("Hva skal du velge, enten (A/B):")

if Choice2 != "A" and Choice2 !="B":
    print("Ugyldig valg. Velg automatisk A.")
    Choice2 = "A"
elif Choice2 == "B":
   print("Du har valgt B.")
else:
    print("Du har valgt A.")
  

#Konflikt 3: Team trivsel
print("3. Hvordan vil du priotiere teamets trivsel.")
print("Valg A :Relasjonsbygging.")
print("Valg B : Prioritere fremdrift")
Choice3 = input("Hva skal du velge, enten (A/B):")

if Choice3 != "A" and Choice3 != "B":
 print("Ugyldig valg. Velg automatisk A.")
 Choice3 = "A"
elif Choice3 == "B":
   print("Du har valgt B.")
else:
 print("Du har valgt A.")
 
 
# Sluttresultat 
 print("Resultatene av valgene dine:")

 if Choice1 == "A" and Choice2 == "A" and Choice3 == "A":
    print("Teamtes trivsel funker fint, konflikten er dermed løst og trivsel er høy!")
 elif Choice1 == "B" and Choice2 == "B" and Choice3 == "B":
    print("Teamet har økte problemer, konflikt og trivsel er nå lav!")
 else: 
    print("Teamet har fått blandet resultater. Noe funker, andre konflikter må videre følges opp.")

print("Takk for at du har prøvd å ledet team gjennom disse konfliktene.")
