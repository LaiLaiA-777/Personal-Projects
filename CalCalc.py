# This program will calculate the amount of calories that the user needs to
# maintain, lose or gain weight.


""" The main function will retireve data from all other funtions and use it
to display the need calories"""

def main():
    print("Welcme to Calorie Calculator")
    name = getName()
    age = getAge()
    height = getHeight()
    weight = getWeight()
    gender = getGender()
    actlvl = getActivityLevel()
    calneed = findCalories(height, age, weight, gender, actlvl)
    displayResults(calneed)

""" getName function will request name from user and
confirm that their input is correct. """

def getName():
    rightName = "N"                                        # Set Rightname to N 
    while rightName.upper() != "Y":                        # Loop for asking and confirming users name
        name = input('What is your name? ')                # Request name from user and assign input to name
        rightName = input(f"Is {name} correct (Y or N)? ") # Confirm name is correct
    return name

""" getAge function request age from user and
confirm if input is correct. """
        
def getAge():
    age = 1
    rightAge = "N"
    while age != 0:
        age = int(input("How old are you? "))
        rightAge = input(f"Is {age} correct (Y or N)? ")
        if rightAge.upper() == "Y":
            break
        else:
            continue
    if age < 15:
        print("""You are too young! It is important to enjoy your youth! 
              Trying to lose or gain weight too early can cause
              disruptions to your brain development. Please be cautious
              as you proceed! """)
        return age
    else:
        return age

def getHeight():
    height = 1
    rightHeight = "N"
    while height != 0:
        height = float(input("What is your height? "))
        rightHeight = input(f"Is {height} correct (Y or N)? ")
        if rightHeight.upper() == "Y":
            break
        elif rightHeight.upper() != ("Y" or "N"):
            print("""Please enter "Y" or "N" """)
            continue
        else:
            continue
    convHeight = input("Is your height in centimeters or inches? ")
    if convHeight.upper() == "INCHES":
        height *= 2.54
    return height

def getWeight():
    weight = 1
    rightWeight = "N"
    while weight != 0:
        weight = float(input("What is your weight? "))
        rightWeight = input(f"Is {weight} correct? ")
        if rightWeight.upper() == "Y":
            break
        elif rightWeight.upper() != ("Y" or "N"):
            print("""Please enter "Y" or "N" """)
            continue
        else:
            continue
    convWeight = input("Is your weight is pounds or kilos? ")
    if convWeight.upper() == "POUNDS":
        weight *= 0.453592
    return weight

def getGender():
    gender = "None"
    while gender == "None":
        gender = input("What is your gender (M or F)? ")
    return gender

def getActivityLevel():
    print("How many days per week do you exercise?")
    print("Exercise Levels")
    print("Little to No Exercise: 1")
    print("1-3 days per week: 2")
    print("4-5 days per week: 3")
    print("6-7 days per week: 4")
    print("6-7 days per week and Physical Job: 5")
    
    actlvl = 1
    while actlvl != 0:
        actlvl = int(input("What is your exercise level? "))
        if actlvl >= 1 and actlvl <= 5:
            break
        else:
            print("Please enter a level between 1 and 5")
            continue

# Assign Activity Factor to activity level
    if actlvl == 1:
        actRate = 1.2
    elif actlvl == 2:
        actRate = 1.375
    elif actlvl == 3:
        actRate = 1.55
    elif actlvl == 4:
        actRate = 1.725
    else:
        actRate = 1.9
              
    return actRate         # Return actRate to main function       
    
def findCalories(height, age, weight, gender, actRate):

    if gender == "M":

        calneed = 66.5 + (13.75 * weight) + (5.003 * height) - (6.75 * age)

    else:
        calneed = 655.1 + (9.563 * weight) + (1.850 * height) - (4.675 * age)

    return calneed

    

    
    print(height, age, weight, gender, actRate)

def displayResults(calneed):
    print(calneed, ".2f")

main()
