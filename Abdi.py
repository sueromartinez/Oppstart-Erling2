def hent_valg(sporsmalstekst: str) -> str:
    """Viser et spørsmål, tar inn A/B og bruker A som standard ved ugyldig valg."""
    print(sporsmalstekst)
    valg = input("Hva gjør du? ").strip().upper()

    if valg not in ("A", "B"):
        print("Ugyldig valg, du velger automatisk valg A.\n")
        valg = "A"
    return valg


print("velkommen til prosjekt Erling.\n")
print("---------------------------------------------")

# ------------------ KONFLIKT ------------------
konflikt = ""

spm1 = (
    "Det har oppstått en uenighet mellom Silje og Sivert angående teknologi og designvalg.\n"
    "Hva skal du gjøre?\n\n"
    "A) Du ignorer det, og ser om det løser seg med tiden.\n"
    "B) Du har et felles møte med de to og løser problemet.\n"
)

valg = hent_valg(spm1)

if valg == "A":
    konflikt = "Høy"
    print("Du ignorerte kranglingen og den har forverret seg.\n")
else:  # valg == "B"
    konflikt = "Lav"
    print("Møtet virket og problemet løste seg.\n")

print("---------------------------------------------")

# ------------------ SAMARBEID ------------------
Samarbeid = ""

spm2 = (
    "Det oppstår en konflikt mellom Jabir og Hamid angående prototypen.\n"
    "Hva skal du gjøre?\n\n"
    "A) De lager hver sin prototype og kombinerer dem.\n"
    "B) De lager en felles prototype.\n"
)

valg1 = hent_valg(spm2)

if valg1 == "A":
    Samarbeid = "Lav"
    print("Samarbeidet i gruppen forverrer seg og prosjektet står på spill.\n")
else:  # valg1 == "B"
    Samarbeid = "Høy"
    print("De lager en felles prototype, og samarbeidet i gruppen forbedrer seg.\n")

print("---------------------------------------------")

# ------------------ TRIVSEL ------------------
Trivsel = ""

spm3 = (
    "Hvordan kan Erling bevare trivselen i teamet?\n"
    "Hva skal du gjøre?\n\n"
    "A) Relasjonsbygging i teamet.\n"
    "B) Prioritere fremdrift i prosjektet.\n"
)

valg2 = hent_valg(spm3)

if valg2 == "A":
    Trivsel = "Høy"
    print("Gruppens trivsel øker og prosjektet går riktig vei.\n")
else:  # valg2 == "B"
    Trivsel = "Lav"
    print("Fremdriften stagnerer og trivselen i gruppen synker.\n")

print("---------------------------------------------")
print("Resultatet av valgene dine ga følgende resultat:\n")

# ------------------ RESULTAT ------------------
if Samarbeid == "Høy" and konflikt == "Høy" and Trivsel == "Høy":
    print("Teamet fungerer bra, men konfliktnivået er høyt. Prosjektet blir levert til tiden,\n"
          "men Erling må jobbe aktivt med konfliktløsning fremover.\n")

elif Samarbeid == "Lav" and konflikt == "Lav" and Trivsel == "Lav":
    print("Prosjektet har lite konflikter, men samtidig lite trivsel og samarbeid.\n"
          "Dette fører til et dårlig levert prosjekt.\n")

elif Samarbeid == "Høy" and konflikt == "Lav" and Trivsel == "Høy":
    print("Prosjektet går på skinner, og teamet leverer over forventning.\n")

elif Samarbeid == "Lav" and konflikt == "Høy" and Trivsel == "Lav":
    print("Ingen samarbeider og konfliktene er store i gruppa. Prosjektet er i fare.\n")

elif Samarbeid == "Høy" and konflikt == "Høy" and Trivsel == "Lav":
    print("Teamet samarbeider greit, men konfliktnivået er høyt og trivselen lav.\n"
          "Prosjektet blir levert, men kvaliteten preges av dårlig arbeidsmiljø.\n")

elif Samarbeid == "Lav" and konflikt == "Lav" and Trivsel == "Høy":
    print("Folk trives, men samarbeidet er svakt. Prosjektet blir levert,\n"
          "men kunne vært mye bedre med sterkere teamarbeid.\n")

elif Samarbeid == "Lav" and konflikt == "Høy" and Trivsel == "Høy":
    print("Gruppa trives sosialt, men konflikter og manglende samarbeid gjør\n"
          "at prosjektet blir rotete og ustrukturert.\n")

elif Samarbeid == "Høy" and konflikt == "Lav" and Trivsel == "Lav":
    print("Teamet samarbeider godt og har kontroll på konflikter,\n"
          "men lav trivsel kan på sikt svekke motivasjonen og resultatet.\n")

else:
    print("Noe har gått galt, vennligst prøv igjen :)\n")
print("Takk for at du spilte prosjekt Erling!")