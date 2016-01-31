#!/usr/bin/env python
# --*-- encoding: iso-8859-1 --*--

import random

class Locale():
    FR = 'FR'
    EN = 'EN'

class Gender():
    M = 'M'
    F = 'F'
    U = 'U' #Unisex, Adjective works for both gender

class Name():
    def __init__(self, locale, gender, name):
        self.locale = locale
        self.gender = gender
        self.name = name

class Adjective():
    def __init__(self, locale, gender, adjective):
        self.locale = locale
        self.gender = gender
        self.adjective = adjective

class NameStore():
    NAMES = [
             Name(Locale.FR, Gender.M, "pirate"),
             Name(Locale.EN, Gender.M, "pirate"),

             Name(Locale.FR, Gender.M, "hacker"),
             Name(Locale.EN, Gender.M, "hacker"),

             Name(Locale.FR, Gender.F, "patate"),
             Name(Locale.EN, Gender.F, "potatoe"),

             Name(Locale.FR, Gender.F, "huitre"),
             Name(Locale.EN, Gender.F, "oyster"),

             Name(Locale.FR, Gender.M, "canibale"),
             Name(Locale.EN, Gender.M, "Canibal"),

             Name(Locale.FR, Gender.F, "tomate"),
             Name(Locale.EN, Gender.F, "tomatoe"),

             Name(Locale.FR, Gender.M, "conconbre-de-mer"),
             Name(Locale.EN, Gender.M, "sea-cucumber"),

             Name(Locale.FR, Gender.M, "caribou"),
             Name(Locale.EN, Gender.M, "caribou"),

             Name(Locale.FR, Gender.M, "narval"),
             Name(Locale.EN, Gender.M, "narval"),

             Name(Locale.FR, Gender.M, "phacochere"),
             Name(Locale.EN, Gender.M, "warthog"),

             Name(Locale.FR, Gender.F, "guenon"),
             Name(Locale.EN, Gender.M, "monkey"), #no word for 'female monkey'

             Name(Locale.FR, Gender.F, "mouette"),
             Name(Locale.EN, Gender.F, "seagull"),

             Name(Locale.FR, Gender.F, "murene"),
             Name(Locale.EN, Gender.F, "mureen"),

             Name(Locale.FR, Gender.F, "langouste"),
             Name(Locale.EN, Gender.F, "crayfish"),

             Name(Locale.FR, Gender.F, "moule"),
             Name(Locale.EN, Gender.F, "mussel"),

             Name(Locale.FR, Gender.F, "meduse"),
             Name(Locale.EN, Gender.F, "jelly-fish"),

             Name(Locale.FR, Gender.M, "astronaute"),
             Name(Locale.EN, Gender.M, "astronaut"),

             Name(Locale.FR, Gender.M, "ingenieur"),
             Name(Locale.EN, Gender.M, "engineer"),

             Name(Locale.FR, Gender.M, "labrador"),
             Name(Locale.EN, Gender.M, "lab"),

             Name(Locale.FR, Gender.F, "asperge"),
             Name(Locale.EN, Gender.F, "aspergus"),

             Name(Locale.FR, Gender.M, "ivrogne"),
             Name(Locale.EN, Gender.M, "drunk"),

             Name(Locale.FR, Gender.M, "lutin"),
             Name(Locale.EN, Gender.M, "leprechaun"),

             Name(Locale.FR, Gender.F, "fee"),
             Name(Locale.EN, Gender.F, "fairy"),

             Name(Locale.FR, Gender.M, "vampire"),
             Name(Locale.EN, Gender.M, "vampire"),

             Name(Locale.FR, Gender.M, "demon"),
             Name(Locale.EN, Gender.M, "demon"),

             Name(Locale.FR, Gender.F, "crotte"),
             Name(Locale.EN, Gender.F, "poop"),

             Name(Locale.FR, Gender.F, "anguille"),
             Name(Locale.EN, Gender.F, "eel"),

             Name(Locale.FR, Gender.M, "lamproie"),
             Name(Locale.EN, Gender.M, "lamprey"),

             Name(Locale.FR, Gender.M, "murmure"),
             Name(Locale.EN, Gender.M, "murmur"),

             Name(Locale.FR, Gender.M, "alien"),
             Name(Locale.EN, Gender.M, "alien"),

             Name(Locale.FR, Gender.F, "sorciere"),
             Name(Locale.EN, Gender.F, "whitch"),

             Name(Locale.FR, Gender.M, "fantome"),
             Name(Locale.EN, Gender.M, "ghost"),

             Name(Locale.FR, Gender.F, "momie"),
             Name(Locale.EN, Gender.F, "mummy"),

             Name(Locale.FR, Gender.M, "yeti"),
             Name(Locale.EN, Gender.M, "sasquatch"),

             Name(Locale.FR, Gender.M, "papillon"),
             Name(Locale.EN, Gender.M, "butterfly"),

             Name(Locale.FR, Gender.F, "mouche"),
             Name(Locale.EN, Gender.F, "fly"),

             Name(Locale.FR, Gender.M, "dahu"),
             #no english equivalent I think

             Name(Locale.FR, Gender.M, "ogre"),
             Name(Locale.EN, Gender.M, "ogre"),

             Name(Locale.FR, Gender.M, "zombie"),
             Name(Locale.EN, Gender.M, "zombie"),
             ]

class AdjectiveStore():
    ADJECTIVES = [
                  Adjective(Locale.FR, Gender.M, "palpitant"),
                  Adjective(Locale.FR, Gender.F, "palpitante"),
                  Adjective(Locale.EN, Gender.U, "Vibrating"),

                  Adjective(Locale.FR, Gender.M, "pervert"),
                  Adjective(Locale.FR, Gender.F, "perverse"),
                  Adjective(Locale.EN, Gender.U, "pervert"),

                  Adjective(Locale.FR, Gender.U, "sale"),
                  Adjective(Locale.EN, Gender.U, "dirty"),

                  Adjective(Locale.FR, Gender.U, "sauvage"),
                  Adjective(Locale.EN, Gender.U, "wild"),

                  Adjective(Locale.FR, Gender.M, "coquin"),
                  Adjective(Locale.FR, Gender.F, "coquine"),
                  Adjective(Locale.EN, Gender.U, "rascal"), #not sure

                  Adjective(Locale.FR, Gender.U, "magique"),
                  Adjective(Locale.EN, Gender.U, "magical"),

                  Adjective(Locale.FR, Gender.M, "enrichit"),
                  Adjective(Locale.EN, Gender.F, "enrichie"),
                  Adjective(Locale.EN, Gender.U, "enriched"),

                  Adjective(Locale.FR, Gender.U, "ivre"),
                  Adjective(Locale.EN, Gender.U, "drunken"),

                  Adjective(Locale.FR, Gender.M, "croquant"),
                  Adjective(Locale.FR, Gender.F, "croquante"),
                  Adjective(Locale.EN, Gender.U, "crispy"),

                  Adjective(Locale.FR, Gender.M, "extra-moelleux"),
                  Adjective(Locale.FR, Gender.F, "extra-moelleuse"),
                  Adjective(Locale.EN, Gender.U, "extra-soft"),

                  Adjective(Locale.FR, Gender.U, "humide"),
                  Adjective(Locale.EN, Gender.U, "wet"),

                  Adjective(Locale.FR, Gender.U, "moite"),
                  Adjective(Locale.EN, Gender.U, "moist"),

                  Adjective(Locale.FR, Gender.U, "celeste"),
                  Adjective(Locale.EN, Gender.U, "celestial"),

                  Adjective(Locale.FR, Gender.M, "majesteux"),
                  Adjective(Locale.FR, Gender.F, "majestueuse"),
                  Adjective(Locale.EN, Gender.U, "majestuous"),

                  Adjective(Locale.FR, Gender.U, "flasque"),
                  Adjective(Locale.EN, Gender.U, "flask"),

                  Adjective(Locale.FR, Gender.M, "delicieux"),
                  Adjective(Locale.FR, Gender.F, "delicieuse"),
                  Adjective(Locale.EN, Gender.U, "delicious"),

                  Adjective(Locale.FR, Gender.U, "degueulasse"),
                  Adjective(Locale.EN, Gender.U, "disgusting"),

                  Adjective(Locale.FR, Gender.M, "divin"),
                  Adjective(Locale.FR, Gender.F, "divine"),
                  Adjective(Locale.EN, Gender.U, "holy"),

                  Adjective(Locale.FR, Gender.M, "eblouissant"),
                  Adjective(Locale.FR, Gender.F, "eblouissante"),
                  Adjective(Locale.EN, Gender.U, "dazzling"),

                  Adjective(Locale.FR, Gender.M, "exaltant"),
                  Adjective(Locale.FR, Gender.F, "exaltante"),
                  Adjective(Locale.EN, Gender.U, "exalting"),

                  Adjective(Locale.FR, Gender.U, "sexy"),
                  Adjective(Locale.EN, Gender.U, "sexy"),

                  Adjective(Locale.FR, Gender.U, "suave"),
                  Adjective(Locale.EN, Gender.U, "suave"),

                  Adjective(Locale.FR, Gender.M, "somptueux"),
                  Adjective(Locale.FR, Gender.F, "somptueuse"),
                  Adjective(Locale.EN, Gender.U, "somptuous"),

                  Adjective(Locale.FR, Gender.M, "valeureux"),
                  Adjective(Locale.FR, Gender.F, "valeureuse"),
                  Adjective(Locale.EN, Gender.U, "valourous"),

                  Adjective(Locale.FR, Gender.M, "troublant"),
                  Adjective(Locale.FR, Gender.F, "troublante"),
                  Adjective(Locale.EN, Gender.U, "troubling"),

                  Adjective(Locale.FR, Gender.U, "dramatique"),
                  Adjective(Locale.EN, Gender.U, "dramatical"),

                  Adjective(Locale.FR, Gender.U, "supreme"),
                  Adjective(Locale.EN, Gender.U, "supreem"),

                  Adjective(Locale.FR, Gender.M, "libidineux"),
                  Adjective(Locale.FR, Gender.F, "libidineuse"),
                  Adjective(Locale.EN, Gender.U, "libidinous"),

                  Adjective(Locale.FR, Gender.U, "irresistible"),
                  Adjective(Locale.EN, Gender.U, "irresistible"),

                  Adjective(Locale.FR, Gender.U, "insuportable"),
                  Adjective(Locale.EN, Gender.U, "unbereable"),

                  Adjective(Locale.FR, Gender.M, "libidineux"),
                  Adjective(Locale.FR, Gender.F, "libidineuse"),
                  Adjective(Locale.EN, Gender.U, "libidinous"),

                  Adjective(Locale.FR, Gender.M, "infernal"),
                  Adjective(Locale.FR, Gender.F, "infernale"),
                  Adjective(Locale.EN, Gender.U, "infernal"),

                  Adjective(Locale.FR, Gender.U, "horrible"),
                  Adjective(Locale.EN, Gender.U, "horrible"),

                  Adjective(Locale.FR, Gender.U, "grandiose"),
                  Adjective(Locale.EN, Gender.U, "grandiose"),

                  Adjective(Locale.FR, Gender.U, "de-la-mort"),
                  Adjective(Locale.EN, Gender.U, "hell"),

                  Adjective(Locale.FR, Gender.U, "de-combat"),
                  Adjective(Locale.EN, Gender.U, "combat"),

                  Adjective(Locale.FR, Gender.M, "glissant"),
                  Adjective(Locale.FR, Gender.F, "glissante"),
                  Adjective(Locale.EN, Gender.U, "slippery"),

                  Adjective(Locale.FR, Gender.M, "fetard"),
                  Adjective(Locale.FR, Gender.F, "fetarde"),
                  Adjective(Locale.EN, Gender.U, "party"),

                  Adjective(Locale.FR, Gender.U, "ultra-rapide"),
                  Adjective(Locale.EN, Gender.U, "ultra-fast"),

                  Adjective(Locale.FR, Gender.M, "beuglant"),
                  Adjective(Locale.FR, Gender.F, "beuglante"),
                  Adjective(Locale.EN, Gender.U, "loud"),

                  Adjective(Locale.FR, Gender.M, "poilu"),
                  Adjective(Locale.FR, Gender.F, "poilue"),
                  Adjective(Locale.EN, Gender.U, "hairy"),

                  Adjective(Locale.FR, Gender.M, "petillant"),
                  Adjective(Locale.FR, Gender.F, "petillante"),
                  Adjective(Locale.EN, Gender.U, "sparkling"),

                  Adjective(Locale.FR, Gender.M, "silencieux"),
                  Adjective(Locale.FR, Gender.F, "silencieuse"),
                  Adjective(Locale.EN, Gender.U, "silent"),

                  Adjective(Locale.FR, Gender.M, "mou"),
                  Adjective(Locale.FR, Gender.F, "molle"),
                  Adjective(Locale.EN, Gender.U, "soft"),

                  Adjective(Locale.FR, Gender.M, "ecxitant"),
                  Adjective(Locale.FR, Gender.F, "ecxitante"),
                  Adjective(Locale.EN, Gender.U, "exiting"),

                  Adjective(Locale.FR, Gender.U, "de-paques"),
                  Adjective(Locale.EN, Gender.U, "easter"),

                  Adjective(Locale.FR, Gender.U, "herbivore"),
                  Adjective(Locale.EN, Gender.U, "herbivorous"),

                  Adjective(Locale.FR, Gender.M, "furieux"),
                  Adjective(Locale.FR, Gender.F, "furieuse"),
                  Adjective(Locale.EN, Gender.U, "furious"),

                  Adjective(Locale.FR, Gender.M, "mignon"),
                  Adjective(Locale.FR, Gender.F, "mignonne"),
                  Adjective(Locale.EN, Gender.U, "cute"),

                  Adjective(Locale.FR, Gender.U, "sensible"),
                  Adjective(Locale.EN, Gender.U, "sensitive"),

                  Adjective(Locale.FR, Gender.M, "huileux"),
                  Adjective(Locale.FR, Gender.F, "huileuse"),
                  Adjective(Locale.EN, Gender.U, "oily"),

                  Adjective(Locale.FR, Gender.U, "moderne"),
                  Adjective(Locale.EN, Gender.U, "modern"),

                  Adjective(Locale.FR, Gender.U, "enorme"),
                  Adjective(Locale.EN, Gender.U, "enormous"),

                  Adjective(Locale.FR, Gender.M, "juteux"),
                  Adjective(Locale.FR, Gender.F, "juteuse"),
                  Adjective(Locale.EN, Gender.U, "juicy"),

                  Adjective(Locale.FR, Gender.M, "luisant"),
                  Adjective(Locale.FR, Gender.F, "luisante"),
                  Adjective(Locale.EN, Gender.U, "shiny"),

                  Adjective(Locale.FR, Gender.M, "original"),
                  Adjective(Locale.FR, Gender.F, "originale"),
                  Adjective(Locale.EN, Gender.U, "original"),

                  Adjective(Locale.FR, Gender.M, "pourri"),
                  Adjective(Locale.FR, Gender.F, "pourrie"),
                  Adjective(Locale.EN, Gender.U, "rotten"),

                  Adjective(Locale.FR, Gender.M, "savoureux"),
                  Adjective(Locale.FR, Gender.F, "savoureuse"),
                  Adjective(Locale.EN, Gender.U, "tasty")
                  ]

class Generator():
    def __init__(self, locale):
        self.locale = locale

    def _getNamesAccordingToLocale(self):
        localisedNames = []
        for name in NameStore.NAMES:
            if self.locale == name.locale:
                localisedNames.append(name)
        return localisedNames

    def _getAdjectivesAccordingToLocaleAndGender(self, gender):
        localisedCompatibleAdjectives = []
        for a in AdjectiveStore.ADJECTIVES:
            if (self.locale == a.locale) and (a.gender in [gender, Gender.U]):
                localisedCompatibleAdjectives.append(a)
        return localisedCompatibleAdjectives

    def _camelize(self, s):

        def capitalize_nth(s, n):
            return s[:n] + s[n].upper() + s[n+1:]

        def locateDashes(s):
            positions = []
            for i, char in enumerate(s):
                if char == '-':
                    positions.append(i)
            return positions

        dashesPositions = locateDashes(s)
        s = capitalize_nth(s, 0)
        for position in dashesPositions:
            s = capitalize_nth(s, position+1)
        s = s.replace("-", "")
        return s

    def generateName(self):
        names = self._getNamesAccordingToLocale()
        name = random.choice(names)
        adjs = self._getAdjectivesAccordingToLocaleAndGender(name.gender)
        adj = random.choice(adjs)

        if self.locale == Locale.FR:
            return name.name + "-"  + adj.adjective

        if self.locale == Locale.EN:
            return adj.adjective + "-" + name.name

        raise Exception("Locale is unknown")

    def generateNameCamel(self):
        return self._camelize(self.generateName())
