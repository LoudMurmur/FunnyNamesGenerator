#!/usr/bin/env python
# --*-- encoding: iso-8859-1 --*--
from funnynamegenerator import AdjectiveStore, NameStore, Locale, Gender

def getListDuplicate(data):
    temp = set()
    duplicate = []
    for word in data:
        old_length = len(temp)
        temp.add(word)
        if old_length == len(temp):
            duplicate.append(word)
    return duplicate

def makeNameList(names, locale):
    res = []
    for name in names:
        if name.locale == locale:
            res.append(name.name)
    return res

def makeAdjectiveList(adjectives, locale):
    res = []
    for adj in adjectives:
        if adj.locale == locale:
            res.append(adj.adjective)
    return res

namesFR = makeNameList(NameStore.NAMES, Locale.FR)
adjectivesFR = makeAdjectiveList(AdjectiveStore.ADJECTIVES, Locale.FR)
namesEN = makeNameList(NameStore.NAMES, Locale.EN)
adjectivesEN = makeAdjectiveList(AdjectiveStore.ADJECTIVES, Locale.EN)

print "FR"
print getListDuplicate(namesFR)
print getListDuplicate(adjectivesFR)
print "EN"
print getListDuplicate(namesEN)
print getListDuplicate(adjectivesEN)

