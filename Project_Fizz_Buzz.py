"""
Write a program that prints the numbers from 1 to 100.
But for multiples of three print "Fizz" instead of the 
number nd for the multiples of five print "Buzz".  For
numbers which are multipls of both three and five print
"FizzBuzz".

1
2
Fizz
4
Buzz
...
14
FizzBuzz
-Function
-Looping
-Conditionals
-Math operators
"""

# for fizzbuzz in range(101):
#     if fizzbuzz % 3 == 0 and fizzbuzz % 5 == 0:
#         print("fizzbuzz")
#         continue
#     elif fizzbuzz % 3 == 0:
#         print("fizz")
#         continue
#     elif fizzbuzz % 5 == 0:
#         print("buzz")
#         continue
#     print(fizzbuzz)



def fizz_buzz(max_num):
  for num in range(1, max_num + 1):
    if num % 3 == 0 and num % 5 == 0:
      print('FizzBuzz')
    elif num % 5 == 0:
      print('Buzz')
    elif num % 3 == 0:
      print('Fizz')
    else:
      print(num)


fizz_buzz(100)
