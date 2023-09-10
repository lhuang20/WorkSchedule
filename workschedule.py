# main
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
                return "No work (Night shift before)"
            elif n == (base + 7):
                return "No work (Day shift next)"
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

# Error checking function for month and date ranges
def is_month_error(m: int) -> bool:
  return m > 12 or m < 1

# Error checking function for month and date ranges
def is_day_error(d: int) -> bool:
  return d > 31 or d < 1

# frontend function
while True:
    month_input = int(input("Enter a month (number only): "))
    day_input = int(input("Enter a day (number only): "))
    if is_month_error(month_input):
      print("Month out of bounds")
    elif is_day_error(day_input):
      print("Day out of bounds")
    elif is_month_error(month_input) == False and is_day_error(day_input) == False:
      print(get_work_status(month_input, day_input))


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

# tests for error checking functions
# print(is_month_error(1000))
# print(is_month_error(11))
# print(is_month_error(12))
# print(is_month_error(13))
# print(is_month_error(-1))
# print(is_month_error(0))
# print(is_month_error(1))

# print(is_day_error(1000))
# print(is_day_error(30))
# print(is_day_error(31))
# print(is_day_error(29))
# print(is_day_error(32))
# print(is_day_error(-1))
# print(is_day_error(0))
# print(is_day_error(1))
