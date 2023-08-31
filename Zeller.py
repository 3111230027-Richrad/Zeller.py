# File: zeller.py
# Description: Program to calculate the day of the week using Zeller's Congruence
# Assignment Number: 3
#
# Name: <Richard Loua>
# SID:  <3111230027>
# Email: <3111230027@live.gctu.edu.gh>
# Grader: <Carolyn OR Emma OR Ahmad>
#
# On my honor, <Richard>, this programming assignment is my own work
# and I have not provided this code to any other student.

def calculate_day_of_week(month, day, year):
    # Map month names to corresponding month numbers
    month_numbers = {
        "January": 13, "February": 14, "March": 3, "April": 4, "May": 5, "June": 6,
        "July": 7, "August": 8, "September": 9, "October": 10, "November": 11, "December": 12
    }

    # Adjust year for January and February
    if month == "January" or month == "February":
        year -= 1

    # Calculate required values
    month_number = month_numbers[month]
    variation_in_days_per_month = (13 * (month_number + 1)) // 5
    leap_year_days = year // 4 + year // 400
    century_days = year // 100
    total_days = day + variation_in_days_per_month + year + leap_year_days - century_days
    day_of_week = total_days % 7

    return day_of_week


# Get input from the user
month = input("Enter the month (for example, January, February, etc.): ")
day = int(input("Enter the day (an integer): "))
year = int(input("Enter the year (an integer): "))

# Calculate and print the day of the week
day_names = ['Saturday', 'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
day_of_week = calculate_day_of_week(month, day, year)
print(f"The day of the week is {day_names[day_of_week]}.")
