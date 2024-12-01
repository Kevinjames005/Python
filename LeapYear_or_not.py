def is_leap_year(year):
    """Checks if the given year is a leap year or not"""
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

input_year = int(input("Enter the year that you want to check if it's a leap year or not: "))
leap_or_not = is_leap_year(input_year)
if leap_or_not == True :
    print(f"The year {input_year} is a leap year.")
else :
    print(f"The year {input_year} is not a leap year.")

# Write your code here.
# Don't change the function name.