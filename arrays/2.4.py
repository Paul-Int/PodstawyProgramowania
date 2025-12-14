# Weekly meal plan [Breakfast, Lunch, Dinner] for 7 days
meal_plan = [
    ["Oatmeal", "Grilled Chicken Salad", "Spaghetti"],
    ["Pancakes", "Sandwich", "Steak"],
    ["Smoothie", "Chicken Wrap", "Salmon"],
    ["Eggs", "Pasta", "Soup"],
    ["Toast", "Burrito", "Pizza"],
    ["Cereal", "Salad", "Fish Tacos"],
    ["Bagel", "Rice and Beans", "Stir-fry"]
]

def weekday(n):
    weekdays = ["Monday", "Tuesday", "Wednesday",
                "Thursday", "Friday", "Saturday", "Sunday"]
    return weekdays[n - 1]

def day_meal_plan(meal_plan, day_number):
    meals = meal_plan[day_number - 1]
    return meals[0] + ", " + meals[1] + ", " + meals[2]

print("WEEKLY MEAL PLAN")
print("(Breakfast, Lunch, Dinner)")
print("============================")

day = 1
while day <= 7:
    print(weekday(day) + ":", day_meal_plan(meal_plan, day))
    day += 1