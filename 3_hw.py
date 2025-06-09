def task_1(a, b):
    result = max(a, b)
    print(result)
    return result

def task_2(a, b):
    result = "yes" if abs(a-b) == 135 else "no"
    print(result)
    return result

def task_3(m):
    seasons = {12:"зима", 1:"зима", 2:"зима", 3:"весна", 4:"весна", 5:"весна",
               6:"лето", 7:"лето", 8:"лето", 9:"осень", 10:"осень", 11:"осень"}
    result = seasons[m]
    print(result)
    return result

def task_4(a, b, c):
    result = "yes" if all(x > 10 for x in [a, b, c]) else "no"
    print(result)
    return result

def task_5(numbers):
    result = sum(1 for x in numbers if x > 8)
    print(result)
    return result

def task_6():
    result = 365 * 29
    print(result)
    return result

task_1(15, 23)
(task_2(150, 15))
task_3(7)