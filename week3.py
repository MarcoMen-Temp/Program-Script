#Marco Men's week 3-Collatz Sequence
raw_input = int(input('Enter a number, please:'))
number = raw_input
steps = 0
while number > 1:
      if number % 2 == 0:
         number = number / 2
         print(number)
      else:
         number = number * 3 + 1
         print(number)

      steps += 1

print('%s' % (raw_input) ,'took {}'.format(steps)) , 'steps'