# GMIT - Data Analytics

## 52167 - Progaramming & Scripting

### **Weekly Assignments** 


#### *Week 1 - fib.py (by Dr. Ian Mcloughlin )*

  > Task - Was to copy and paste a file from GitHub and run it in VS Code
  > File - returns the nth Fibonnaci number, which in fib.py is 28 and returns the 28th fibonnacci number( 317811 )


----------------------------------------------------------//----------------------------------------------------------------------------


#### *Week2* 

> File Used This Week - Same for both assignments
   * fib1-week2.py 
      * In this file I input my first name in an assigned variable
      * The file then runs and assigns the ASCII character codes for the first and last letters 
      * Calculates the sum
      * Returns the nth(=Sum calculated) fibonnaci number
  
  * week2-fib2.py 
      * This is the same as above,but for the surname is used in the variable input( I used my second name )
      
 > Definition of ord()- After googling (perhaps not a proper verb) " ord () ",which lead me to sites such as GeeksforGeek.org and stackoverflow. The definition is the inverse of Chr() -Return the Unicode code point for one character string . Example: on my first name ,the first letter is an " M " with an Unicode number of 77; and the last letter " o " with the value of 111. The sum of the 2 is 188 ( fib1.py )

My second name  " Filipe ", the same principle applies . Unicode values for :

- " F " is 70 and " e " is 101. The sum of both is 171 ( fib2.py )

I used the following site https://unicode-table.com/en/#004D , to confirm the values ( defined as HTML - code )
      
      
----------------------------------------------------------//----------------------------------------------------------------------------
           
#### *Week 3 - week3.py*

File - Returns the Collatz Sequence
> Collatz Sequence :
> A random number runs a backwards sequence and ends always in 1
   > Two Conditions For This to happen:
* If an odd nunmber --> divide by 3 and add 1
* If even number --> divide by 2

I also included the number of steps(counted) that it took for the sequence to run until it reaches 1 

According to "Numberphile" on YouTube, the highest number(the one that takes the highest number of steps to reach to 1) is 63,728,127( 949 steps to reach to 1 )


---------------------------------------------------------//-----------------------------------------------------------------------------


#### *Week 4 - <ProjectEuler -Prob5> Problem5.py *

> This file is not exactly what I was going for,but in the process of writing it I improved my knowledge of Python Language:
* How to create a factorisation list of a number
* Append elements in lists
* Import functions and use some of their tools(i.e.math function with pow or sqrt)
* Perform multiplication of all elements within a list 

> The other file problem5.py is not written by me,but I decided to keep it for future reference and as an aspiration to one day write similar code




---------------------------------------------------------//-----------------------------------------------------------------------------


#### *Week 5* - <DataSet>
  > **DataSet** is a folder that contains **open.py** (which is the one performed by Lecturer on video lecture)
  
  > The **format.py** is the file for the assignment,with top row,numerical values formatted(column spaced and aligned with the top) and separator('|'). My most recent change was based on: "https://www.neuraldesigner.com/learning/examples/iris_flowers_classification",for the headings,with the measuring metric in brackets
  
  
  -------------------------------------------------------//-----------------------------------------------------------------------------
  
  
#### *Week 6 - factorials.py*


> Factorial of a number is number multiplication sequence,that starts from the number and multiplies by all the previous numbers down to 1.
   > Example:
   
   * 5! = 5x4x3x2x1
   * But 0! = 1(not 0)
   
> This algorithm can be written using recursion(a function that returns to itself until the condition is no longer satisfied-exiting the function)
