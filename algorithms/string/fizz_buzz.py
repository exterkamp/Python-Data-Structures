def fizz_buzz(n):
    """
    Return the numbers (1,n) but if the number is
    divisible by 3 add "Fizz", if the number is
    divisible by 5, add "Buzz", if it is 
    divisible by both, add "FizzBuzz"

    """
    return [("Fizz" if x % 3 == 0 else "") + ("Buzz" if x % 5 == 0 else "") or str(x) for x in range(1,n+1)]