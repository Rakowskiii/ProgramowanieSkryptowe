from DeanerySystem.day import Day
from DeanerySystem.term import Term


term1 = Term(8, 30)
term2 = Term(9, 45, 30)
term3 = Term(9, 45, 90)
print(term3.earlierThan(term2))
print(term1)                             # Ma się wypisać: "8:30 [90]"
print(term2)                             # Ma się wypisać: "9:45 [30]"
print(term3)                             # Ma się wypisać: "9:45 [90]"
print("term1 < term2:", term1 < term2)   # Ma się wypisać True
print("term1 <= term2:", term1 <= term2) # Ma się wypisać True
print("term1 > term2:", term1 > term2)   # Ma się wypisać False
print("term1 >= term2:", term1 >= term2) # Ma się wypisać False
print("term2 == term2:", term2 == term2) # Ma się wypisać True
print("term2 == term3:", term2 == term3) # Ma się wypisać False
term4 = term3 - term1                    # Tworzy termin, którego:
                                         # - godzina rozpoczęcia jest taka jak 'term1',
                                         # - czas trwania to różnica minut pomiędzy godziną zakończenia 'term3' (11:15), a godziną rozpoczęcia 'term1' (8:30)
print(term4)                