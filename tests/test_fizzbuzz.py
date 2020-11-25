import fizzbuzz

def test_1_got_1():
    assert fizzbuzz.fizzbuzz(1) == 1

def test_2_return_2():
    assert fizzbuzz.fizzbuzz(2) == 2

def test_3_return_fizz():
    assert fizzbuzz.fizzbuzz(3) == "Fizz"

def test_5_return_buzz():
    assert fizzbuzz.fizzbuzz(5) == "Buzz"

def test_13_return_buzz():
    assert fizzbuzz.fizzbuzz(13) == "Fizz"

def test_15_retrun_fizzbuzz():
    assert fizzbuzz.fizzbuzz(15) == "FizzBuzz"

def test_51_return_fizzbuzz():
    assert fizzbuzz.fizzbuzz(51) == "FizzBuzz"

def test_process_all():
    assert fizzbuzz.process_file("./resource/testData.txt") == """1
2
Fizz
4
Buzz
Fizz
7
8
Fizz
Buzz
11
Fizz
Fizz
14
FizzBuzz
16"""