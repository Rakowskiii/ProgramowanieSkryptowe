from .day import Day
import math
class Term(object):
    def __init__(self, h, m,duration = 90,day = None):
        self.trans ={
            Day.MON: "Poniedzialek",
            Day.TUE: "Wtorek",
            Day.WED: "Sroda",
            Day.THU: "Czwartek",
            Day.FRI: "Piątek",
            Day.SAT: "Sobota",
            Day.SUN: "Niedziela"
        }
        self.hour = h
        self.minute = m 
        self.duration = duration
        self.__day = day

    def __str__(self):
        if self.__day == None:
            return f"{self.hour}:{self.minute} [{self.duration}]"
        return f"{self.trans[self.__day]} {self.hour}:{self.minute} [{self.duration}]"
    
    def earlierThan(self, termin):
        if self.__day.value < termin.__day.value:
            if self.hour < termin.hour:
                return True
            elif self.hour == termin.hour:
                if self.minute < termin.minute:
                    return True
        return False
    
    def laterThan(self, termin):
        if self.__day.value > termin.__day.value:
            if self.hour > termin.hour:
                return True
            elif self.hour == termin.hour:
                if self.minute > termin.minute:
                    return True
        return False

    def equals(self, termin):
        if str(self) == str(termin):
            return True
        return False

    def minuteDifference(self, term):
        dur = int(math.fabs((self.hour*60+self.minute)-(term.hour*60+term.minute)))
        return Term(self.__day, self.hour, self.minute, dur)

    def endTime(self):
        time = (self.hour*60+self.minute+self.duration)
        fmin = time%60
        fhour = time//60
        fday = (self.__day.value + fhour//24)%7
        fhour = fhour%24
        return Term(Day(fday),fhour,fmin)
        

