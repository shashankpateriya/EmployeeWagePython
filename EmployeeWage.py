import random

is_absent = 0
is_half_time = 1
is_full_time = 2
emp_rate_per_hour = 20
emp_hrs = 0
emp_wage = 0
full_time_emp_hrs = 8
half_time_emp_hrs = 4


def employee_attendance():
    attendance = {
        is_full_time: full_time_emp_hrs,
        is_half_time: half_time_emp_hrs,
        is_absent: 0
    }
    day = 0
    total_emp_hours = 0

    while (day < 20 and total_emp_hours < 100):
        checkemp = random.randint(0, 2)
        total_emp_hours = total_emp_hours + attendance.get(checkemp)
        day = day + 1

    return total_emp_hours * emp_rate_per_hour

if __name__ == '__main__':
    total_emp_wage = employee_attendance()
    print(f"Total wage of employee of a month is {total_emp_wage}")
