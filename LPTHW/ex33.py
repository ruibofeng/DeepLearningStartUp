# -*- coding: utf-8 -*-

def make_lists(max, step):
    i = 0
    numbers = []
    while i < max:
        print "At the top i is %d" % i
        numbers.append(i)
        
        i = i + step
        print "Numbers now: ", numbers
        print "At the bottom i is %d" % i
    return numbers

#numbers = make_lists(10, 2)
numbers = []
for i in range(0, 10, 2):
    print "At the top i is %d" % i
    numbers.append(i)
    print "Numbers now: ", numbers
    print "At the bottom i is %d" % i

print "The numbers: "

for num in numbers:
    print num


