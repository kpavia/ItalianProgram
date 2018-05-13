"""
These functions display conjugation endings. No quizzing functionality.
"""


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
                    conjugate_present_are_verb(verb, pronoun)
                    go_again = input("Continue? y/n\n").lower()
                    if go_again != "y":
                        return True
            if is_verb == "ere":
                again = True
                while again:
                    print("conjugating -ere")
                    pronoun = input("What pronoun? io, tu, lui, lei, noi, voi, loro?\n").lower()
                    conjugate_present_ere_verb(verb, pronoun)
                    go_again = input("Continue? y/n\n").lower()
                    if go_again != "y":
                        return True
            if is_verb == "ire":
                again = True
                while again:
                    print("conjugating -ire")
                    pronoun = input("What pronoun? io, tu, lui, lei, noi, voi, loro?\n").lower()
                    conjugate_present_ire_verb(verb, pronoun)
                    go_again = input("Continue? y/n\n").lower()
                    if go_again != "y":
                        return True


def print_verb_dict(verb):
    """Prints out the info in the verb's dictionary"""
    for keys in verb:
        print(f'{keys}: {verb[keys]}')


def verb_ending_good(verb):
    """
    Returns the last 3 characters of the verb to determine the verb type
    Verb is passed in as a string
    Error handling checks to make sure the verb is a string data type and that it's actually a verb
    and not some other word
    Returns: a boolean, True if a verb or False if not a verb
    """
    try:
        is_verb = verb[-3:]
        if is_verb in ["are", "ere", "ire"]:
            return True
        else:
            return False
    except TypeError:
        raise TypeError


def verb_ending(verb):
    """
    Returns the last 3 characters of the verb to determine the verb type
    Verb is passed in as a string
    Error handling checks to make sure the verb is a string data type and that it's actually a verb
    and not some other word
    Returns: a boolean, True if a verb or False if not a verb
    """
    try:
        is_verb = verb[-3:]
        if is_verb in ["are", "ere", "ire"]:
            return is_verb
        else:
            return False
    except TypeError:
        raise TypeError


def strip_off_ending(verb, pronoun, tense):
    """
    Strips the ending (last 3 characters) off the verb
    Parameters: accepts a string
    Return: returns a string
    Error handling: checks to make sure parameter is a verb and not just a word
    Returns an error message if that condition is true
    """
    ending = verb_ending(verb)
    if ending is False:
        raise ValueError
    else:
        try:
            pronouns = ["io", "lei", "lui", "voi", "loro"]
            if verb == "mangiare" and tense == "imperfetto":
                return verb[:-3]
            if verb[-4] == "i" and pronoun not in pronouns:
                return verb[:-4]
            else:
                return verb[:-3]
        except TypeError:
            raise TypeError


def conjugate_present_are_verb(verb, pronoun, tense):
    """
    Conjugates regular verbs ending in -are.
    Parameters: both arguments must be strings
    Return: returns a conjugated verb as a string
    Error handling: checks to see if the verb ends in -are, then checks to see if the verb is irregular
    Returns error message if one of those conditions is true
    """

    are_endings = {"io": "o", "tu": "i", "lui": "a", "lei": "a", "noi": "iamo", "voi": "ate", "loro": "ano"}
    add_h = {"io": "o", "tu": "hi", "lui": "a", "lei": "a", "noi": "hiamo", "voi": "ate", "loro": "ano"}
    irregular_are = ["fare", "andare"]
    fare = {"io": "faccio", "tu": "fai", "lei": "fa", "lui": "fa", "noi": "facciamo", "voi": "fate", "loro": "fanno"}
    andare = {"io": "vado", "tu": "vai", "lui": "va", "lei": "va", "noi": "andiamo", "voi": "andate", "loro": "vanno"}

    # this section checks for the irregular verbs fare, andare
    if verb in irregular_are:
        if verb == "fare":
            # print(fare[pronoun])
            return fare[pronoun]
        else:
            # print(andare[pronoun])
            return andare[pronoun]

    # this section checks for spelling issues like with mancare in order to preserve hard "k" sound of infinitive
    # if it's a verb like mancare then the if section adds an "h" for the spelling to preserve hard "k" sound
    # if it's a normal -are verb, then the else section conjugates it normally
    if verb[-4] == "c":
        stripped_verb = strip_off_ending(verb, pronoun, tense)
        new_verb = stripped_verb + add_h[pronoun]
        # print(new_verb)
        return new_verb
    else:
        stripped_verb = strip_off_ending(verb, pronoun, tense)
        new_verb = stripped_verb + are_endings[pronoun]
        # print(new_verb)
        print(stripped_verb)
        return new_verb


def conjugate_present_ere_verb(verb, pronoun, tense):
    """
    Conjugates regular verbs ending in -are.
    Parameters: accepts a string
    Return: returns a conjugated verb as a string
    Error handling: checks to see if the verb ends in -ere, then checks to see if the verb is irregular
    Returns error message if one of those conditions is true
    """
    ere_endings = {"io": "o", "tu": "i", "lui": "e", "lei": "e", "noi": "iamo", "voi": "ete", "loro": "ono"}
    stripped_verb = strip_off_ending(verb, pronoun, tense)
    new_verb = stripped_verb + ere_endings[pronoun]
    return new_verb


def conjugate_present_ire_verb(verb, pronoun, tense):
    """
    Conjugates regular verbs ending in -are.
    Parameters: accepts a string
    Return: returns a conjugated verb as a string
    Error handling: checks to see if the verb ends in -ire, then checks to see if the verb is irregular
    Returns error message if one of those conditions is true
    """
    ire_endings = {"io": "o", "tu": "i", "lui": "e", "lei": "e", "noi": "iamo", "voi": "ite", "loro": "ono"}
    isco_endings = {"io": "isco", "tu": "isci", "lui": "isce", "lei": "isce", "noi": "iamo", "voi": "ite",
                    "loro": "iscono"}
    isco_verbs = ["capire", "finire", "pulire", "construire", "preferire", "obedire"]
    if verb in isco_verbs:
        stripped_verb = strip_off_ending(verb, pronoun, tense)
        new_verb = stripped_verb + isco_endings[pronoun]
        return new_verb
    else:
        stripped_verb = strip_off_ending(verb, pronoun, tense)
        new_verb = stripped_verb + ire_endings[pronoun]
        return new_verb


def display_present_are_endings():
    """
    Function just displays present tense -are verb endings.
    No parameters.
    Returns nothing
    """
    are_endings = {"io": "-o", "tu": "-i", "lui": "-a", "lei": "-a", "noi": "-iamo", "voi": "-ate", "loro": "-ano"}
    for keys in are_endings:
        print(f'{keys}: {are_endings[keys]}')


def display_present_ere_endings():
    """
    Function just displays present tense -ere verb endings.
    No parameters.
    Returns nothing
    """
    ere_endings = {"io": "-o", "tu": "-i", "lui": "-e", "lei": "-e", "noi": "-iamo", "voi": "-ete", "loro": "-ono"}
    for keys in ere_endings:
        print(f'{keys}: {ere_endings[keys]}')


def display_present_ire_endings():
    """
    Function just displays present tense -ire verb endings.
    No parameters.
    Returns nothing
    """
    ire_endings = {"io": "-o", "tu": "-i", "lui": "-e", "lei": "-e", "noi": "-iamo", "voi": "-ite", "loro": "-ono"}
    for keys in ire_endings:
        print(f'{keys}: {ire_endings[keys]}')


def conjugate_imperfect_are_verb(verb, pronoun, tense):
    are_endings = {"io": "avo", "tu": "avi", "lui": "ava", "lei": "ava", "noi": "avamo", "voi": "avate", "loro": "avano"}
    add_h = {"io": "o", "tu": "hi", "lui": "a", "lei": "a", "noi": "hiamo", "voi": "ate", "loro": "ano"}
    irregular_are = ["fare", "andare"]
    fare = {"io": "facevo", "tu": "facevi", "lei": "faceva", "lui": "faceva", "noi": "facevamo", "voi": "facevate",
            "loro": "facevano"}
    andare = {"io": "andavo", "tu": "andavi", "lui": "andava", "lei": "andava", "noi": "andavamo", "voi": "andavate",
              "loro": "andavano"}

    # this section checks for the irregular verbs fare, andare
    if verb in irregular_are:
        if verb == "fare":
            # print(fare[pronoun])
            return fare[pronoun]
        else:
            # print(andare[pronoun])
            return andare[pronoun]

    # this section checks for spelling issues like with mancare in order to preserve hard "k" sound of infinitive
    # if it's a verb like mancare then the if section adds an "h" for the spelling to preserve hard "k" sound
    # if it's a normal -are verb, then the else section conjugates it normally
    if verb[-4] == "c":
        stripped_verb = strip_off_ending(verb, pronoun, tense)
        new_verb = stripped_verb + add_h[pronoun]
        # print(new_verb)
        return new_verb
    else:
        stripped_verb = strip_off_ending(verb, pronoun, tense)
        new_verb = stripped_verb + are_endings[pronoun]
        # print(new_verb)
        return new_verb





