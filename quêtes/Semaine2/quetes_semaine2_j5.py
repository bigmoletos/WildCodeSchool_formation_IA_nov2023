

"""
Help for statisticians!
Your fellow statisticians need you. They want to learn how to program in Python and have tons of calculations to do.

Very kindly, you agree to help them. Complete the missions below.

For all functions below, please add an extra cell where you actually call the function on at least two different inputs and displays the returned value (if the function doesn't already display stuff).
"""

# Mission 9: Create a function that takes a day as a parameter and returns the next day (i.e. for Sunday it would return Monday).
# You can use lists or dictionaries to solve this.

def get_next_day(your_day):
    list_days=["monday","thuesday","wednesday","thursday","friday","saturday","sunday"]
    i=0
    for day in list_days:
        if day== your_day:
            current_day_index = days_of_week.index(day)
        next_day_index = (current_day_index + 1) % 7
            nextday=list_days[i]
    return nextday


# test de la fonction
day="Sunday"
get_next_day(day)


def next_day(day):
    days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    try:
        current_day_index = days_of_week.index(day)
        next_day_index = (current_day_index + 1) % 7
        return days_of_week[next_day_index]
    except ValueError:
        return "Invalid day. Please enter a valid day of the week."

# Test the function
print(next_day('Sunday'))  # Output: Monday
