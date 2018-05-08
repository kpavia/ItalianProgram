irregular_are = ["fare", "andare"]
irregular_ere = ["avere", "essere", "potere", "volere", "sapere", "bere"]
irregular_ire = ["uscire", "dire", "venire"]
isco_verbs = ["capire", "finire", "pulire", "construire", "preferire"]
mangiare = dict({"verb": "Mangiare", "translation": "to eat"})
mangiare["presente"] = {"io": "mangio", "tu": "mangi", "lui": "mangia", "lei": "mangia", "noi": "mangiamo",
                        "voi": "mangiate", "loro": "mangiano"}
mangiare["imperfetto"] = {"io": "mangiavo", "tu": "mangiavi", "lui": "mangiava", "lei": "mangiava", "noi": "mangiavamo",
                          "voi": "mangiavate", "loro": "mangiavano"}
mangiare["futuro"] = {"io": "mangiero'", "tu": "mangerai", "lui": "mangera'", "lei": "mangera'", "noi": "mangeremo",
                      "voi": "mangerete", "loro": "mangeranno"}

# TODO: move while loop to begin(); while loop in function is buggy

def begin():
    verb = input("What verb do you want to conjugate?\n")  # verb = mangiare
    is_verb = verb_ending(verb)  # isverb = are
    if is_verb is False:
        raise ValueError
    else:
        if is_verb == "are":
            conjugate_are_verb(verb)
        if is_verb == "ere":
            conjugate_ere_verb(verb)
        if is_verb == "ire":
            conjugate_ire_verb(verb)


def print_verb_dict(verb):
    """Prints out the info in the verb's dictionary"""
    for keys in verb:
        print(f'{keys}: {verb[keys]}')


def verb_ending(verb):
    """
    Returns the last 3 characters of the verb to determine the verb type
    Verb is passed in as a string
    Error handling checks to make sure the verb is a string data type and that it's actually a verb
    and not some other word
    Returns: a boolean False if an error is found
    """
    try:
        is_verb = verb[-3:]
        if is_verb in ["are", "ere", "ire"]:
            return is_verb
        else:
            return False
    except TypeError:
        raise TypeError


def strip_off_ending(verb, tense):
    """
    Strips the ending (last 3 characters) off the verb
    Parameters: accepts a string
    Return: returns a string
    Error handling: checks to make sure parameter is a verb and not just a verb
    Returns an error message if that condition is true
    """
    ending = verb_ending(verb)
    if ending is False:
        raise ValueError
    else:
        try:
            tenses = ["io", "lei", "lui", "voi", "loro"]
            if verb[-4] == "i" and tense not in tenses:
                return verb[:-4]
            else:
                return verb[:-3]
        except TypeError:
            raise TypeError


def conjugate_are_verb(verb):
    """
    Conjugates regular verbs ending in -are.
    Parameters: accepts a string
    Return: returns a conjugated verb as a string
    Error handling: checks to see if the verb ends in -are, then checks to see if the verb is irregular
    Returns error message if one of those conditions is true
    """
# TODO: place all input questions into begin and out of conjugating functions

    are_endings = {"io": "o", "tu": "i", "lui": "a", "lei": "a", "noi": "iamo", "voi": "ate", "loro": "ano"}
    are_verb = verb_ending(verb)
    if are_verb is False:
        raise ValueError
    verb_end = verb_ending(verb)
    if verb in irregular_are:
        raise ValueError
    if verb_end != "are":
        raise ValueError
    else:
        again = True
        print("starting while loop")
        while again:
            tense = input("Which tense? Io, Tu, Lui, Lei, Noi, Voi, Loro?\n").lower()
            stripped_verb = strip_off_ending(verb, tense)
            conjugated_verb = stripped_verb + are_endings[tense]
            print(conjugated_verb)
            try_again = input("Continue? Y/N?\n").lower()
            if try_again == "n":
                new_verb = input("Want a different verb? Y/N\n").lower()
                if new_verb == "n":
                    break


def conjugate_ere_verb(verb):
    """
    Conjugates regular verbs ending in -are.
    Parameters: accepts a string
    Return: returns a conjugated verb as a string
    Error handling: checks to see if the verb ends in -are, then checks to see if the verb is irregular
    Returns error message if one of those conditions is true
    """
    ere_endings = {"io": "o", "tu": "i", "lui": "e", "lei": "e", "noi": "iamo", "voi": "ete", "loro": "ono"}
    ere_verb = verb_ending(verb)
    if ere_verb is False:
        raise ValueError
    verb_end = verb_ending(verb)
    if verb in irregular_ere:
        raise ValueError
    if verb_end != "ere":
        raise ValueError
    else:
        again = True
        while again:
            tense = input("Which tense? Io, Tu, Lui, Lei, Noi, Voi, Loro?\n").lower()
            stripped_verb = strip_off_ending(verb)
            conjugated_verb = stripped_verb + ere_endings[tense]
            print(conjugated_verb)
            try_again = input("Continue? Y/N?\n").lower()
            if try_again == "n":
                return "done"


def conjugate_ire_verb(verb):
    """
    Conjugates regular verbs ending in -are.
    Parameters: accepts a string
    Return: returns a conjugated verb as a string
    Error handling: checks to see if the verb ends in -are, then checks to see if the verb is irregular
    Returns error message if one of those conditions is true
    """
    ire_endings = {"io": "o", "tu": "i", "lui": "e", "lei": "e", "noi": "iamo", "voi": "ite", "loro": "ono"}
    isco_endings = {"io": "isco", "tu": "isci", "lui": "isce", "lei": "isce", "noi": "iamo", "voi": "ite",
                    "loro": "iscono"}
    ire_verb = verb_ending(verb)
    if ire_verb is False:
        raise ValueError
    verb_end = verb_ending(verb)
    if verb in irregular_ere:
        raise ValueError
    if verb_end != "ire":
        raise ValueError
    if verb in isco_verbs:
        again = True
        while again:
            tense = input("Which tense? Io, Tu, Lui, Lei, Noi, Voi, Loro?\n").lower()
            stripped_verb = strip_off_ending(verb)
            conjugated_verb = stripped_verb + isco_endings[tense]
            print(conjugated_verb)
            try_again = input("Continue? Y/N?\n").lower()
            if try_again == "n":
                return "done"
    else:
        again = True
        while again:
            tense = input("Which tense? Io, Tu, Lui, Lei, Noi, Voi, Loro?\n").lower()
            stripped_verb = strip_off_ending(verb)
            conjugated_verb = stripped_verb + ire_endings[tense]
            print(conjugated_verb)
            try_again = input("Continue? Y/N?\n").lower()
            if try_again == "n":
                return "done"


begin()
# conjugate_are_verb("mangiare")
