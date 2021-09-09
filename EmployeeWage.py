import random


class EmployeeWage:

    def employee_attendance(self):
        attendance = random.randint(0, 1)
        if attendance == 0:
            print("Employee is Present")
        else:
            print("Employee is Absent")
        return attendance


if __name__ == '__main__':
    print("Welcome to Employee Wage Computation Program")
    employee = EmployeeWage()
    isPresent = employee.employee_attendance()