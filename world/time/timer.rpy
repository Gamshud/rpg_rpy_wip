init:
    default time = Timer(minutes=23, hours=0, days=14, months=4, years=1283)


init -3 python:
    class Timer():
        def __init__(self, minutes=0, hours=0, days=0, years=0, months=1):
            self.globalminutes = 0
            self.minutes = minutes
            self.hours = hours
            self.days = days
            self.currentday = 0
            self.months = months
            self.years = years
            self.curr_month = months
            self.part = "morning"
            self.time_of_the_year = "spring"
            self.hoursadd(0)
            self.hoursaddy(0)

        def checktime(self):
            time_date = ((str(self.minutes)) + "m. " + (str(self.hours)) + "h. " + (str(self.days)) + "d. " + (str(self.months)) + "M. " + (str(self.years)) + "Y. " + self.time_of_the_year + " ")
            return(time_date)
            
        def hoursadd(self, add):
            minutes = (add * 60)
            self.minutesadd(minutes)
            
        def minutesadd(self, add_minutes):
            self.minutes += add_minutes
            self.globalminutes += add_minutes
            for i in pc.buffs:
                if i[0] <= self.globalminutes:
                    pc.buff_del(i[1])
                    pc.buffs.remove(i)
                    self.minutesadd(0)
                else:
                    pass
            while self.minutes >= 60:
                self.minutes -= 60
                self.hoursaddy(1)
            
            self.checktime()
            
       
        def hoursaddy(self, add_hours):
            self.hours += add_hours
            while self.hours >= 24:
                self.hours -= 24
                self.daysadd(1)
                self.currentday += 1
                pc.all_charsstat()
                
            if self.hours >= 23 or self.hours <= 4:
                self.part = "night"
            elif self.hours >= 5 and self.hours <= 8:
                self.part = "morning"
            elif self.hours >= 9 and self.hours <= 18:
                self.part = "day"
            elif self.hours >= 19 and self.hours <= 22:
                self.part = "evening"
             

        def daysadd(self, days_add):
            self.days += days_add
            
            while (self.months == 1 or self.months == 3 or self.months == 5 or self.months == 7 or self.months == 8 or self.months == 10 or self.months == 12) and self.days > 31:
                self.month(1)
                self.days -= 31
            while self.months == 2 and self.days > 28:
                self.month(1)
                self.days -= 28
            while (self.months == 4 or self.months == 6 or self.months == 9 or self.months == 11) and self.days > 30:
                self.month(1)
                self.days -= 30
            if self.months >= 13:
                self.month(0)

        def month(self, add_month):
            self.months += add_month
            while self.months > 12:
                    self.months -= 12
                    self.years += 1
            if (self.months == 12 or self.months == 1 or self.months == 2):
                self.time_of_the_year = self.toty = "winter"
            elif (self.months == 3 or self.months == 4 or self.months == 5):
                self.time_of_the_year = self.toty = "spring"
            elif (self.months == 6 or self.months == 7 or self.months == 8):
                self.time_of_the_year = self.toty = "summer"
            elif (self.months == 9 or self.months == 10 or self.months == 11):
                self.time_of_the_year = self.toty = "autumn"
            
            

            