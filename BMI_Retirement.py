from BMI import BMI
from Retirement import Retirement

def main():
    userBmi = BMI()
    userRetirement = Retirement()

    while(1):
        print("Welcome! This app will help you calculate your BMI or your desired retirement age!")
        print("At any point, type 'exit' to leave the program.")
        print("What would you like to calculate?")
        response = str(input("BMI or Retirement: "))

        if response == "BMI":
            
            print("Enter your height in feet and inches.")
            response = input("Feet: ")
            if response == "exit":
                break
            userBmi.feet = int(response)

            response = input("Inches: ")
            if response == "exit":
                break
            userBmi.inches = int(response)

            response = input("Enter your weight in pounds: ")
            if response == "exit":
                break
            userBmi.weight = int(response)

            print("Your BMI is: ", userBmi.calculate_bmi())
            print(userBmi.give_result())
            print("")

        elif response == "retirement":

            response = input("Enter your age: ")
            if response == "exit":
                break
            userRetirement.age = int(response)

            response = input("Enter your salary: ")
            if response == "exit":
                break
            userRetirement.salary = int(response)

            response = input("Enter the percent of your salary you save annually: ")
            if response == "exit":
                break
            if int(response) > 100:
                response = 100
            userRetirement.percent = int(response)

            response = input("Enter your desired retirement savings goal: ")
            if response == "exit":
                break
            userRetirement.goal = int(response)

            print(userRetirement.give_retirement_age())
            print("")


        elif response == "exit":
            break

        else:
            print("ERROR: Not a valid response. Please enter 'BMI' or 'Retirement' or 'exit'.")
            print("")

main()



