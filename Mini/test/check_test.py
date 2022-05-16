# importing the required packages
import json
import unittest
from Mini.src import check
from mock import patch




# creating class armstrong number

class ArmstrongNumber(unittest.TestCase):

    def setUp(self):  # Created setup() to assign argument to event
        self.event = {"numbers": [153, 0]}
        self.numbers = 153
        self.sum = 0

    # test lambda handler to check the response

    def test_lambda_handler_true(self):
        result = check.lambda_handler(self.event, )
        data = json.loads(result["body"])  # converting json to python dictionary
        print("data:", data)
        patch('mini.src.check.armstrong', return_value="Passed")
        result = check.armstrong(153, 0)
        assert result == "Passed"

    def test_lambda_handler_false(self):
        result = check.lambda_handler(self.event, )
        data = json.loads(result["body"])  # converting json to python dictionary
        print("data:", data)
        patch('mini.src.check.armstrong', return_value="Error")
        result = check.armstrong(154,0)
        assert result == "Error"

    def test_employee_pass(mocker):
        patch('mini.src.check.employee', return_value={'id':1})
        result = check.employee()
        assert result == {'id': 1}

    def test_employee_fail(mocker):
        patch('mini.src.check.employee', return_value={'id':1})
        result = check.employee()
        assert result == "Error"







if __name__ == '__main__':
    unittest.main()
