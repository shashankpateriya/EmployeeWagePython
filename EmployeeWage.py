import random


class EmployeeWage:

    is_half_time = 1
    is_full_time = 2
    emp_rate_per_hour = 20
    emp_hrs = 0
    emp_wage = 0
    full_time_emp_hrs = 8
    half_time_emp_hrs = 4

    def employee_attendance(i):
        attendance = random.randint(0, 2)
        return attendance

    def employee_work_hours(i, attendance_of_employee):
        switch = {
            0: EmployeeWage.full_time_emp_hrs,
            1: EmployeeWage.half_time_emp_hrs,
            2: 0
        }
        EmployeeWage.emp_hrs = switch.get(attendance_of_employee)
        print(EmployeeWage.emp_hrs)

if __name__ == '__main__':
    print("Welcome to Employee Wage Computation Program")
    employee = EmployeeWage()
    is_present = employee.employee_work_hours(employee.employee_attendance())
    employee.emp_wage = employee.emp_rate_per_hour * employee.emp_hrs
    print(employee.emp_wage)