from enum import Enum
import math
class Day(Enum):
    MON = 0
    TUE = 1
    WED = 2
    THU = 3
    FRI = 4
    SAT = 5
    SUN = 6
    def difference(self, day):
        d = day.value-self.value
        if  d > 3:
            return d-7
        elif d < - 3:
            return d+7
        else:
            return d


def nthDayFrom(n, day):
    return(Day((n+day.value)%7))
