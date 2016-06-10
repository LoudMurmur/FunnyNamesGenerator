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
    def __init__(self, locale, gender, value):
        self.locale = locale
        self.gender = gender
        self.value = value

class Adjective():
    def __init__(self, locale, gender, value, invert=False):
        self.locale = locale
        self.gender = gender
        self.value = value
        self.invert = invert

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
             Name(Locale.EN, Gender.M, "canibal"),

             Name(Locale.FR, Gender.F, "tomate"),
             Name(Locale.EN, Gender.F, "tomatoe"),

             Name(Locale.FR, Gender.M, "conconbre-de-mer"),
             Name(Locale.EN, Gender.M, "sea-cucumber"),

             Name(Locale.FR, Gender.M, "caribou"),
             Name(Locale.EN, Gender.M, "caribou"),

             Name(Locale.FR, Gender.M, "narval"),
             Name(Locale.EN, Gender.M, "narwhal"),

             Name(Locale.FR, Gender.M, "phacochere"),
             Name(Locale.EN, Gender.M, "warthog"),

             Name(Locale.FR, Gender.F, "guenon"),
             #no word for 'female monkey'
             Name(Locale.EN, Gender.M, "monkey"),

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
             Name(Locale.EN, Gender.M, "labrador"),

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

             Name(Locale.FR, Gender.M, "cyborg"),
             Name(Locale.EN, Gender.M, "cyborg"),

             Name(Locale.FR, Gender.M, "robot"),
             Name(Locale.EN, Gender.M, "robot"),

             Name(Locale.FR, Gender.M, "chevalier"),
             Name(Locale.EN, Gender.M, "knight"),

             Name(Locale.FR, Gender.F, "amazone"),
             Name(Locale.EN, Gender.F, "amazon"),

             Name(Locale.FR, Gender.M, "guerrier"),
             Name(Locale.EN, Gender.M, "warrior"),

             Name(Locale.FR, Gender.F, "licorne"),
             Name(Locale.EN, Gender.F, "unicorne"),

             Name(Locale.FR, Gender.F, "loutre"),
             Name(Locale.EN, Gender.F, "otter"),

             Name(Locale.FR, Gender.M, "phoque"),
             Name(Locale.EN, Gender.M, "sea-lion"),

             Name(Locale.FR, Gender.M, "hypocondriaque"),
             Name(Locale.EN, Gender.M, "hypocondriac"),

             Name(Locale.FR, Gender.M, "mage"),
             Name(Locale.EN, Gender.M, "sorcerer"),

             Name(Locale.FR, Gender.M, "cul-terreux"),
             Name(Locale.FR, Gender.M, "beauf"),
             Name(Locale.EN, Gender.M, "redneck"),
             Name(Locale.EN, Gender.M, "hillbilly"),

             Name(Locale.FR, Gender.M, "colloc"),
             Name(Locale.EN, Gender.M, "roomate"),

             Name(Locale.FR, Gender.F, "bacterie"),
             Name(Locale.EN, Gender.F, "bacteria"),

             Name(Locale.FR, Gender.M, "virus"),
             Name(Locale.EN, Gender.M, "virus"),

             Name(Locale.FR, Gender.M, "mutant"),
             Name(Locale.EN, Gender.M, "mutant"),

             Name(Locale.FR, Gender.M, "cafard"),
             Name(Locale.EN, Gender.M, "cockroach"),

             Name(Locale.FR, Gender.M, "poireau"),
             Name(Locale.EN, Gender.M, "leek"),

             Name(Locale.FR, Gender.F, "pintade"),
             Name(Locale.EN, Gender.F, "guinea-fowl"),

             Name(Locale.FR, Gender.F, "mite"),
             Name(Locale.EN, Gender.F, "moth"),

             Name(Locale.FR, Gender.F, "fougere"),
             Name(Locale.EN, Gender.F, "fern"),

             Name(Locale.FR, Gender.F, "plante-verte"),
             Name(Locale.EN, Gender.F, "house-plant"),

             Name(Locale.FR, Gender.M, "ornithorynque"),
             Name(Locale.EN, Gender.M, "platypus"),

             Name(Locale.FR, Gender.M, "pingouin"),
             Name(Locale.EN, Gender.M, "penguin"),

             Name(Locale.FR, Gender.F, "truie"),
             Name(Locale.FR, Gender.F, "cochone"),
             Name(Locale.EN, Gender.F, "sow"),

             Name(Locale.FR, Gender.M, "mogwai"),
             Name(Locale.FR, Gender.M, "gremlin"),
             Name(Locale.EN, Gender.M, "mogwai"),
             Name(Locale.EN, Gender.M, "gremlin"),

             Name(Locale.FR, Gender.M, "poney"),
             Name(Locale.EN, Gender.M, "pony"),

             Name(Locale.FR, Gender.M, "reve"),
             Name(Locale.EN, Gender.M, "dream"),

             Name(Locale.FR, Gender.M, "barman"),
             Name(Locale.EN, Gender.M, "barman"),

             Name(Locale.FR, Gender.M, "dinosaure"),
             Name(Locale.EN, Gender.M, "dinosaur"),

             Name(Locale.FR, Gender.M, "poulpe"),
             Name(Locale.EN, Gender.M, "octopus"),

             Name(Locale.FR, Gender.M, "crabe"),
             Name(Locale.EN, Gender.M, "crab"),

             Name(Locale.FR, Gender.M, "vieillard"),
             Name(Locale.FR, Gender.F, "vieillarde"),
             Name(Locale.EN, Gender.M, "geezer"),
             Name(Locale.EN, Gender.F, "hag"),

             Name(Locale.FR, Gender.F, "carpe"),
             Name(Locale.EN, Gender.F, "carp"),

             Name(Locale.FR, Gender.M, "dictateur"),
             Name(Locale.EN, Gender.M, "dictator"),

             Name(Locale.FR, Gender.F, "stripteaseuse"),
             Name(Locale.EN, Gender.F, "stripper"),

             Name(Locale.FR, Gender.F, "creature"),
             Name(Locale.EN, Gender.F, "creature"),

             Name(Locale.FR, Gender.M, "centaure"),
             Name(Locale.EN, Gender.M, "centaure"),

             Name(Locale.FR, Gender.M, "satyre"),
             Name(Locale.EN, Gender.M, "satyr"),

             Name(Locale.FR, Gender.M, "cyclope"),
             Name(Locale.EN, Gender.M, "cyclope"),

             Name(Locale.FR, Gender.M, "dieu"),
             Name(Locale.EN, Gender.M, "god"),

             Name(Locale.FR, Gender.M, "gobelin"),
             Name(Locale.EN, Gender.M, "gobelin"),

             Name(Locale.FR, Gender.M, "geant"),
             Name(Locale.EN, Gender.M, "giant"),

             Name(Locale.FR, Gender.M, "eunuque"),
             Name(Locale.EN, Gender.M, "eunuch"),

             Name(Locale.FR, Gender.M, "lapin"),
             Name(Locale.EN, Gender.M, "rabbit"),

             Name(Locale.FR, Gender.M, "leviathan"),
             Name(Locale.EN, Gender.M, "leviathan"),

             Name(Locale.FR, Gender.M, "minotaure"),
             Name(Locale.EN, Gender.M, "minotaure"),

             Name(Locale.FR, Gender.M, "monster"),
             Name(Locale.EN, Gender.M, "monster"),

             Name(Locale.FR, Gender.M, "caniche"),
             Name(Locale.EN, Gender.F, "poodle"),

             Name(Locale.FR, Gender.M, "titan"),
             Name(Locale.EN, Gender.M, "titan"),

             Name(Locale.FR, Gender.M, "saumon"),
             Name(Locale.EN, Gender.M, "salmon"),

             Name(Locale.FR, Gender.M, "troll"),
             Name(Locale.EN, Gender.M, "troll"),

             Name(Locale.FR, Gender.F, "valkyrie"),
             Name(Locale.EN, Gender.F, "valkyrie"),

             Name(Locale.FR, Gender.M, "pokemon"),
             Name(Locale.EN, Gender.M, "pokemon"),

             Name(Locale.FR, Gender.M, "arbre"),
             Name(Locale.EN, Gender.M, "tree"),

             Name(Locale.FR, Gender.M, "faisan"),
             Name(Locale.EN, Gender.M, "pheasant"),

             Name(Locale.FR, Gender.M, "champignon"),
             Name(Locale.EN, Gender.M, "mushroom"),

             Name(Locale.FR, Gender.M, "shaman"),
             Name(Locale.EN, Gender.M, "shaman"),

             Name(Locale.FR, Gender.M, "chimere"),
             Name(Locale.EN, Gender.M, "chimera")
             ]

class AdjectiveStore():
    ADJECTIVES = [
                  Adjective(Locale.FR, Gender.M, "palpitant"),
                  Adjective(Locale.FR, Gender.F, "palpitante"),
                  Adjective(Locale.EN, Gender.U, "palpitating"),

                  Adjective(Locale.FR, Gender.M, "pulsant"),
                  Adjective(Locale.FR, Gender.F, "pulsante"),
                  Adjective(Locale.EN, Gender.U, "pulsating"),

                  Adjective(Locale.FR, Gender.M, "vibrant"),
                  Adjective(Locale.FR, Gender.F, "vibrante"),
                  Adjective(Locale.EN, Gender.U, "vibrating"),

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
                  Adjective(Locale.FR, Gender.F, "enrichie"),
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
                  Adjective(Locale.EN, Gender.U, "flacid"),

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
                  Adjective(Locale.EN, Gender.U, "tasty"),

                  Adjective(Locale.FR, Gender.M, "revigorant"),
                  Adjective(Locale.FR, Gender.F, "revigorante"),
                  Adjective(Locale.EN, Gender.U, "invigorating"),

                  Adjective(Locale.FR, Gender.M, "rafraichissant"),
                  Adjective(Locale.FR, Gender.F, "rafraichissante"),
                  Adjective(Locale.EN, Gender.U, "refreshing"),

                  Adjective(Locale.FR, Gender.U, "invisible"),
                  Adjective(Locale.EN, Gender.U, "invinsible"),

                  Adjective(Locale.FR, Gender.U, "hipster"),
                  Adjective(Locale.EN, Gender.U, "hipster"),

                  Adjective(Locale.FR, Gender.U, "hippie"),
                  Adjective(Locale.EN, Gender.U, "hippy"),

                  Adjective(Locale.FR, Gender.U, "photogenique"),
                  Adjective(Locale.EN, Gender.U, "photogenic"),

                  Adjective(Locale.FR, Gender.U, "debile"),
                  Adjective(Locale.EN, Gender.U, "retarded"),

                  Adjective(Locale.FR, Gender.U, "informe"),
                  Adjective(Locale.EN, Gender.U, "malformed"),

                  Adjective(Locale.FR, Gender.M, "brulant"),
                  Adjective(Locale.FR, Gender.F, "brulante"),
                  Adjective(Locale.EN, Gender.U, "red-hot"),

                  Adjective(Locale.FR, Gender.M, "radioactif"),
                  Adjective(Locale.FR, Gender.F, "radioactive"),
                  Adjective(Locale.EN, Gender.U, "radioactive"),

                  Adjective(Locale.FR, Gender.M, "phosphorescent"),
                  Adjective(Locale.FR, Gender.F, "phosphorescente"),
                  Adjective(Locale.EN, Gender.U, "glowing"),

                  Adjective(Locale.FR, Gender.M, "endormit"),
                  Adjective(Locale.FR, Gender.F, "endormie"),
                  Adjective(Locale.EN, Gender.U, "sleeping"),

                  Adjective(Locale.FR, Gender.U, "de-la-montagne"),
                  Adjective(Locale.EN, Gender.U, "mountain"),

                  Adjective(Locale.FR, Gender.M, "pouilleux"),
                  Adjective(Locale.FR, Gender.F, "pouilleuse"),
                  Adjective(Locale.EN, Gender.U, "lousy"),

                  Adjective(Locale.FR, Gender.M, "aguicheur"),
                  Adjective(Locale.FR, Gender.F, "aguicheuse"),
                  Adjective(Locale.EN, Gender.U, "teasing"),

                  Adjective(Locale.FR, Gender.M, "ruisselant"),
                  Adjective(Locale.FR, Gender.F, "ruisselante"),
                  #no english

                  Adjective(Locale.FR, Gender.U, "anemique"),
                  Adjective(Locale.EN, Gender.U, "anemic"),

                  Adjective(Locale.FR, Gender.U, "lubrique"),
                  Adjective(Locale.EN, Gender.U, "lewd"),

                  Adjective(Locale.FR, Gender.U, "sanguinaire"),
                  Adjective(Locale.EN, Gender.U, "bloodthirsty"),

                  Adjective(Locale.FR, Gender.M, "vicieux"),
                  Adjective(Locale.FR, Gender.F, "vicieuse"),
                  Adjective(Locale.EN, Gender.U, "vicious"),

                  Adjective(Locale.FR, Gender.M, "pernicieux"),
                  Adjective(Locale.FR, Gender.F, "pernicieuse"),
                  Adjective(Locale.EN, Gender.U, "pernicious"),

                  Adjective(Locale.FR, Gender.M, "morveux"),
                  Adjective(Locale.FR, Gender.F, "morveuse"),
                  Adjective(Locale.EN, Gender.U, "snotty"),

                  Adjective(Locale.FR, Gender.M, "dodu"),
                  Adjective(Locale.FR, Gender.F, "dodue"),
                  Adjective(Locale.EN, Gender.U, "plump"),

                  Adjective(Locale.FR, Gender.M, "hysterique"),
                  Adjective(Locale.EN, Gender.U, "hysteric"),

                  Adjective(Locale.FR, Gender.M, "baveux"),
                  Adjective(Locale.FR, Gender.F, "baveuse"),
                  Adjective(Locale.EN, Gender.U, "drooling"),

                  Adjective(Locale.FR, Gender.M, "ecoeurant"),
                  Adjective(Locale.FR, Gender.F, "ecoeurante"),
                  Adjective(Locale.EN, Gender.U, "sickening"),

                  Adjective(Locale.FR, Gender.M, "velu"),
                  Adjective(Locale.FR, Gender.F, "velue"),
                  #no english, already used hairy for poilu

                  Adjective(Locale.FR, Gender.M, "odorant"),
                  Adjective(Locale.FR, Gender.F, "odorante"),
                  Adjective(Locale.EN, Gender.U, "smelly"),

                  Adjective(Locale.FR, Gender.M, "moisi"),
                  Adjective(Locale.FR, Gender.F, "moisie"),
                  Adjective(Locale.EN, Gender.U, "mouldy"),

                  Adjective(Locale.FR, Gender.M, "fletri"),
                  Adjective(Locale.FR, Gender.F, "fletrie"),
                  Adjective(Locale.EN, Gender.U, "withered"),

                  Adjective(Locale.FR, Gender.U, "reveche"),
                  Adjective(Locale.EN, Gender.U, "surly"), #not sure

                  Adjective(Locale.FR, Gender.U, "putride"),
                  Adjective(Locale.EN, Gender.U, "putrid"),

                  Adjective(Locale.FR, Gender.U, "fetide"),
                  Adjective(Locale.EN, Gender.U, "fetid"),

                  Adjective(Locale.FR, Gender.U, "au-chocolat"),
                  Adjective(Locale.EN, Gender.U, "chocolate"),

                  Adjective(Locale.FR, Gender.U, "indomptable"),
                  Adjective(Locale.EN, Gender.U, "indomptable"),

                  Adjective(Locale.FR, Gender.U, "romantique"),
                  Adjective(Locale.EN, Gender.U, "romantic"),

                  Adjective(Locale.FR, Gender.M, "calin"),
                  Adjective(Locale.FR, Gender.F, "caline"),
                  Adjective(Locale.EN, Gender.U, "huggy"),

                  Adjective(Locale.FR, Gender.M, "farfelu"),
                  Adjective(Locale.FR, Gender.F, "farfelue"),
                  Adjective(Locale.EN, Gender.U, "eccentric"),

                  Adjective(Locale.FR, Gender.M, "rutilant"),
                  Adjective(Locale.FR, Gender.F, "rutilante"),
                  #no english, already used sparkling elsewhere

                  Adjective(Locale.FR, Gender.U, "sous-acide"),
                  Adjective(Locale.EN, Gender.U, "lsd"),

                  Adjective(Locale.FR, Gender.U, "sous-champi"),
                  Adjective(Locale.EN, Gender.U, "tripping"),

                  Adjective(Locale.FR, Gender.U, "revolutionnaire"),
                  Adjective(Locale.EN, Gender.U, "revolutionnary"),

                  Adjective(Locale.FR, Gender.M, "brutal"),
                  Adjective(Locale.FR, Gender.F, "brutale"),
                  Adjective(Locale.EN, Gender.U, "brutal"),

                  Adjective(Locale.FR, Gender.U, "erotique"),
                  Adjective(Locale.EN, Gender.U, "erotic"),

                  Adjective(Locale.FR, Gender.U, "porno"),
                  Adjective(Locale.EN, Gender.U, "porn"),

                  Adjective(Locale.FR, Gender.M, "interdit"),
                  Adjective(Locale.FR, Gender.F, "interdite"),
                  Adjective(Locale.EN, Gender.U, "forbidden"),

                  Adjective(Locale.FR, Gender.U, "ionique"),
                  Adjective(Locale.EN, Gender.U, "ionic"),

                  Adjective(Locale.FR, Gender.U, "metallique"),
                  Adjective(Locale.EN, Gender.U, "metallic"),

                  Adjective(Locale.FR, Gender.U, "ultra-sonique"),
                  Adjective(Locale.EN, Gender.U, "ultra-sonic"),

                  Adjective(Locale.FR, Gender.U, "tyrannique"),
                  Adjective(Locale.EN, Gender.U, "tyrannic"),

                  Adjective(Locale.FR, Gender.U, "toxique"),
                  Adjective(Locale.EN, Gender.U, "toxic"),

                  Adjective(Locale.FR, Gender.U, "chimique"),
                  Adjective(Locale.EN, Gender.U, "chimical"),

                  Adjective(Locale.FR, Gender.U, "sadique"),
                  Adjective(Locale.EN, Gender.U, "sadistic"),

                  Adjective(Locale.FR, Gender.U, "psychotique"),
                  Adjective(Locale.EN, Gender.U, "psychotic"),

                  Adjective(Locale.FR, Gender.U, "psychopathe"),
                  Adjective(Locale.EN, Gender.U, "psychopathic"),

                  Adjective(Locale.FR, Gender.U, "pudique"),
                  Adjective(Locale.EN, Gender.U, "pudic"),

                  Adjective(Locale.FR, Gender.U, "psychedelique"),
                  Adjective(Locale.EN, Gender.U, "psychedelic"),

                  Adjective(Locale.FR, Gender.U, "prophetique"),
                  Adjective(Locale.EN, Gender.U, "prophetic"),

                  Adjective(Locale.FR, Gender.U, "prehistorique"),
                  Adjective(Locale.EN, Gender.U, "prehistoric"),

                  Adjective(Locale.FR, Gender.U, "prophethique"),
                  Adjective(Locale.EN, Gender.U, "prophethic"),

                  Adjective(Locale.FR, Gender.U, "mystique"),
                  Adjective(Locale.EN, Gender.U, "mystical"),

                  Adjective(Locale.FR, Gender.M, "nauseabon"),
                  Adjective(Locale.FR, Gender.F, "nauseabonde"),
                  Adjective(Locale.EN, Gender.U, "foul"),

                  Adjective(Locale.FR, Gender.U, "metaphysique"),
                  Adjective(Locale.EN, Gender.U, "metaphysical"),

                  Adjective(Locale.FR, Gender.U, "mecanique"),
                  Adjective(Locale.EN, Gender.U, "mecanic"),

                  Adjective(Locale.FR, Gender.U, "malefique"),
                  Adjective(Locale.EN, Gender.U, "maleficient"),

                  Adjective(Locale.FR, Gender.U, "microscopique"),
                  Adjective(Locale.EN, Gender.U, "microscopic"),

                  Adjective(Locale.FR, Gender.U, "lunatique"),
                  Adjective(Locale.EN, Gender.U, "lunatic"),

                  Adjective(Locale.FR, Gender.U, "atomique"),
                  Adjective(Locale.EN, Gender.U, "atomic"),

                  Adjective(Locale.FR, Gender.U, "nucleaire"),
                  Adjective(Locale.EN, Gender.U, "nuclear"),

                  Adjective(Locale.FR, Gender.U, "hypnotique"),
                  Adjective(Locale.EN, Gender.U, "hypnotic"),

                  Adjective(Locale.FR, Gender.U, "honorifique"),
                  Adjective(Locale.EN, Gender.U, "honorifical"),

                  Adjective(Locale.FR, Gender.U, "heroique"),
                  Adjective(Locale.EN, Gender.U, "heroic"),

                  Adjective(Locale.FR, Gender.U, "heretique"),
                  Adjective(Locale.EN, Gender.U, "heretic"),

                  Adjective(Locale.FR, Gender.U, "gothique"),
                  Adjective(Locale.EN, Gender.U, "goth"),

                  Adjective(Locale.FR, Gender.U, "cybernetique"),
                  Adjective(Locale.EN, Gender.U, "cybernetic"),

                  Adjective(Locale.FR, Gender.U, "bionique"),
                  Adjective(Locale.EN, Gender.U, "bionic"),

                  Adjective(Locale.FR, Gender.U, "chaotique"),
                  Adjective(Locale.FR, Gender.U, "du-chaos"),
                  Adjective(Locale.EN, Gender.U, "chaotic"),

                  Adjective(Locale.FR, Gender.U, "quantique"),
                  Adjective(Locale.EN, Gender.U, "quantic"),

                  Adjective(Locale.FR, Gender.U, "antique"),
                  Adjective(Locale.EN, Gender.U, "antic"),

                  Adjective(Locale.FR, Gender.U, "amnesique"),
                  Adjective(Locale.EN, Gender.U, "amnesic"),

                  Adjective(Locale.FR, Gender.U, "aerodynamique"),
                  Adjective(Locale.EN, Gender.U, "aerodynamic"),

                  Adjective(Locale.FR, Gender.U, "imaginaire"),
                  Adjective(Locale.EN, Gender.U, "imaginary"),

                  Adjective(Locale.FR, Gender.M, "primordial"),
                  Adjective(Locale.FR, Gender.F, "primordiale"),
                  Adjective(Locale.EN, Gender.U, "primordial"),

                  Adjective(Locale.FR, Gender.M, "abyssal"),
                  Adjective(Locale.FR, Gender.F, "abyssale"),
                  Adjective(Locale.EN, Gender.U, "abyssal"),

                  Adjective(Locale.FR, Gender.M, "ancestral"),
                  Adjective(Locale.FR, Gender.F, "ancestrale"),
                  Adjective(Locale.EN, Gender.U, "ancestral"),

                  Adjective(Locale.FR, Gender.M, "anormal"),
                  Adjective(Locale.FR, Gender.F, "anormale"),
                  #nope,

                  Adjective(Locale.FR, Gender.M, "astral"),
                  Adjective(Locale.FR, Gender.F, "astrale"),
                  Adjective(Locale.EN, Gender.U, "astral"),

                  Adjective(Locale.FR, Gender.M, "ceremonial"),
                  Adjective(Locale.FR, Gender.F, "ceremoniale"),
                  Adjective(Locale.EN, Gender.U, "ceremonial"),

                  Adjective(Locale.FR, Gender.M, "colossal"),
                  Adjective(Locale.FR, Gender.F, "colossale"),
                  Adjective(Locale.EN, Gender.U, "colossal"),

                  Adjective(Locale.FR, Gender.M, "neural"),
                  Adjective(Locale.FR, Gender.F, "neurale"),
                  Adjective(Locale.EN, Gender.U, "neural"),

                  Adjective(Locale.FR, Gender.M, "spatial"),
                  Adjective(Locale.FR, Gender.F, "spatiale"),
                  Adjective(Locale.EN, Gender.U, "spatial"),

                  Adjective(Locale.FR, Gender.M, "sideral"),
                  Adjective(Locale.FR, Gender.F, "siderale"),
                  Adjective(Locale.EN, Gender.U, "sideral"),

                  Adjective(Locale.FR, Gender.M, "spectral"),
                  Adjective(Locale.FR, Gender.F, "spectrale"),
                  Adjective(Locale.EN, Gender.U, "spectral"),

                  Adjective(Locale.FR, Gender.U, "funeste"),
                  Adjective(Locale.EN, Gender.U, "disastrous"),

                  Adjective(Locale.FR, Gender.M, "urbain"),
                  Adjective(Locale.FR, Gender.F, "urbaine"),
                  Adjective(Locale.EN, Gender.U, "urban"),

                  Adjective(Locale.FR, Gender.M, "miteu"),
                  Adjective(Locale.FR, Gender.F, "miteuse"),
                  #nope

                  Adjective(Locale.FR, Gender.M, "moyenageux"),
                  Adjective(Locale.FR, Gender.F, "moyenageuse"),
                  Adjective(Locale.EN, Gender.U, "moyenageous"),

                  Adjective(Locale.FR, Gender.M, "envoutant"),
                  Adjective(Locale.FR, Gender.F, "envoutante"),
                  Adjective(Locale.EN, Gender.U, "bewitching"),

                  Adjective(Locale.FR, Gender.M, "fretillant"),
                  Adjective(Locale.FR, Gender.F, "fretillante"),
                  Adjective(Locale.EN, Gender.U, "wriggling"),

                  Adjective(Locale.FR, Gender.M, "malfaisant"),
                  Adjective(Locale.FR, Gender.F, "malfaisante"),
                  Adjective(Locale.EN, Gender.U, "evil"),

                  Adjective(Locale.FR, Gender.M, "languissant"),
                  Adjective(Locale.FR, Gender.F, "languissante"),
                  Adjective(Locale.EN, Gender.U, "languishing"),

                  Adjective(Locale.FR, Gender.M, "oppressant"),
                  Adjective(Locale.FR, Gender.F, "oppressante"),
                  Adjective(Locale.EN, Gender.U, "oppressing"),

                  Adjective(Locale.FR, Gender.M, "repugnant"),
                  Adjective(Locale.FR, Gender.F, "repugnante"),
                  Adjective(Locale.EN, Gender.U, "repulsive"),

                  Adjective(Locale.FR, Gender.M, "surprenant"),
                  Adjective(Locale.FR, Gender.F, "surprenante"),
                  Adjective(Locale.EN, Gender.U, "surprising"),

                  Adjective(Locale.FR, Gender.U, "veritable"),
                  Adjective(Locale.EN, Gender.U, "true"),

                  Adjective(Locale.FR, Gender.U, "invulnerable"),
                  Adjective(Locale.EN, Gender.U, "invulnerable"),

                  Adjective(Locale.FR, Gender.U, "de-lumiere"),
                  Adjective(Locale.EN, Gender.U, "light"),

                  Adjective(Locale.FR, Gender.U, "des-tenebres"),
                  Adjective(Locale.EN, Gender.U, "tenebrous"),

                  Adjective(Locale.FR, Gender.M, "gluant"),
                  Adjective(Locale.FR, Gender.F, "gluante"),
                  Adjective(Locale.EN, Gender.U, "slimy"),

                  Adjective(Locale.FR, Gender.M, "psychoactif"),
                  Adjective(Locale.FR, Gender.F, "psychoactive"),
                  Adjective(Locale.EN, Gender.U, "psychoactive"),

                  Adjective(Locale.FR, Gender.U, "legendaire"),
                  Adjective(Locale.EN, Gender.U, "legendary"),

                  Adjective(Locale.FR, Gender.U, "de-la-foret"),
                  Adjective(Locale.EN, Gender.U, "forest"),

                  Adjective(Locale.FR, Gender.U, "de-competition"),
                  Adjective(Locale.EN, Gender.U, "competitive"),

                  Adjective(Locale.FR, Gender.U, "de-bataille"),
                  Adjective(Locale.EN, Gender.U, "battle"),

                  Adjective(Locale.FR, Gender.U, "de-guerre"),
                  Adjective(Locale.EN, Gender.U, "war"),

                  Adjective(Locale.FR, Gender.M, "tribal"),
                  Adjective(Locale.FR, Gender.F, "tribale"),
                  Adjective(Locale.EN, Gender.U, "tribal"),

                  Adjective(Locale.FR, Gender.U, "epique"),
                  Adjective(Locale.EN, Gender.U, "epic"),

                  Adjective(Locale.FR, Gender.U, "mythique"),
                  Adjective(Locale.EN, Gender.U, "mythical"),

                  Adjective(Locale.FR, Gender.M, "tueur"),
                  Adjective(Locale.FR, Gender.F, "tueuse"),
                  Adjective(Locale.EN, Gender.U, "killer"),

                  Adjective(Locale.FR, Gender.U, "des-bois"),
                  Adjective(Locale.FR, Gender.U, "des-champs"),
                  Adjective(Locale.FR, Gender.U, "champetre"),

                  Adjective(Locale.FR, Gender.U, "splendide"),
                  Adjective(Locale.EN, Gender.U, "splendid"),

                  Adjective(Locale.FR, Gender.U, "neo", True),
                  Adjective(Locale.EN, Gender.U, "neo"),

                  Adjective(Locale.FR, Gender.M, "furtif"),
                  Adjective(Locale.FR, Gender.F, "furtive"),
                  Adjective(Locale.EN, Gender.U, "stealthy"),

                  Adjective(Locale.FR, Gender.U, "de-petite-vertue"),
                  Adjective(Locale.EN, Gender.U, "of-little-virtue", True),

                  Adjective(Locale.FR, Gender.M, "boutonneux"),
                  Adjective(Locale.FR, Gender.F, "boutonneuse"),
                  Adjective(Locale.EN, Gender.U, "spotty"),

                  Adjective(Locale.FR, Gender.M, "bigleu"),
                  Adjective(Locale.FR, Gender.F, "bigleuse"),

                  Adjective(Locale.FR, Gender.M, "des-sables"),
                  Adjective(Locale.FR, Gender.M, "du-desert"),
                  Adjective(Locale.EN, Gender.U, "sand"),
                  Adjective(Locale.EN, Gender.U, "desert"),

                  Adjective(Locale.FR, Gender.U, "carnivore"),
                  Adjective(Locale.EN, Gender.U, "carnivorous"),

                  Adjective(Locale.FR, Gender.U, "monstrueux"),
                  Adjective(Locale.EN, Gender.U, "monstruous"),

                  Adjective(Locale.FR, Gender.U, "titanesque"),
                  Adjective(Locale.EN, Gender.U, "titanic"),

                  Adjective(Locale.FR, Gender.U, "sage"),
                  Adjective(Locale.FR, Gender.U, "de-la-sagesse"),
                  Adjective(Locale.FR, Gender.U, "du-savoir"),
                  Adjective(Locale.EN, Gender.U, "wise"),

                  Adjective(Locale.FR, Gender.M, "lumineux"),
                  Adjective(Locale.FR, Gender.F, "lumineuse"),
                  Adjective(Locale.EN, Gender.U, "luminous"),

                  Adjective(Locale.FR, Gender.M, "geant"),
                  Adjective(Locale.FR, Gender.F, "geante"),
                  Adjective(Locale.EN, Gender.U, "giant"),

                  Adjective(Locale.FR, Gender.M, "costaud"),
                  Adjective(Locale.FR, Gender.F, "costaude"),
                  Adjective(Locale.EN, Gender.U, "beefy"),

                  #I'm not translating the 4 next word in english
                  #because they would end with a 'é' and since I'm
                  #using this for server naming it could cause problems
                  Adjective(Locale.EN, Gender.U, "dehydrated"),

                  Adjective(Locale.EN, Gender.U, "lyophilized"),

                  Adjective(Locale.EN, Gender.U, "momified"),

                  Adjective(Locale.EN, Gender.U, "expired"),

                  Adjective(Locale.FR, Gender.U, "analogique"),
                  Adjective(Locale.EN, Gender.U, "analog"),

                  Adjective(Locale.FR, Gender.U, "numerique"),
                  Adjective(Locale.EN, Gender.U, "digital"),

                  Adjective(Locale.FR, Gender.U, "techno", True),
                  Adjective(Locale.EN, Gender.U, "techno"),

                  Adjective(Locale.FR, Gender.M, "insolent"),
                  Adjective(Locale.FR, Gender.F, "insolente"),
                  Adjective(Locale.EN, Gender.U, "insolent"),

                  Adjective(Locale.FR, Gender.U, "noble"),
                  Adjective(Locale.EN, Gender.U, "noble"),

                  Adjective(Locale.FR, Gender.U, "ultra-pure"),
                  Adjective(Locale.EN, Gender.U, "ultra-pure"),

                  Adjective(Locale.FR, Gender.M, "royal"),
                  Adjective(Locale.FR, Gender.F, "royale"),
                  Adjective(Locale.EN, Gender.U, "royal"),

                  Adjective(Locale.FR, Gender.M, "crasseux"),
                  Adjective(Locale.FR, Gender.F, "crasseuse"),
                  Adjective(Locale.EN, Gender.U, "filfty"),

                  Adjective(Locale.FR, Gender.M, "puant"),
                  Adjective(Locale.FR, Gender.F, "puante"),
                  Adjective(Locale.EN, Gender.U, "stinky"),

                  Adjective(Locale.FR, Gender.M, "terrifiant"),
                  Adjective(Locale.FR, Gender.F, "terrifiante"),
                  Adjective(Locale.EN, Gender.U, "terrifying"),

                  Adjective(Locale.FR, Gender.U, "des-bas-fonds"),

                  Adjective(Locale.FR, Gender.U, "aquatique"),
                  Adjective(Locale.EN, Gender.U, "aquatic"),

                  Adjective(Locale.FR, Gender.U, "dynamique"),
                  Adjective(Locale.EN, Gender.U, "dynamic"),

                  Adjective(Locale.FR, Gender.M, "interdimensionnel"),
                  Adjective(Locale.FR, Gender.F, "interdimensionnelle"),
                  Adjective(Locale.EN, Gender.U, "interdimensionnal"),

                  Adjective(Locale.FR, Gender.U, "en-carton"),
                  Adjective(Locale.FR, Gender.U, "en-mousse"),
                  #french expression for "who suck"

                  Adjective(Locale.FR, Gender.U, "transgenique"),
                  Adjective(Locale.EN, Gender.U, "trangenic"),

                  Adjective(Locale.FR, Gender.U, "aware"),
                  Adjective(Locale.EN, Gender.U, "aware"),

                  Adjective(Locale.EN, Gender.U, "awesome")
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

        nameValue = name.value.lower()
        adjValue = adj.value.lower()

        if self.locale == Locale.FR:
            if adj.invert:
                return adjValue + "-"  + nameValue
            else:
                return nameValue + "-"  + adjValue

        if self.locale == Locale.EN:
            if adj.invert:
                return nameValue + "-" + adjValue
            else:
                return adjValue + "-" + nameValue

        raise Exception("Locale is unknown")

    def generateNameCamel(self):
        return self._camelize(self.generateName())
