# -*- coding: utf-8 -*-

name = "Feng ruibo"
age = 31
height = 180
height_inch = height * 0.39
weight = 65
weight_pounds = weight * 2.2
eyes = "Black"
teeth = "White"
hair = "Black"

print "Let's talk about %s." % name
print "He's %d centimetres tall." % height
print "He's %d kilometres heavy." % weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (
        age, height, weight, age + height + weight)

#试试%r
print "He's %s pounds heavy." % weight_pounds
print "He's %r pounds heavy." % weight_pounds
