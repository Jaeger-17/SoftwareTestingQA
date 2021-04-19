import unittest
from Retirement import Retirement
from BMI import BMI

class TestBMIRetirement(unittest.TestCase):

    def test_calculate_bmi(self):
        userBMI_1 = BMI(5, 10, 100)
        userBMI_2 = BMI(5, 10, 126)
        userBMI_3 = BMI(5, 10, 150)
        userBMI_4 = BMI(5, 10, 170)
        userBMI_5 = BMI(5, 2, 150)
        userBMI_6 = BMI(5, 10, 204)
        userBMI_7 = BMI(5, 2, 175)

        self.assertEqual(userBMI_1.calculate_bmi(), 14.7)
        self.assertEqual(userBMI_2.calculate_bmi(), 18.5)
        self.assertEqual(userBMI_3.calculate_bmi(), 22.0)
        self.assertEqual(userBMI_4.calculate_bmi(), 25.0)
        self.assertEqual(userBMI_5.calculate_bmi(), 28.1)
        self.assertEqual(userBMI_6.calculate_bmi(), 30.0)
        self.assertEqual(userBMI_7.calculate_bmi(), 32.8)

    def test_give_result(self):

        userBMI_1 = BMI(5, 10, 100)
        userBMI_2 = BMI(5, 10, 126)
        userBMI_3 = BMI(5, 10, 150)
        userBMI_4 = BMI(5, 10, 170)
        userBMI_5 = BMI(5, 2, 150)
        userBMI_6 = BMI(5, 10, 204)
        userBMI_7 = BMI(5, 2, 175)

        self.assertEqual(userBMI_1.give_result(), "You are underweight.")
        self.assertEqual(userBMI_2.give_result(), "Your weight is normal.")
        self.assertEqual(userBMI_3.give_result(), "Your weight is normal.")
        self.assertEqual(userBMI_4.give_result(), "You are overweight.")
        self.assertEqual(userBMI_5.give_result(), "You are overweight.")
        self.assertEqual(userBMI_6.give_result(), "You are obese.")
        self.assertEqual(userBMI_7.give_result(), "You are obese.")

    def test_calculate_retirement(self):
        

if __name__ == '__main__':
    unittest.main()
