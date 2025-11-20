print("Velkommen til kommunens nye portal! Du er Erling og skal gjøre noen valg.\n")

# Beslutning 1

print ("1) Konflikten mellom Silje og Sivert.\n")
print ("Skal han ta det opp i plenum eller individuelt for å skape åpenhet?\n ")

print ("A: Felles samtale; ta det opp i plenum.\n")
print ("B: Individuelle samtaler\n")

valg1 = input("Velg A eller B\n")

# Beslutning 2

print ("2), Konflikten mellom Hamdi og Jabir")
print ("Skal han ta et felles møte mellom dem for å jobbe sammen\n")

print("A: Felles møte.\n")
print ("B: Vente.")

valg2 = input("Velg A eller B\n")

# Beslutning 3

print ("3, Hvordan holde oppe motivasjonen?")

print ("A: Relasjonsbygging")
print ("B: Prioritere fremdrift")

valg3 = input("Velg A eller B\n")

# Sluttutfall

print("\nSLUTT")

# Utfall 1, gode valg

if valg1 == "B" and valg2 == "A" and valg3 == "A":
    print("Teamet viser tillit og går videre til norming-fasen!")

# Utfall 2, mindre gode valg

elif valg3 == "B":
    print("Prosjektet går videre, men forsatt problemer i teamet")


# Utfall 3, dårlige valg

else:
    print("Prosjektet blir forsinket, lite samhold")

print("Takk for at du spilte!")