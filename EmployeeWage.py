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
            print("Employee is Full time Present with wage " + str(EmployeeWage.full_time_emp_hrs * EmployeeWage.emp_rate_per_hour))
        elif attendance == EmployeeWage.is_half_time:
            print("Employee is Half time Present with wage " + str(EmployeeWage.half_time_emp_hrs * EmployeeWage.emp_rate_per_hour))
        else:
            print("Employee is absent")
        return attendance

if __name__ == '__main__':
    print("Welcome to Employee Wage Computation Program")
    employee = EmployeeWage()
    is_present = employee.employee_attendance()