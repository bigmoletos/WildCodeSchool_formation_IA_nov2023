

"""
Help for statisticians!
Your fellow statisticians need you. They want to learn
how to program in Python and have tons of calculations to do.

Very kindly, you agree to help them. Complete the missions below.

For all functions below, please add an extra cell where you
actually call the function on at least two different inputs
and displays the returned value (if the function doesn't
already display stuff).
"""

# Mission 9: Create a function that takes a day as a parameter and returns the next day (i.e. for Sunday it would return Monday).
# You can use lists or dictionaries to solve this.

def get_next_day(your_day):
    list_days=["monday","thuesday","wednesday","thursday","friday","saturday","sunday"]
    if your_day.lower() in list_days:
        nextday = list_days.index(your_day.lower())
        print(nextday)
        # nextday = (nextday + 1) % 7
        nextday = [
            (nextday + 1)
            if not (nextday + 1)==7
            else 0
            for i in range(6)
              ]
        print(nextday)
        list_days=list_days[nextday]
    else:
        return
    # print("the next day: ", list_days)
    return list_days




# test de la fonction


your_day="sunday"
print("ma variable: ", get_next_day(your_day))

# def next_day(day):
#     days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
#     try:
#         current_day_index = days_of_week.index(day)
#         next_day_index = (current_day_index + 1) % 7
#         return days_of_week[next_day_index]
#     except ValueError:
#         return "Invalid day. Please enter a valid day of the week."

# # Test the function
# print(next_day('Sunday'))  # Output: Monday
