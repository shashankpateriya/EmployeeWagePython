import logging
import random


from employeewageinfo import EmployeeWageInfo

logging.basicConfig(
    filename="employeewagelogger.log",
    filemode="a",
    format="%(asctime)s %(levelname)s-%(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)
log = logging.getLogger()


class EmployeeWage:
    is_absent = 0
    is_present = 1
    is_part_time = 2
    full_day_hours = 8
    part_time_hours = 4
    company_list = []
    company_dictionary = {}

    def add_company(self, name, wage_per_hour, maximum_working_hours, maximum_working_days):
        try:
            employee_wage_info = EmployeeWageInfo(name, wage_per_hour, maximum_working_hours, maximum_working_days)
            self.company_list.append(employee_wage_info)
            if len(self.company_list) == 0:
                raise Exception(' List is empty ')
            print(employee_wage_info)
            return employee_wage_info
        except Exception as e:
            log.warning("Invalid input")

    def employee_check(self, checkemp):
        try:
            attendance = {
                self.is_present: self.full_day_hours,
                self.is_part_time: self.part_time_hours,
                self.is_absent: 0,
            }
            return attendance.get(checkemp)
        except Exception as e:
            print("Invalid input ", e)

    def compute_wage(self, employee_wage_info):
        working_days = 0
        working_hours = 0
        total_wage = 0
        daily_wage = 0
        employee_working_hours = 0
        try:
            while working_days < employee_wage_info.get_maximum_working_days() \
                    and working_hours < employee_wage_info.get_maximum_working_hours():
                random_number = random.randint(0, 2)  # To obtain a random number between 0 and 3
                employee_working_hours = self.employee_check(random_number)
                daily_wage = employee_wage_info.get_wage_per_hour() * employee_working_hours
                total_wage += daily_wage
                working_days += 1
                working_hours += employee_working_hours
            print("Total wage of the company ", employee_wage_info.get_name(), " in the month is ", total_wage)
        except Exception as e:
            print("Invalid input ", e)


if __name__ == '__main__':

    employee_wage = EmployeeWage()
    employee_wage.add_company("reliance", 20, 100, 20)
    employee_wage.add_company("bigbazar", 25, 75, 15)
    employee_wage.add_company("flipkart", 20, 60, 30)
    employee_wage.add_company("dMart", 15, 95, 25)
    for _ in EmployeeWage.company_list:
        employee_wage.compute_wage(_)
