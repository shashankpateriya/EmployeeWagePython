import logging
import random
import pandas
from valueoutofbound import ValueOutOfBound
logging.basicConfig(
    filename="employeewagelogger.log",
    filemode="a",
    format="%(asctime)s %(levelname)s-%(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)
log = logging.getLogger()


class CompanyWageInfo:

    def __init__(self, name, wage_per_hour, maximum_working_hours, maximum_working_days):
        self.name = name
        self.wage_per_hour = wage_per_hour
        self.maximum_working_hours = maximum_working_hours
        self.maximum_working_days = maximum_working_days


class EmployeeWage:
    is_absent = 0
    is_present = 1
    is_part_time = 2
    full_day_hours = int(input("Enter full day hours: "))
    part_time_hours = int(input("Enter half day hours: "))
    company_list = []

    def __init__(self, *company):
        self.company_list.extend(company)

    def employee_check(self, checkemp):
        try:
            attendance = {
                self.is_present: self.full_day_hours,
                self.is_part_time: self.part_time_hours,
                self.is_absent: 0,
            }
            return attendance.get(checkemp)
        except Exception as e:
            log.warning("Invalid input ", e)

    def compute_wage(self, company):
        working_days = 0
        working_hours = 0
        total_wage = 0
        try:
            while (working_days < company.maximum_working_days) \
                    and (working_hours < company.maximum_working_hours):
                random_number = random.randint(0, 2)  # To obtain a random number between 0 and 3
                employee_working_hours = self.employee_check(random_number)
                daily_wage = company.wage_per_hour * employee_working_hours
                total_wage += daily_wage
                working_days += 1
                working_hours += employee_working_hours
            print(f"Employee's salary for company {company.name} in the month is {total_wage}")
        except TypeError:
            print("Input correct naming convention")
        except ValueOutOfBound:
            print("Value is not in range")

    def company_emp_wage(self):
        for company in self.company_list:
            self.compute_wage(company)

 
if __name__ == '__main__':
    print('Welcome to Employee Wage Computation Program')
    reliance = CompanyWageInfo("reliance", 20, 100, 20)
    bigbazar = CompanyWageInfo("Bigbazar", 25, 75, 15)
    flipk = CompanyWageInfo("Flipkart", 20, 60, 30)
    dMart = CompanyWageInfo("DMart", 15, 95, 25)

    companies = EmployeeWage(reliance, bigbazar, flipk, dMart)
    companies.company_emp_wage()

    df = pandas.to_csv("companyinfo.csv")
    print(df)