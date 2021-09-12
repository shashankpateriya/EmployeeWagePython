import random

is_absent = 0
is_half_time = 1
is_full_time = 2
full_time_emp_hrs = 8
half_time_emp_hrs = 4


class EmpWageBuilder:
    def __init__(self, wage_per_hour, num_of_working_days, work_hours_per_month, company):
        self.wage_per_hour = wage_per_hour
        self.num_of_working_days = num_of_working_days
        self.work_hours_per_month = work_hours_per_month
        self.company = company

    def daily_wage(self,emp_hours):
        return emp_hours * self.wage_per_hour

    def employee_attendance(self,checkemp):
        attendance = {
            is_full_time: full_time_emp_hrs,
            is_half_time: half_time_emp_hrs,
            is_absent: 0
        }
        return attendance.get(checkemp)

    def employee_salary(self):
        day = 0
        total_working_hours = 0
        total_emp_wage = 0
        while (day < 20 and total_working_hours < 100):
            checkemp = random.randint(0, 2)
            emp_hours = self.employee_attendance(checkemp)
            total_working_hours = total_working_hours + emp_hours
            day += 1
            total_emp_wage = self.daily_wage(emp_hours)
        return total_emp_wage

    def emp_calculate_salary(self):
        self.total_emp_wage = self.employee_salary()
        print(f"Employee wage for company {self.company} is {self.total_emp_wage}")

if __name__ == "__main__":
    print("Welcome to Employee Wage Builder")
    unysis = EmpWageBuilder(21, 25, 100, "Unysis")
    airtel = EmpWageBuilder(30, 35, 110, "Airtel")
    unysis.emp_calculate_salary()
    airtel.emp_calculate_salary()
