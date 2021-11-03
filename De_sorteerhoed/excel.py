
import openpyxl

path = "Vragen.xlsx"

# Werkblad openen
# Werkblad creëeren
wb_obj = openpyxl.load_workbook(path)

# pakt het goeie sheet
sheet_obj = wb_obj.active
Vragen = int(0)
Antwoord = int(0)
Rij = 2
Kolom = 2
# Er zijn 18 vragen dus vragen kleiner dan 18
while Vragen < 18:
    Rij += 1
    Kolom = 2
    Antwoord = 0
    Vragen += 1
    while Kolom < 7:
        Question = sheet_obj.cell(row=Rij, column=Kolom)

        Antwoord += 1
        Kolom += 1

        print(Question.value)
# wat hierboven gebeurd is dat er gevraagd wordt zoek in Rij  en Kolom dan kom je dus uit bij een specefieke cell deze
# cell is in het eerste geval de vraag en de rest zijn de antwoorden
