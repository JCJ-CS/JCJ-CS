import math

def tdee_calculator(gender, age, height, weight, activity_level, goal):
    tdee = 0
    multiplier = 0
    height = height 
    weight = weight
    type_of_goal =""
    
    if activity_level == 1:
        multiplier = 1.2
    elif activity_level == 2:
        multiplier = 1.375
    elif activity_level == 3:
        multiplier = 1.55
    elif activity_level == 4:
        multiplier = 1.725
    elif activity_level == 5:
        multiplier = 1.9
    else:
        print ("Please choose an activity level.")
        
    if gender == "female":
        tdee = (655 + (4.35*weight) + (4.7*height) - (4.7*age))*multiplier
    elif gender == "male":
        tdee = (66 + (6.23*weight) + (12.7*height) - (6.8*age))*multiplier
    
    print(str(math.ceil(tdee)) + " k/cal")
    
    if goal != "":
        proteins = 0
        fats = 0
        carbs = 0
        if goal == 1:
            type_of_goal = "lean bulking"
            proteins = weight + 25
            fats = 75
            carbs = weight * 1.75
        if goal == 2:
            type_of_goal = "dirty bulking"
            proteins = weight + 35
            fats = 100
            carbs = weight *1.85
        if goal == 3:
            type_of_goal = "maintaining weight"
            proteins = weight + 25
            fats = 75
            carbs = weight*1.25
        if goal == 4:
            type_of_goal = "cutting weight"
            proteins = weight + 25
            fats = 50
            carbs = (weight / 10)*10
        print("Since you chose %s as your goal, follow these macros while maintaining a daily carb-cycle:" % type_of_goal)
        print("Protein - %d (+/- 10)" % proteins)
        print("Fats - %d (+/- 25)" % fats)
        print("Carbs - %d (+/- 20)" % carbs)


tdee_calculator("female", 29, 62, 107, 2, 3)
    
        