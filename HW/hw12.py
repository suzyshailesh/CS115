'''
Created on 11/25/18
@author:   Susmitha Shailesh
Pledge:    I pledge my honor that I have abided by the Stevens Honor System.

CS115 - Hw 12 - Date class
'''
DAYS_IN_MONTH = (0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)

class Date(object):
    '''A user-defined data structure that stores and manipulates dates.'''

    # The constructor is always named __init__.
    def __init__(self, month, day, year):
        '''The constructor for objects of type Date.'''
        self.month = month
        self.day = day
        self.year = year

    # The 'printing' function is always named __str__.
    def __str__(self):
        '''This method returns a string representation for the
           object of type Date that calls it (named self).

             ** Note that this _can_ be called explicitly, but
                it more often is used implicitly via the print
                statement or simply by expressing self's value.'''
        return '%02d/%02d/%04d' % (self.month, self.day, self.year)

    # Here is an example of a 'method' of the Date class.
    def isLeapYear(self):
        '''Returns True if the calling object is in a leap year; False
        otherwise.'''
        if self.year % 400 == 0:
            return True
        if self.year % 100 == 0:
            return False
        if self.year % 4 == 0:
            return True
        return False

    def copy(self):
        '''Returns a new object with the same month, day, year
        as the calling object (self).'''
        dnew = Date(self.month, self.day, self.year)
        return dnew
    
    def equals(self, d2):
        '''Decides if self and d2 represent the same calendar date,
        whether or not they are the in the same place in memory.'''
        return self.year == d2.year and self.month == d2.month and \
               self.day == d2.day

    def tomorrow(self):
        '''Changes the calling object so that it represents one calendar
        day after the date it originally represented'''

        if self.month == 2 and self.isLeapYear() == True:
            DIM = 29
        else: DIM = DAYS_IN_MONTH[self.month]

        if self.month == 12 and self.day == 31:
            self.year = self.year + 1
            self.month = 1
            self.day = 1
        elif self.day == DIM:
            self.month = self.month + 1
            self.day = 1
        else: self.day = self.day + 1

    def yesterday(self):
        '''Changes the calling object so that it represents one calendar
        day before the date it originally represented'''
        if self.month == 3 and self.isLeapYear() == True:
            DIM = 29
        else: DIM = DAYS_IN_MONTH[self.month-1]

        if self.month == 1 and self.day == 1:
            self.year = self.year - 1
            self.month = 12
            self.day = 31
        elif self.day == 1:
            self.month = self.month - 1
            self.day = DIM
        else: self.day = self.day - 1

    def addNDays(self, N):
        '''Changes the calling object so that it represents N calendar days
        after the date it originally represented'''
        for i in range(N):
            print(self)
            self.tomorrow()
        print(self)

    def subNDays(self, N):
        '''Changes the calling object so that it represents N calendar days
        before the date it originally represented'''
        for i in range(N):
            print(self)
            self.yesterday()
        print(self)

    def isBefore(self, d2):
        '''returns True if the calling object is a calendar date before the
        input d2'''
        if self.year < d2.year:
            return True
        elif self.year == d2.year and self.month < d2.month:
            return True
        elif self.year == d2.year and self.month == d2.month and\
             self.day < d2.day:
            return True
        else: return False

    def isAfter(self, d2):
        '''returns True if the calling object is a calendar date after the
        input d2'''
        if self.year > d2.year:
            return True
        elif self.year == d2.year and self.month > d2.month:
            return True
        elif self.year == d2.year and self.month == d2.month and\
             self.day > d2.day:
            return True
        else: return False

    def diff(self, d2):
        '''returns an integer representing the number of days
        between self and d2'''
        d3 = self.copy()
        d4 = d2.copy()
        count = 0
        while d3.isBefore(d4):
            d4.yesterday()
            count=count-1
        while d3.isAfter(d4):
            d4.tomorrow()
            count=count+1
        return count

    def dow(self):
        '''returns the day of the week of the object that calls it'''
        num = self.diff(Date(11,9,2011))

        if num < 0:
            day = (7+num)%7
        else: day = num%7

        if day == 1:
            return "Thursday"
        elif day == 2:
            return "Friday"
        elif day == 3:
            return "Saturday"
        elif day == 4:
            return "Sunday"
        elif day == 5:
            return "Monday"
        elif day == 6:
            return "Tuesday"
        elif day == 7 or day == 0:
            return "Wednesday"
                
                
