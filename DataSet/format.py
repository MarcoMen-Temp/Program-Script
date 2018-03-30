"""Marco Men - Exercise 5 (Format)
 """ 
import csv
#Adapted from:'https://docs.python.org/3/tutorial/controlflow.html#more-on-defining-functions(section 4.7.3-Concat(earth,mars,venus),with "|"" as separator)
def concat(*args, sep= "| "):
      return sep.join(args)


print(concat("Sepal Length(cm)", "Sepal Width(cm)","Petal Length(cm)","Petal Width(cm)"))

#Adapted from StackOverFlow: 'Formatting Output of CSV file in Python'
with open("iris.csv") as f:
      reader = csv.reader(f)
      for row in reader:
            print('{:>15} | {:>14} | {:>15} | {:>14}' .format(*row))
#The numeric values' separators were to be used to help align them to the args on top