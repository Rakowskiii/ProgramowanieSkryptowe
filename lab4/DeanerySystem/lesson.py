from .day import Day
from .term import Term

class Lesson(object):
    def __init__(self, term, name, teacherName, year):
        self.term = term
        self.name = name
        self.teacherName = teacherName
        self.year = year
        if term._Term__day.value < 4:
            if term.hour*60+term.minute+term.duration < 20*60:
                self.full_time = True
            
    def earlierDay(self):
        if True:
            self.term._Term__day = Day(self.term._Term__day.value-1)

    def laterDay(self):
        if True:
            self.term._Term__day = Day(self.term._Term__day.value+1)

    def earlierTime(self):
        self.term.hour-=self.term.duration//60
        t = self.term.duration%60
        if self.term.minute >= t:
           self.term.minute -= t
        else:
            self.term.hour -= 1
            self.term.minute -= (t-60)

    def laterTime(self):
        self.term.hour += self.term.duration//60
        t = self.term.hour%60
        self.term.hour += t
        if self.term.hour > 60:
            self.term.hour -= 1
            self.term.minute -= 60

