
import unittest
from .test_utils import CustomTestCase, CustomTestRunner


class TestExercise29(CustomTestCase):

    def test_list_usage(self):
        """
        The program should not use lists to solve the exercise.
        """
        self.assertNotUsesList()

    def test_dict_usage(self):
        """
        The program should not use dictionaries to solve the exercise.
        """
        self.assertNoUsesDictionary()

    def test_function_usage(self):
        """
        The program should not use functions to solve the exercise.
        """
        self.assertNotUseSelfDefinedFunctions()

    # ## Exercise 29: Caesar Cipher - Hard 🥵 (Est. Time: 15-20 mins | Points: 30)

    # **Problem:** Encrypt a string using the Caesar cipher, shifting letters by a specified number of places in the alphabet.

    # ### Input:
    # - An integer for the shift amount and a string to encrypt.

    # ### Output:
    # - The encrypted string.

    # ### Examples:


    # | No. | Inputs         | Outputs |
    # | --- | -------------- | ------- |
    # | 1   | 1<br>abc       | bcd     |
    # | 2   | 26<br>abc      | abc     |
    # | 3   | 1<br>Python    | Qzuipo  |
    # | 4   | 3<br>Python    | Sbwkrq  |
    # | 5   | 5<br>Python    | Udtqts  |

    def test_case_1(self):
        """
        Test case 1: Encrypting 'abc' with shift amount 1 should result in 'bcd'.
        """
        inputs = ["1", "abc"]
        output = self.run_exercise(inputs)
        expected_output = "bcd"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_case_2(self):
        """
        Test case 2: Encrypting 'abc' with shift amount 26 should result in 'abc'.
        """
        inputs = ["26", "abc"]
        output = self.run_exercise(inputs)
        expected_output = "abc"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_case_3(self):
        """
        Test case 3: Encrypting 'Python' with shift amount 1 should result in 'Qzuipo'.
        """
        inputs = ["1", "Python"]
        output = self.run_exercise(inputs)
        expected_output = "Qzuipo"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_case_4(self):
        """
        Test case 4: Encrypting 'Python' with shift amount 3 should result in 'Sbwkrq'.
        """
        inputs = ["3", "Python"]
        output = self.run_exercise(inputs)
        expected_output = "Sbwkrq"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_case_5(self):
        """
        Test case 5: Encrypting 'Python' with shift amount 5 should result in 'Udymts'.
        """
        inputs = ["5", "Python"]
        output = self.run_exercise(inputs)
        expected_output = "Udymts"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)


if __name__ == '__main__':
    unittest.main(testRunner=CustomTestRunner())
