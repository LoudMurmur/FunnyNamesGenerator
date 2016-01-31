#!/usr/bin/env python
# --*-- encoding: iso-8859-1 --*--

from funnynamegenerator import Generator, Locale

frGenerator = Generator(Locale.FR)
enGenerator = Generator(Locale.EN)

print "===== FR ====="
for n in range(10):
    print frGenerator.generateName()

print "===== EN ====="
for n in range(10):
    print enGenerator.generateName()

print "===== FR CAMEL ====="
for n in range(10):
    print frGenerator.generateNameCamel()

print "===== EN CAMEL ====="
for n in range(10):
    print enGenerator.generateNameCamel()
