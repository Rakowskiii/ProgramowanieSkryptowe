from typing import List
from .term import Term
from .day import Day
from .lesson import Lesson
from enum import Enum


class Action(Enum):
    DAY_EARLIER = 0
    DAY_LATER = 1
    TIME_EARLIER = 2
    TIME_LATER = 3


class Timetable1(object):
    """ Class containing a set of operations to manage the timetable """
    lesson_list =  list()
    ll = {
            Day.MON : ['']*8,
            Day.TUE : ['']*8,
            Day.WED : ['']*8,
            Day.THU : ['']*8,
            Day.FRI : ['']*8,
            Day.SAT : ['']*8,
            Day.SUN : ['']*8
    }
    time_conv = {
            8 : 0,
            9 : 1,
            11 : 2,
            12 : 3,
            14 : 4,
            15 : 5,
            17 : 6,
            18 : 7
        }
    
    full_time = {
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
    def fix(self):
        self.ll = {
            Day.MON : ['']*8,
            Day.TUE : ['']*8,
            Day.WED : ['']*8,
            Day.THU : ['']*8,
            Day.FRI : ['']*8,
            Day.SAT : ['']*8,
            Day.SUN : ['']*8
        }
        for l in self.lesson_list:
            self.ll[l.term.day][self.time_conv[l.term.hour]] = l.name
        
    def __init__(self):
        self.fix()
        

    def __str__(self):
        self.fix()
        out = ""
        out += "*Poniedziałek*Wtorek      *Środa       *Czwartek    *Piątek      *Sobota      *Niedziela\n"
        out += "********************************************************************************************"
        for i in range(0,8):
            out += f"\n*{self.ll[Day(0)][i]: <12}*{self.ll[Day(1)][i]: <12}*{self.ll[Day(2)][i]: <12}*{self.ll[Day(3)][i]: <12}*{self.ll[Day(4)][i]: <12}*{self.ll[Day(5)][i]: <12}*{self.ll[Day(6)][i]: <12}*"
            out += "\n********************************************************************************************"
        return out

##########################################################
    def isTermFree(self, term: Term):
        if term.hour not in self.time_conv.keys():
            return False
        return self.ll[term.day][self.time_conv[term.hour]] == ''

    
    def isCool(self, term: Term, full_time: bool):
        start = term.hour*60+term.minute
        if start >= self.full_time[full_time][term.day][0]*60:
            if start + 90 < self.full_time[full_time][term.day][1]*60:
                return True
        return False

    def can_be_transferred_to(self, term: Term, full_time: bool) -> bool:
        return self.isTermFree(term) and self.isCool(term, full_time)



 ##########################################################

    def put(self, lesson: Lesson) -> bool:
        if self.isCool(lesson.term, lesson.full_time) and self.isTermFree(lesson.term):
            self.lesson_list.append(lesson)
            return True
        return False
##########################################################

    def parse(self, actions: List[str]) -> List[Action]:
        out = list()
        for action in actions:
            if action == "d+":
                out.append(Action.DAY_LATER)
            elif action == "d-":
                out.append(Action.DAY_EARLIER)
            elif action == "t+":
                out.append(Action.TIME_LATER)
            elif action == "t-":
                out.append(Action.TIME_EARLIER)
        return out


##########################################################

    def perform(self, actions: List[Action]):
        actions_trans = { 
            Action.TIME_EARLIER : Lesson.earlierTime,
            Action.TIME_LATER : Lesson.laterTime,
            Action.DAY_LATER : Lesson.laterDay,
            Action.DAY_EARLIER : Lesson.earlierDay
        }
        for i in range(0, len(actions)):
            to_do = actions_trans[actions[i]]
            index = i%len(self.lesson_list)
            lesson = self.lesson_list[index]
            h, m, d, = 0,0,0
            action = actions[i]
            if action == Action.TIME_EARLIER:
                h = -1
                m = -30
            if action == Action.TIME_LATER:
                h = 1
                m = 30
            if action == Action.DAY_LATER:
                d = 1
            if action == Action.DAY_EARLIER:
                d = -1
            new_term = Term(lesson.term.hour+h, (lesson.term.minute+m)%60, lesson.term.duration, Day(lesson.term.day.value+d))
            if self.can_be_transferred_to(new_term, lesson.full_time):
                to_do(self.lesson_list[index])
            
        
##########################################################