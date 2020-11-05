from .day import Day
from .term import Term

class Lesson(object):
    def __init__(self, term, name, teacherName, year):
        self.term = term
        self.name = name
        self.teacherName = teacherName
        self.year = year
        self.full_time = False
        if self.term._Term__day.value <= 4:
            if term.hour*60+term.minute+term.duration < 20*60:
                self.full_time = True
            
    def earlierDay(self):
        if True:
            self.term._Term__day = Day(self.term._Term__day.value-1)

    def laterDay(self):
        if True:
            self.term._Term__day = Day(self.term._Term__day.value+1)

    times = {
        True: {
            Day.MON : (8,20),
            Day.TUE : (8,20),
            Day.WED : (8,20),
            Day.THU : (8,20),
            Day.FRI : (8,17),
            Day.SAT : (0,0),
            Day.SUN : (0,0)
        },
        False: {
            Day.MON : (0,0),
            Day.TUE : (0,0),
            Day.WED : (0,0),
            Day.THU : (0,0),
            Day.FRI : (17,20),
            Day.SAT : (8,20),
            Day.SUN : (8,20)
        }
    }
    def earlierTime(self):
        start = self.times[self.full_time][self.term.day][0]*60 + 90
        if self.term.hour*60 + self.term.minute >=  start:
            self.term.hour -= 1
            self.term.minute = (self.term.minute - 30)%60

    def laterTime(self):
        end =  self.times[self.full_time][self.term.day][1]*60 - 90
        if self.term.hour*60 + self.term.minute+self.term.duration <= end:
            self.term.hour += 1
            self.term.minute = (self.term.minute + 30)%60

