7# main
def get_work_status(month: int, day: int) -> str:
    n = convert_date_to_n(month, day)
    
    if n >= 175:
        base = 175 # June 24, 2023 = Work day
        threshold = 3
        while True:
            if base <= n <= (base + 1):
                return "Day"
            elif (base + 1) <= n <= (base + 2):
                return "Night (Swing)"
            elif (base + 1) <= n <= (base + 3):
                return "Night"                  
            if (base + 5) <= n <= (base + 6):
                return "No work"
            elif n == (base + 4):
                return "No work (Night shift yesterday)"
            elif n == (base + 7):
                return "No work (Day shift tomorrow)"
            base = base + threshold + 5
    if n < 175:
        base = 174 # June 24, 2023 = Work day
        threshold = 3
        while True:
            if base >= n >= base - threshold:
                return "No work"
            if (base - 4) >= n >= (base - 7):
                return "Work"
            base = base - threshold - 5          
                
# helper function
def convert_date_to_n(month: int, day: int) -> int:
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    acc = []
    n = 0
    
    for d in days:
        if n < (month-1):   
            acc.append(d)
            n += 1
                       
    return sum(acc) + day
            
# frontend function
while True:
    month_input = int(input("Enter a month: "))
    day_input = int(input("Enter a day: "))
    output = get_work_status(month_input, day_input)
    
    print(output)


# tests for convert_date_to_n        
# print(convert_date_to_n(12, 31))
# print(convert_date_to_n(6, 14))
# print(convert_date_to_n(1, 1))

# tests for get_work_status
# print(get_work_status(7, 2))
# print(get_work_status(6, 28))
# print(get_work_status(12, 31))

# print(get_work_status(6, 23))
# print(get_work_status(6, 22))
# print(get_work_status(6, 21))
# print(get_work_status(6, 20))
# print(get_work_status(6, 19))
# print(get_work_status(6, 18))

# print(get_work_status(6, 30))