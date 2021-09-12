import math

"""
Write a function that converts from kilograms to pounds. Use the scalar conversion of 2.2 lbs per kilogram to make
your conversion. Lastly, print the resulting array of weights in pounds in the main program.
"""


def kgTOlbs(array):
    for i in range(len(array)):
        array[i] *= 2.2


testArray1 = [1, 2, 10, 50, 100]
kgTOlbs(testArray1)
print(testArray1)

""" 
Write a Python function to sum all the numbers in a list
"""


def sumOfElements(array):
    sum = 0
    for i in range(len(array)):
        sum += array[i]
    return sum


testArray2 = [1, 2, 10, 50, 100]
print(sumOfElements(testArray2))

""" 
Write a Python function to check whether a number is in a given range.
"""


def numInRange(num, rangeStart, rangeStop, rangeStep):
    return num in range(rangeStart, rangeStop, rangeStep)


print(numInRange(10, 0, 15, 5))

print(numInRange(2, 1, 15, 2))

""" 
Write a Python function that takes a number as a parameter and check the number is prime or not. Note : A prime
number (or a prime) is a natural number greater than 1 and that has no positive divisors other than 1 and itself. 
"""


def isPrime(num):
    if num < 2:
        return False

    for i in range(2, int(math.sqrt(num))+1):
        if num % i == 0:
            return False
    return True


print(isPrime(7))

print(isPrime(9))


""" 
Write a Python function that checks whether a passed string is palindrome or not.
Note: A palindrome is a word, phrase, or sequence that reads the same backward as forward, e.g., madam or nurses run.
"""


def isPalindrome(word):

    cpyword = word.replace(" ", "")
    reversed = cpyword[::-1]

    return reversed == cpyword;


print(isPalindrome("nurses run"))
print(isPalindrome("not a palindrome"))