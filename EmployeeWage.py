import random


class EmployeeWage:

    def employee_attendance(self):
        attendance = random.randint(0, 1)
        if attendance == 0:
            print("Employee is Present")
        else:
            print("Employee is Absent")
        return attendance
    def employee_wage(self):
        # is_full_time = 1
        emp_rate_per_hour = 20
        # emp_hrs = 0
        # emp_wage = 0
        empcheck = random.randint(0, 1)
        if empcheck == 1:
            emp_hrs = 8
            print("Employee is presnt and daily wage is " + str(emp_hrs * emp_rate_per_hour))
        else:
            emp_hrs = 0
            print(f"Employee is absent")
        return empcheck

if __name__ == '__main__':
    print("Welcome to Employee Wage Computation Program")
    employee = EmployeeWage()
    is_present = employee.employee_attendance()
    wage = EmployeeWage()
    total_wage = wage.employee_wage()