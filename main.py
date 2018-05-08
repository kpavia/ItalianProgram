irregular_are = ["fare", "andare"]
irregular_ere = ["avere", "essere", "potere", "volere", "sapere", "bere"]
irregular_ire = ["uscire", "dire", "venire"]
mangiare = dict({"verb": "Mangiare", "translation": "to eat"})
mangiare["presente"] = {"io": "mangio", "tu": "mangi", "lui": "mangia", "lei": "mangia", "noi": "mangiamo",
                        "voi": "mangiate", "loro": "mangiano"}
mangiare["imperfetto"] = {"io": "mangiavo", "tu": "mangiavi", "lui": "mangiava", "lei": "mangiava", "noi": "mangiavamo",
                          "voi": "mangiavate", "loro": "mangiavano"}
mangiare["futuro"] = {"io": "mangiero'", "tu": "mangerai", "lui": "mangera'", "lei": "mangera'", "noi": "mangeremo",
                      "voi": "mangerete", "loro": "mangeranno"}


def begin():
    verb = input("What verb do you want to conjugate?\n")
    is_verb = verb_ending(verb)  # get the verb ending; returns False if not a verb
    if is_verb is False:
        raise ValueError
    else:  # call the conjugating function
        if is_verb == "are":
            again = True
            while again:
                print("conjugating -are")
                pronoun = input("What pronoun? io, tu, lui, lei, noi, voi, loro?\n").lower()
                conjugate_are_verb(verb, pronoun)
                go_again = input("Continue? y/n\n").lower()
                if go_again != "y":
                    again = False
        if is_verb == "ere":
            again = True
            while again:
                print("conjugating -ere")
                pronoun = input("What pronoun? io, tu, lui, lei, noi, voi, loro?\n").lower()
                conjugate_ere_verb(verb, pronoun)
                go_again = input("Continue? y/n\n").lower()
                if go_again != "y":
                    again = False
        if is_verb == "ire":
            again = True
            while again:
                print("conjugating -ire")
                pronoun = input("What pronoun? io, tu, lui, lei, noi, voi, loro?\n").lower()
                conjugate_ire_verb(verb, pronoun)
                go_again = input("Continue? y/n\n").lower()
                if go_again != "y":
                    again = False


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


def strip_off_ending(verb, pronoun):
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
            pronouns = ["io", "lei", "lui", "voi", "loro"]
            if verb[-4] == "i" and pronoun not in pronouns:
                return verb[:-4]
            else:
                return verb[:-3]
        except TypeError:
            raise TypeError


def conjugate_are_verb(verb, pronoun):
    """
    Conjugates regular verbs ending in -are.
    Parameters: both arguments must be strings
    Return: returns a conjugated verb as a string
    Error handling: checks to see if the verb ends in -are, then checks to see if the verb is irregular
    Returns error message if one of those conditions is true
    """

    are_endings = {"io": "o", "tu": "i", "lui": "a", "lei": "a", "noi": "iamo", "voi": "ate", "loro": "ano"}
    stripped_verb = strip_off_ending(verb, pronoun)
    new_verb = stripped_verb + are_endings[pronoun]
    print(new_verb)
    return new_verb


def conjugate_ere_verb(verb, pronoun):
    """
    Conjugates regular verbs ending in -are.
    Parameters: accepts a string
    Return: returns a conjugated verb as a string
    Error handling: checks to see if the verb ends in -are, then checks to see if the verb is irregular
    Returns error message if one of those conditions is true
    """
    ere_endings = {"io": "o", "tu": "i", "lui": "e", "lei": "e", "noi": "iamo", "voi": "ete", "loro": "ono"}
    stripped_verb = strip_off_ending(verb, pronoun)
    new_verb = stripped_verb + ere_endings[pronoun]
    print(new_verb)
    return new_verb


def conjugate_ire_verb(verb, pronoun):
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
    isco_verbs = ["capire", "finire", "pulire", "construire", "preferire"]
    if verb in isco_verbs:
        stripped_verb = strip_off_ending(verb, pronoun)
        new_verb = stripped_verb + isco_endings[pronoun]
        print(new_verb)
        return new_verb
    else:
        stripped_verb = strip_off_ending(verb, pronoun)
        new_verb = stripped_verb + ire_endings[pronoun]
        print(new_verb)
        return new_verb


begin()
# conjugate_are_verb("mangiare")
