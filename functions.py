"""
These are the completed functions. This .py file is temporary while I work on functions and complete them.
"""


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


def conjugate_are_verb(verb, pronoun):
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
            print(fare[pronoun])
            return fare[pronoun]
        else:
            print(andare[pronoun])
            return andare[pronoun]

    # this section checks for spelling issues like with mancare in order to preserve hard "k" sound of infinitive
    # if it's a verb like mancare then the if section adds an "h" for the spelling to preserve hard "k" sound
    # if it's a normal -are verb, then the else section conjugates it normally
    if verb[-4] == "c":
        stripped_verb = strip_off_ending(verb, pronoun)
        new_verb = stripped_verb + add_h[pronoun]
        print(new_verb)
        return new_verb
    else:
        stripped_verb = strip_off_ending(verb, pronoun)
        new_verb = stripped_verb + are_endings[pronoun]
        print(new_verb)
        return new_verb


def conjugate_ere_verb(verb, pronoun):
    """
    Conjugates regular verbs ending in -are.
    Parameters: accepts a string
    Return: returns a conjugated verb as a string
    Error handling: checks to see if the verb ends in -ere, then checks to see if the verb is irregular
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
    Error handling: checks to see if the verb ends in -ire, then checks to see if the verb is irregular
    Returns error message if one of those conditions is true
    """
    ire_endings = {"io": "o", "tu": "i", "lui": "e", "lei": "e", "noi": "iamo", "voi": "ite", "loro": "ono"}
    isco_endings = {"io": "isco", "tu": "isci", "lui": "isce", "lei": "isce", "noi": "iamo", "voi": "ite",
                    "loro": "iscono"}
    isco_verbs = ["capire", "finire", "pulire", "construire", "preferire", "obedire"]
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