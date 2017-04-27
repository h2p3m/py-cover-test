import random
import os
    
class world:
  def notCovered():
    print 'Hello, world!'
  def reallyNotCovered():
    print 'Hello?'

    min = 1
    max = 6
    roll_again = "yes"

    while roll_again == "yes" or roll_again == "y":
        print "Rolling the dices..."
        print "The values are...."
        print random.randint(min, max)
        print random.randint(min, max)

        roll_again = raw_input("Roll the dices again?")
  def deff():
    cur_path = os.getcwd()
    ignore_set = set(["__init__.py", "count_sourcelines.py"])

    loclist = []

    for pydir, _, pyfiles in os.walk(cur_path):
        for pyfile in pyfiles:
            if pyfile.endswith(".py") and pyfile not in ignore_set:
                totalpath = os.path.join(pydir, pyfile)
                loclist.append( ( len(open(totalpath, "r").read().splitlines()),
                                   totalpath.split(cur_path)[1]) )

    for linenumbercount, filename in loclist: 
        print "%05d lines in %s" % (linenumbercount, filename)

    print "\nTotal: %s lines (%s)" %(sum([x[0] for x in loclist]), cur_path)
