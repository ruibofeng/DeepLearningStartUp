# -*- coding: utf-8 -*-

print "How old are you?",
age = raw_input()
print "How tall are you?",
height = raw_input()
print "How much do you weight?",
weight = raw_input()
#下面是我添加的内容
print "What is your favorite color?",
color = raw_input("--> ")

print "So, you're %r old, %r tall and %r heavy." % (
    age, height, weight)
print "Your favorite color is %r." % color
