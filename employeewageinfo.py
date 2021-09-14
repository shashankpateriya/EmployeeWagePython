class EmployeeWageInfo:

    def __init__(self, name, wage_per_hour, maximum_working_hours, maximum_working_days):
        self.name = name
        self.maximum_working_days = maximum_working_days
        self.maximum_working_hours = maximum_working_hours
        self.wage_per_hour = wage_per_hour

    def __str__(self):
        return "{} {} {} {} ".format(self.name, self.maximum_working_hours, self.maximum_working_days,
                                     self.wage_per_hour)

    def get_name(self):
        return self.name

    def get_maximum_working_days(self):
        return self.maximum_working_days

    def get_maximum_working_hours(self):
        return self.maximum_working_hours

    def get_wage_per_hour(self):
        return self.wage_per_hour

    def set_name(self, name):
        self.name = name

    def set_maximum_working_days(self, maximum_working_days):
        self.maximum_working_days = maximum_working_days

    def set_maximum_working_hours(self, maximum_working_hours):
        self.maximum_working_hours = maximum_working_hours

    def set_wage_per_hour(self, wage_per_hour):
        self.wage_per_hour = wage_per_hour