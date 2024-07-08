from re import findall
from math import log, factorial


class Calculator:
    def __init__(self):
        self._string_data = None
        self._number_data = None

    def display(self) -> [float, int]:
        try:
            self.number_data = Calculator.string_to_number_calc(self.string_data)
        except ZeroDivisionError:
            return "zero division error"
        except (ValueError, RuntimeError) as e:
            return str(e)

        return int(self.number_data) if self.number_data.is_integer() else self.number_data

    @staticmethod
    def string_to_number_calc(string_data: str) -> float:
        if not isinstance(string_data, str):
            raise TypeError("invalid string")

        def list_to_number_calc(list_data: list) -> float:

            for i, element in enumerate(list_data):
                if element == "-":
                    list_data[i + 1] = -1 * float(list_data[i + 1])
                    if i != 0 and list_data[i-1] != "(":
                        list_data[i] = "+"
                    else:
                        del list_data[i]

            op_priority = ("(", "abs", "mod", "log", "!", "^", "*", "/", "+", "-")
            for op in op_priority:
                if op in list_data:
                    index = list_data.index(op)

                    previous_data_in_list = None
                    next_data_in_list = None
                    if not (op in ["("]):
                        if not (op in ["abs"]):
                            previous_data_in_list = float(list_data[index - 1])
                        if not (op in ["!"]):
                            next_data_in_list = float(list_data[index + 1])
                    match op:
                        case '+':
                            list_data[index] = previous_data_in_list + next_data_in_list
                        case '-':
                            list_data[index] = previous_data_in_list - next_data_in_list
                        case '*':
                            list_data[index] = previous_data_in_list * next_data_in_list
                        case '/':
                            list_data[index] = previous_data_in_list / next_data_in_list
                        case '^':
                            list_data[index] = previous_data_in_list ** next_data_in_list
                        case '(':
                            j = 1
                            last_parentheses = None
                            for i, element in enumerate(list_data[index + 1:]):
                                if element == ")":
                                    j -= 1
                                if element == "(":
                                    j += 1
                                if j == 0:
                                    last_parentheses = i + index + 1
                                    break

                            list_data[index] = list_to_number_calc(list_data[index + 1: last_parentheses])
                            del list_data[index + 1:last_parentheses + 1]
                        case 'mod':
                            coefficient = 1
                            if previous_data_in_list < 0:
                                coefficient = -1
                            list_data[index] = (previous_data_in_list * coefficient % next_data_in_list) * coefficient
                        case 'log':
                            list_data[index] = log(next_data_in_list, previous_data_in_list)
                        case '!':
                            list_data[index] = float(factorial(int(previous_data_in_list)))
                        case 'abs':
                            list_data[index] = abs(next_data_in_list)

                    if not (op in ["("]):
                        if not (op in ["!"]):
                            del list_data[index + 1]
                        if not (op in ["abs"]):
                            del list_data[index - 1]
                    return list_to_number_calc(list_data)
            else:
                if len(list_data) != 1:
                    raise RuntimeError("can't process input data")
                return float(list_data[0])

        string_data = "".join(findall(r'\S*', string_data)).rstrip("=")
        number_op_list = findall(r'[\d.]+|[()]|[a-zA-Z]+|\W', string_data)
        if string_data == "":
            raise ValueError("data cant is empty")

        if number_op_list.count("(") != number_op_list.count(")"):
            raise RuntimeError("invalid parentheses")

        return list_to_number_calc(number_op_list)

    @property
    def string_data(self):
        return self._string_data

    @string_data.setter
    def string_data(self, string_data):
        if not isinstance(string_data, str):
            raise ValueError("Invalid string")

        self._string_data = string_data

    @string_data.deleter
    def string_data(self):
        raise RuntimeError("cant delete this attribute")

    @property
    def number_data(self) -> float:
        return self._number_data

    @number_data.setter
    def number_data(self, number_data):
        if not (isinstance(number_data, float)):
            raise ValueError("Invalid float")

        self._number_data = number_data

    @number_data.deleter
    def number_data(self):
        raise RuntimeError("cant delete this attribute")


def main():
    data = input('Enter your string: ')

    calculator = Calculator()
    calculator.string_data = data

    print(f"your result is: {calculator.display()}")
    # print(f"your result with static is: {calculator.string_to_number_calc(data)}")


if __name__ == '__main__':
    print("hi to this calculator\n"
          "operator is 'add: +', 'sub: -', 'mul: *', 'divide: /'"
          ", 'pow: ^', 'mod: mod', 'log: log', 'factorial: !', 'abs: abs' \n"
          "example: 2log8 = 3")
    while True:
        main()
