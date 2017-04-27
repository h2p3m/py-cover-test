import random

min = 1
max = 6
    
class world:
  def notCovered():
    print 'Hello, world!'
  def reallyNotCovered():
    print 'Hello?'

    roll_again = "yes"

    while roll_again == "yes" or roll_again == "y":
        print "Rolling the dices..."
        print "The values are...."
        print random.randint(min, max)
        print random.randint(min, max)

        roll_again = raw_input("Roll the dices again?")
