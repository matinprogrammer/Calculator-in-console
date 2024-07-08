import unittest
from Calculator import Calculator as Cal


class TestCalculator(unittest.TestCase):
    def test_eval_result_simple_operator(self):
        self.assertEqual(Cal.string_to_number_calc("2+2"), 4)
        self.assertEqual(Cal.string_to_number_calc("6+35"), 41)
        self.assertEqual(Cal.string_to_number_calc("6+0"), 6)
        self.assertEqual(Cal.string_to_number_calc("12+35+3+8"), 58)
        self.assertEqual(Cal.string_to_number_calc("6.2+2"), 8.2)

        self.assertEqual(Cal.string_to_number_calc("5-2"), 3)
        self.assertEqual(Cal.string_to_number_calc("16-12"), 4)
        self.assertEqual(Cal.string_to_number_calc("13-20"), -7)
        self.assertEqual(Cal.string_to_number_calc("6-6"), 0)

        self.assertEqual(Cal.string_to_number_calc("5*2"), 10)
        self.assertEqual(Cal.string_to_number_calc("16*10"), 160)
        self.assertEqual(Cal.string_to_number_calc("5*0"), -0)

        self.assertEqual(Cal.string_to_number_calc("8/2"), 4)
        self.assertEqual(Cal.string_to_number_calc("144/12"), 12)
        raised = False
        try:
            Cal.string_to_number_calc("6/0")
        except ZeroDivisionError:
            raised = True
        self.assertTrue(raised, 'Exception not raised')

        self.assertEqual(Cal.string_to_number_calc("8^2"), 64)
        self.assertEqual(Cal.string_to_number_calc("10^0"), 1)

        self.assertEqual(Cal.string_to_number_calc("6.2+2="), 8.2)
        self.assertEqual(Cal.string_to_number_calc("6.2+2=fafa"), 8.2)
        self.assertEqual(Cal.string_to_number_calc("6.2+2=5"), 8.2)

    def test_eval_result_negative_number(self):
        self.assertEqual(Cal.string_to_number_calc("-3+2"), -1)
        self.assertEqual(Cal.string_to_number_calc("-3+6"), 3)

        self.assertEqual(Cal.string_to_number_calc("-9-2"), -11)
        self.assertEqual(Cal.string_to_number_calc("-9-11"), -20)

        self.assertEqual(Cal.string_to_number_calc("-6*2"), -12)

        self.assertEqual(Cal.string_to_number_calc("-9/3"), -3)

        self.assertEqual(Cal.string_to_number_calc("-3^3"), -27)
        self.assertEqual(Cal.string_to_number_calc("-9^2"), 81)

    def test_eval_result_parentheses(self):
        self.assertEqual(Cal.string_to_number_calc("6+4*(3-2)"), 10)
        self.assertEqual(Cal.string_to_number_calc("6+4*(3+(3*2))"), 42)
        self.assertEqual(Cal.string_to_number_calc("2*((3-6)+(6/3)*(-1))"), -10)

    def test_eval_result_letter_operator(self):
        self.assertEqual(Cal.string_to_number_calc("10mod(1+2)"), 1)
        self.assertEqual(Cal.string_to_number_calc("-10mod(1+2)"), -1)
        self.assertEqual(Cal.string_to_number_calc("2log(8*8)"), 6)
        self.assertEqual(Cal.string_to_number_calc("3!-5"), 1)
        self.assertEqual(Cal.string_to_number_calc("5!+(-20)"), 100)
        self.assertEqual(Cal.string_to_number_calc("abs(-20)"), 20)
        self.assertEqual(Cal.string_to_number_calc("abs(20)"), 20)

    def test_eval_result_white_space(self):
        self.assertEqual(Cal.string_to_number_calc("5* 5"), 25)
        self.assertEqual(Cal.string_to_number_calc("a bs ( - 4)"), 4)
        self.assertEqual(Cal.string_to_number_calc("2 l og8"), 3)


if __name__ == '__main__':
    unittest.TextTestRunner()
