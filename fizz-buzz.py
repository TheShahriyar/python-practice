
input_data = int(input("Please input number : "))

def fizz_buzz (input):
    if input % 3 == 0 and input % 5 == 0:
        result = "It's FizzBuzz"

    elif input % 3 == 0:
        result = "It's Fizz"

    elif input % 5 == 0:
        result = "It's Buzz"

    else:
        result = "NOT FizzBuzz"

    return result


print(fizz_buzz(input_data))

