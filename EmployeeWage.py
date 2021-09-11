import random

is_absent = 0
is_half_time = 1
is_full_time = 2
emp_rate_per_hour = 20
emp_hrs = 0
emp_wage = 0
full_time_emp_hrs = 8
half_time_emp_hrs = 4


def employee_attendance(wage_per_hour,num_of_working_days,work_hours_per_month,company):
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

    total_emp_wage = total_emp_hours * emp_rate_per_hour
    print(f"Total wage for company {company} is {total_emp_wage}")

employee_attendance(21,25,100,"Unysis")
employee_attendance(30,35,110,"Airtel")