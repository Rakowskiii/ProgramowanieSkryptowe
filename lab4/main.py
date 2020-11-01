from DeanerySystem.action import Timetable1, Action, Term, Day, Lesson

a = Timetable1()
a.lesson_list.append(Lesson(Term(15, 30, 90,Day.WED),"Ang","Polak",2020))
a.lesson_list.append(Lesson(Term(17,00,90,Day.WED),"Skrypto","Polak",2020))
a.lesson_list.append(Lesson(Term(9,30,90,Day.THU),"Matma","Polak",2020))
a.lesson_list.append(Lesson(Term(11,0,90,Day.THU),"Matma","Polak",2020))
a.lesson_list.append(Lesson(Term(12,30,90,Day.THU),"Lesson","Polak",2020))
a.lesson_list.append(Lesson(Term(14,00,90,Day.THU),"Qwerty","Polak",2020))
a.lesson_list.append(Lesson(Term(15,30,90,Day.FRI),"Zabawa","Polak",2020))
a.lesson_list.append(Lesson(Term(17,0,90,Day.FRI),"Patriota","Polak",2020))
print(a)
t1 = Term(14,0,90,Day.SUN)
print(a.can_be_transferred_to(t1, True))