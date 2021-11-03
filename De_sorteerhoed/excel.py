import openpyxl
 
# Locatie Vragen
path = "Vragen.xlsx"
 
# Werkblad openen
# Werkblad creëeren
wb_obj = openpyxl.load_workbook(path)
 
# pakt het goeie sheet
sheet_obj = wb_obj.active

#Start van de Automatische picker
Vragen = int(0)
Antwoord = int (0)
Antwoord = int (0)
#18 vragen dus kleiner dan 18 
while Vragen < 18:
    Rij = 3
    Kolom = 2
    Vragen = Vragen + 1
    Antwoord = Antwoord +1
# er zijn 5 rijen die we gebruiken en dat begint op 2 dus kleiner dan 6 
    while Antwoord < 6:
        Question = sheet_obj.cell(row=Rij, column=Kolom)
        Antwoord = Antwoord +1
        Kolom = Kolom+1
        print(Question.value)


