import random

class EmployeeWage:

    is_half_time = 1
    is_full_time = 2
    emp_rate_per_hour = 20
    emp_hrs = 0
    emp_wage = 0
    full_time_emp_hrs = 8
    half_time_emp_hrs = 4

    def employee_attendance(self):
        attendance = random.randint(0, 2)
        if attendance == EmployeeWage.is_full_time:
            print("Employee is Full time Present")
            EmployeeWage.emp_hrs = EmployeeWage.full_time_emp_hrs
        elif attendance == EmployeeWage.is_half_time:
            print("Employee is Half time Present")
            EmployeeWage.emp_hrs = EmployeeWage.half_time_emp_hrs
        else:
            print("Employee is absent")
            EmployeeWage.emp_hrs = 0

if __name__ == '__main__':
    print("Welcome to Employee Wage Computation Program")
    total_emp_wage_for_a_month = 0
    emp_wage_for_a_month = 0
    total_emp_hours = 0
    day =1
    while ( day < 20 and total_emp_hours < 100):
        print(f"day {day} : ")
        EmployeeWage().employee_attendance()
        total_emp_hours = total_emp_hours + EmployeeWage.emp_hrs
        EmployeeWage.emp_wage = EmployeeWage.emp_rate_per_hour * EmployeeWage.emp_hrs
        print("Employee salary for day is " + str(EmployeeWage.emp_wage))
        total_emp_wage_for_a_month = total_emp_wage_for_a_month + EmployeeWage.emp_wage
        day = day + 1
    else:
        print(f"\nEmployee's Salary for the Entire Month is: {total_emp_wage_for_a_month}")