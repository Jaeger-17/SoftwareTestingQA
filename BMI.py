class BMI:

    def __init__(self, givenFeet = 5, givenInches = 0, givenWeight = 100):
        self.inches = givenInches
        self.feet = givenFeet 
        self.weight = givenWeight

    def set_height(self, givenFeet, givenInches):
        self.feet = givenFeet
        self.inches = givenInches

    def set_weight(self, givenWeight):
        self.weight = givenWeight

    '''def get_height(self):
        return (self.feet * 12) + self.inches'''

    def calculate_bmi(self):
        kilos = self.weight * 0.45
        meters = ((self.feet * 12) + self.inches) * 0.025
        result = (kilos / (meters * meters))
        return round(result, 1)

    def give_result(self):
        bmi = self.calculate_bmi()
        if bmi < 18.5:
            return "You are underweight."
        elif (bmi >= 18.5 and bmi < 25):
            return "Your weight is normal."
        elif (bmi >= 25 and bmi < 30):
            return "You are overweight."
        else:
            return "You are obese."
