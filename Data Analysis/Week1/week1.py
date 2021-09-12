import numpy as np
import pandas

"""
1. Write a NumPy program to create a 3x4 matrix filled with values from 10 to 21.
"""
print("\n1.")
arr1 = np.arange(10, 22)
arr1 = arr1.reshape(3, 4)

print(arr1)

"""
2. Write a NumPy program to test whether none of the elements of a given array is zero.
"""
print("\n2.")

# Make an array with random values to check for 0's
arr2 = np.random.randint(15, size=10)
print(arr2)

if 0 in arr2:
    print("There are 0's in the array")
else:
    print("There are NO 0's in the array")

"""
3. Write a NumPy program to create an array with the values 1, 7, 13, 105 and determine the size of the memory occupied
by the array. 
"""
print("\n3.")

arr3 = np.array([1, 7, 13, 105])

print("The array occupies", arr3.nbytes, "bytes")
# or
print("The array occupies", arr3.size * arr3.itemsize, "bytes")

"""
4. Write a NumPy program to create an array of the integers from 30 to 70
"""
print("\n4.")

arr4 = np.arange(30, 80, 10)
print(arr4)

"""
5. Write a NumPy program to reverse an array (first element becomes last).
"""
print("\n5.")

arr5 = np.random.randint(15, size=10)
print(arr5)

arr5_rev = arr5[::-1]
print(arr5_rev)

# or

arr5_rev2 = np.flipud(arr5)
print(arr5_rev2)

"""
6.  Write a NumPy program (using numpy) to sum of all the multiples of 3 or 5 below 100. 
"""
print("\n6.")

arr6 = np.arange(100)
print(arr6)

sumOfMultiples = np.sum(np.where((arr6 % 3 == 0) | (arr6 % 5 == 0)))
print(sumOfMultiples)

# We can also save the multiples of 3 and 5 in an array with
arr6_multiples = np.extract((arr6 % 3 == 0) | (arr6 % 5 == 0), arr6)
print(arr6_multiples)
"""
7. Add the following two NumPy arrays and Modify a result array by calculating the square root of each element

arrayOne = numpy.array([[5, 6, 9], [21 ,18, 27]])
arrayTwo = numpy.array([[15 ,33, 24], [4 ,7, 1]])
"""
print("\n7.")
# Renamed the arrays so I am consistent with the naming across all exercises
arr71 = np.array([[5, 6, 9], [21, 18, 27]])
arr72 = np.array([[15, 33, 24], [4, 7, 1]])

arr73 = arr71 + arr72
print(arr73)

arr73 = np.sqrt(arr73)
print(arr73)
"""
8. Create a 5X2 integer array from a range between 100 to 200 such that the difference between each element is 10
"""
print("\n8.")

arr8 = np.arange(100, 200, 10).reshape(5,2)
print(arr8)
"""
9. Following is the 2-D array. Print max from axis 0 and min from axis 1

sampleArray = numpy.array([[34,43,73],[82,22,12],[53,94,66]])
"""
print("\n9.")

arr9 = np.array([[34, 43, 73], [82, 22, 12], [53, 94, 66]])
print(arr9)
print("Max value on axis 0 is", np.max(arr9, axis=0))
print("Min value on axis 1 is", np.min(arr9, axis=1))
"""
10. Sort following NumPy array

by the second row and
by the second column
sampleArray = numpy.array([[34,43,73],[82,22,12],[53,94,66]])
"""
print("\n10.")

arr10 = np.array([[34, 43, 73], [82, 22, 12], [53, 94, 66]])
print(arr10)
print("Sort by second row:\n", arr10[:, arr10[1, :].argsort()])

print("Sort by second column:\n", arr10[arr10[:, 1].argsort()])


