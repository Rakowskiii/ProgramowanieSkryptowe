import unittest
from DeanerySystem.action import Timetable1, Action, Term
class TestDeanerySystem(unittest.TestCase):
    def test_parse(self):
        a = Timetable1()
        self.assertEqual(a.parse(["d+","d-","t+","t-"]), [Action.DAY_LATER, Action.DAY_EARLIER, Action.TIME_LATER, Action.TIME_EARLIER])

if __name__== "__main__":
    unittest.main()



#Utwórz konstruktor Lesson(Timetable1 timetable, Term term, String name, string teacherName, int year), który przypisuje swoje argumenty do odpowiednich pól 
#???????