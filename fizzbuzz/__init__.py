""" Fizzbuzz """

def process_file(path):
    """process the test data"""
    result = []
    with open(path, "r") as file:
        line = file.readline()
        while line:
            number = int(line)
            result.append(str(fizzbuzz(number)))
            line = file.readline()
    return "\n".join(result)

def __is_divide_by_or_contains(number, divisor):
    return number % divisor == 0 \
        or str(number).find(str(divisor)) != -1

def fizzbuzz(number):
    """fizzbuzz"""
    result = ""
    if __is_divide_by_or_contains(number, 3):
        result += "Fizz"
    if __is_divide_by_or_contains(number, 5):
        result += "Buzz"
    if result != "":
        return result
    return number
