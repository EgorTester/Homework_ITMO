def task_1(a, b):
    result = max(a, b)
    print(result)


def task_2(a, b):
    result = "yes" if abs(a-b) == 135 else "no"
    print(result)


def task_3(m):
    seasons = {12:"зима", 1:"зима", 2:"зима", 3:"весна", 4:"весна", 5:"весна",
               6:"лето", 7:"лето", 8:"лето", 9:"осень", 10:"осень", 11:"осень"}
    result = seasons[m]
    print(result)


def task_4(a, b, c):
    result = "yes" if all(x > 10 for x in [a, b, c]) else "no"
    print(result)


def task_5(numbers):
    result = sum(1 for x in numbers if x > 10)
    print(result)


def task_6(years, months):

    days_in_year = 365
    days_in_month = 29

    total_days = years * days_in_year + months * days_in_month

    print(total_days)

task_1(15, 23)
(task_2(150, 15))
task_3(7)
task_6(1, 5)