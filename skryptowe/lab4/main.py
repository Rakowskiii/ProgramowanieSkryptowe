from DeanerySystem.action import Timetable1, Action, Term, Day, Lesson

a = Timetable1()
a.put(Lesson(Term(15, 30, 90, Day.WED), "Ang", "Nauczyciel od Ang", 2020))
a.put(Lesson(Term(8,  00, 90, Day.WED), "Skrypto", "Nauczyciel od Skrypto", 2020))
a.put(Lesson(Term(9,  30, 90, Day.THU), "Matma", "Nauczyciel od Matmy", 2020))
a.put(Lesson(Term(11 ,0,  90, Day.THU), "Matma", "Nauczyciel od Matmy", 2020))
a.put(Lesson(Term(8, 00, 90, Day.FRI), "Zabawa", "Nauczyciel od Zabawy", 2020))
print(a)
a.perform(a.parse(["d+", "t-", "t-", "d-", "t-", "d-", "t-", "t+", "d+", "t-", "t-", "t-", "t-", "d-", "t-", "d-", "t-", "t+", "d+", "t-", "t-"]))
print(a)
