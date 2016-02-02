#!/usr/bin/env python
# --*-- encoding: iso-8859-1 --*--
from funnynamegenerator import AdjectiveStore, NameStore, Locale, Gender

def getWordsAccordingToGenderAndLocale(words, gender, locale):
    res = []
    for word in words:
        if word.gender == gender and word.locale == locale:
            res.append(word)
    return res

def getWordsValueAccordingToLocale(words, locale):
    res = []
    for word in words:
        if word.locale == locale:
            res.append(word.value)
    return res

def getListDuplicate(data):
    temp = set()
    duplicate = []
    for word in data:
        old_length = len(temp)
        temp.add(word)
        if old_length == len(temp):
            duplicate.append(word)
    return duplicate

def computeData(locale):

    maleNames = getWordsAccordingToGenderAndLocale(NameStore.NAMES, Gender.M, locale)
    femaleNames = getWordsAccordingToGenderAndLocale(NameStore.NAMES, Gender.F, locale)

    maleAdjs = getWordsAccordingToGenderAndLocale(AdjectiveStore.ADJECTIVES, Gender.M, locale)
    femaleAdjs = getWordsAccordingToGenderAndLocale(AdjectiveStore.ADJECTIVES, Gender.F, locale)
    unisexAdjs = getWordsAccordingToGenderAndLocale(AdjectiveStore.ADJECTIVES, Gender.U, locale)

    NamesValue = getWordsValueAccordingToLocale(NameStore.NAMES, locale)
    AdjsValue = getWordsValueAccordingToLocale(AdjectiveStore.ADJECTIVES, locale)

    NamesDuplicate = getListDuplicate(NamesValue)
    AdjsDuplicate = getListDuplicate(AdjsValue)

    print "====================="
    print "======= %s ==========" %locale
    print "====================="

    if len(NamesDuplicate) == 0 and len(AdjsDuplicate) == 0:

        print "no duplicate found :)"
        print "there is"
        print "%s male names and %s female names" %(len(maleNames), len(femaleNames))
        print "%s male adjectives, %s female adjectives and %s unisex adjectives" %(len(maleAdjs),
                                                                                    len(femaleAdjs),
                                                                                    len(unisexAdjs))
        print "so we have"
        print "male names * (male adjs + unisex adjs)"
        print "+"
        print "female names * (female adjs + unisex adjs)"
        print "="
        malePoss = len(maleNames) * (len(maleAdjs) + len(unisexAdjs))
        femalePoss = len(femaleNames) * (len(femaleAdjs) + len(unisexAdjs))
        poss = malePoss + femalePoss
        print "%s possibilites" %poss

    else:

        print "duplicate found, unable to compute stats"
        print "names duplicates :"
        print NamesDuplicate
        print "adjs duplicates :"
        print AdjsDuplicate

computeData(Locale.FR)
computeData(Locale.EN)


