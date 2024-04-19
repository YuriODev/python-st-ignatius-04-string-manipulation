
import unittest
from .test_utils import CustomTestCase, CustomTestRunner

class TestExercise19(CustomTestCase):

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

    def test_case_1(self):
        """
        Description of the test case 1
        """
        inputs = None
        output = self.run_exercise(inputs)
        expected_output = "None"
        self.assertInCustom(expected=expected_output, actual=output, input_value=inputs)

    def test_case_2(self):
        """
        Description of the test case 2
        """
        inputs = None
        output = self.run_exercise(inputs)
        expected_output = "None"
        self.assertInCustom(expected=expected_output, actual=output, input_value=inputs)

    def test_case_3(self):
        """
        Description of the test case 3
        """
        inputs = None
        output = self.run_exercise(inputs)
        expected_output = "None"
        self.assertInCustom(expected=expected_output, actual=output, input_value=inputs)

    def test_case_4(self):
        """
        Description of the test case 4
        """
        inputs = None
        output = self.run_exercise(inputs)
        expected_output = "None"
        self.assertInCustom(expected=expected_output, actual=output, input_value=inputs)

    def test_case_5(self):
        """
        Description of the test case 5
        """
        inputs = None
        output = self.run_exercise(inputs)
        expected_output = "None"
        self.assertInCustom(expected=expected_output, actual=output, input_value=inputs)

if __name__ == '__main__':
    unittest.main(testRunner=CustomTestRunner())
