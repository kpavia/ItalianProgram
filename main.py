import functions

irregular_ere = ["avere", "essere", "potere", "volere", "sapere", "bere"]
irregular_ire = ["uscire", "dire", "venire"]
mangiare = dict({"verb": "Mangiare", "translation": "to eat"})
mangiare["presente"] = {"io": "mangio", "tu": "mangi", "lui": "mangia", "lei": "mangia", "noi": "mangiamo",
                        "voi": "mangiate", "loro": "mangiano"}
mangiare["imperfetto"] = {"io": "mangiavo", "tu": "mangiavi", "lui": "mangiava", "lei": "mangiava", "noi": "mangiavamo",
                          "voi": "mangiavate", "loro": "mangiavano"}
mangiare["futuro"] = {"io": "mangiero'", "tu": "mangerai", "lui": "mangera'", "lei": "mangera'", "noi": "mangeremo",
                      "voi": "mangerete", "loro": "mangeranno"}

# TODO: make functions that quiz on conjugations
# TODO: need to conjugate irregular -ere, -ire verbs


def begin():
    verb = input("What verb do you want to conjugate?\n")
    is_verb = functions.verb_ending(verb)  # get the verb ending; returns False if not a verb
    if is_verb is False:
        raise ValueError
    else:  # call the conjugating function
        if is_verb == "are":
            again = True
            while again:
                print("conjugating -are")
                pronoun = input("What pronoun? io, tu, lui, lei, noi, voi, loro?\n").lower()
                functions.conjugate_are_verb(verb, pronoun)
                go_again = input("Continue? y/n\n").lower()
                if go_again != "y":
                    return True
        if is_verb == "ere":
            again = True
            while again:
                print("conjugating -ere")
                pronoun = input("What pronoun? io, tu, lui, lei, noi, voi, loro?\n").lower()
                functions.conjugate_ere_verb(verb, pronoun)
                go_again = input("Continue? y/n\n").lower()
                if go_again != "y":
                    return True
        if is_verb == "ire":
            again = True
            while again:
                print("conjugating -ire")
                pronoun = input("What pronoun? io, tu, lui, lei, noi, voi, loro?\n").lower()
                functions.conjugate_ire_verb(verb, pronoun)
                go_again = input("Continue? y/n\n").lower()
                if go_again != "y":
                    return True


def display_present_are_endings():
    are_endings = {"io": "-o", "tu": "-i", "lui": "-a", "lei": "-a", "noi": "-iamo", "voi": "-ate", "loro": "-ano"}
    for keys in are_endings:
        print(f'{keys}: {are_endings[keys]}')


def display_present_ere_endings():
    ere_endings = {"io": "-o", "tu": "-i", "lui": "-e", "lei": "-e", "noi": "-iamo", "voi": "-ete", "loro": "-ono"}
    for keys in ere_endings:
        print(f'{keys}: {ere_endings[keys]}')


def display_present_ire_endings():
    ire_endings = {"io": "-o", "tu": "-i", "lui": "-e", "lei": "-e", "noi": "-iamo", "voi": "-ite", "loro": "-ono"}
    for keys in ire_endings:
        print(f'{keys}: {ire_endings[keys]}')

# just commented out for testing
# starting = True
# while starting:
#     begin()
#     another = input("Choose another verb? y/n\n").lower()
#     if another == "n":
#         starting = False


display_present_are_endings()
print("-------------------------")
display_present_ere_endings()
print("-------------------------")
display_present_ire_endings()
