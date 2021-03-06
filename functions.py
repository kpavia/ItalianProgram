
"""
These functions display conjugation endings. No quizzing functionality.
"""

# TODO: irregular verbs to fix: sedere, avere, scegliere, conoscere, pagare (check all tenses)
# TODO: do all error handling in beginning of functions
# TODO: check all verb conjugating functions for bugs using review_verb()
# TODO: ^ tenses that are checked g2g: -are: present, imperfect


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


# consider deleting this since it duplicates verb_ending()
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
    Returns: the verb's ending if a verb or False if not a verb
    """
    try:
        is_verb = verb[-3:]
        if is_verb in ["are", "ere", "ire"]:
            return is_verb
        else:
            return False
    except TypeError:
        raise TypeError("Word doesn't have a proper verb ending")


def strip_off_ending(verb, tense):
    """
    Strips the ending (last 3 characters) off the verb
    Parameters: accepts a string
    Return: returns a string
    Error handling: checks to make sure parameter is a verb and not just a word
    Returns an error message if that condition is true
    """

    # checks to make sure that the verb is actually a verb
    ending = verb_ending(verb)
    if ending is False:
        raise ValueError("Not a verb")
    else:
        try:
            if ending == "are":
                if verb[-5:] == "giare":
                    if tense in ["imperfetto", "congiuntivoimp"]:
                        return verb[:-3]
                    else:
                        return verb[:-4]
                if verb[-5:] == "ciare":
                    tenses = ["futuro", "congiuntivopr", "condizionale"]
                    if tense in tenses:
                        return verb[:-4]
                    else:
                        return verb[:-3]
                else:
                    return verb[:-3]
            if ending == "ere":
                if verb == "compiere" and tense in ["presente", "imperfetto"]:
                    return verb[:-3]
                else:
                    return verb[:-3]
            if ending == "ire":
                return verb[:-3]
        except TypeError:
            raise TypeError


def api_call_tracker():
    """
    Keeps track of how many API calls are made. Must stay under 5,000/month.
    """
    calls = 0

    # try part: checks to see if the file exists. If it does, it'll read from it and set the calls variable to whatever
    # number is read from the file.
    # except part: if file is not found, it'll create the file and writes a 1 to it. This only should happen when the
    # file is initially created when the first API call is made. That's why it's writing 1 to the file.
    # the Except should be called only on the very first API call. The Try should be called for every API recording
    # hereafter.
    try:
        file = open("api_tracker.txt", "r")
        for item in file:
            calls = int(item)
        file.close()

    except FileNotFoundError:
        file = open("api_tracker.txt", "w")
        file.write("1")
        file.close()
        print("API Calls: 1")
        return None

    calls += 1
    calls = str(calls)

    file = open("api_tracker.txt", "w")
    file.write(calls)
    print(f'API Calls: {calls}')
    file.close()


# present tense


def create_verb_file(verb, tense):
    pronouns = ["io", "tu", "lui", "lei", "noi", "voi", "loro"]
    are_endings = {"io": "o", "tu": "i", "lui": "a", "lei": "a", "noi": "iamo", "voi": "ate", "loro": "ano"}
    add_h = {"io": "o", "tu": "hi", "lui": "a", "lei": "a", "noi": "hiamo", "voi": "ate", "loro": "ano"}
    irregular_are = ["fare", "andare"]
    fare = {"io": "faccio", "tu": "fai", "lei": "fa", "lui": "fa", "noi": "facciamo", "voi": "fate", "loro": "fanno"}
    andare = {"io": "vado", "tu": "vai", "lui": "va", "lei": "va", "noi": "andiamo", "voi": "andate", "loro": "vanno"}

    if tense == "presente":
        stripped_verb = strip_off_ending(verb, "io", tense)
        verb_file = open(f'{verb}.txt', "w")
        verb_file.write(f'{verb} Present Tense\n')
        if verb in irregular_are:
            if verb == "fare":
                for pronoun in fare:
                    new_verb = fare[pronoun]
                    verb_file.write(f'{pronoun}: {new_verb}\n')
        else:
            for pronoun in are_endings:
                new_verb = stripped_verb + are_endings[pronoun]
                verb_file.write(f'{pronoun} {new_verb}\n')
                print(f'{new_verb} recorded.')
        verb_file.close()


def conjugate_present_are_verb(verb, pronoun, tense):
    """
    Conjugates regular verbs ending in -are.
    Parameters: both arguments must be strings
    Return: returns a conjugated verb as a string
    Error handling: checks to see if the verb ends in -are, then checks to see if the verb is irregular
    Returns error message if one of those conditions is true
    """

    are_endings = {"io": "o", "tu": "i", "lui": "a", "lei": "a", "noi": "iamo", "voi": "ate", "loro": "ano"}
    giare_endings = {"io": "io", "tu": "i", "lui": "ia", "lei": "ia", "noi": "iamo", "voi": "iate", "loro": "iano"}
    ciare_endings = {"io": "o", "tu": "", "lui": "a", "lei": "a", "noi": "amo", "voi": "ate", "loro": "ano"}
    add_h = {"io": "o", "tu": "hi", "lui": "a", "lei": "a", "noi": "hiamo", "voi": "ate", "loro": "ano"}
    irregular_are = ["fare", "andare"]
    fare = {"io": "faccio", "tu": "fai", "lei": "fa", "lui": "fa", "noi": "facciamo", "voi": "fate", "loro": "fanno"}
    andare = {"io": "vado", "tu": "vai", "lui": "va", "lei": "va", "noi": "andiamo", "voi": "andate", "loro": "vanno"}

    # this section checks for the irregular verbs fare, andare
    if verb in irregular_are:
        if verb == "fare":
            return fare[pronoun]
        else:
            return andare[pronoun]

    # this section checks for spelling issues like with mancare in order to preserve hard "k" sound of infinitive
    # if it's a verb like mancare then the if section adds an "h" for the spelling to preserve hard "k" sound
    # if it's a normal -are verb, then the else section conjugates it normally
    if verb[-5:] == "giare":
        stripped_verb = strip_off_ending(verb, tense)
        new_verb = stripped_verb + giare_endings[pronoun]
        return new_verb
    if verb[-5:] == "ciare":
        stripped_verb = strip_off_ending(verb, tense)
        new_verb = stripped_verb + ciare_endings[pronoun]
        return new_verb
    if verb[-4:] == "care":
        stripped_verb = strip_off_ending(verb, tense)
        new_verb = stripped_verb + add_h[pronoun]
        return new_verb
    if verb[-4:] == "gare":
        stripped_verb = strip_off_ending(verb, tense)
        new_verb = stripped_verb + add_h[pronoun]
        return new_verb
    else:
        stripped_verb = strip_off_ending(verb, tense)
        new_verb = stripped_verb + are_endings[pronoun]
        return new_verb


def conjugate_present_ere_verb(verb, pronoun, tense):
    """
    Conjugates regular verbs ending in -ere.
    Parameters: accepts a string
    Return: returns a conjugated verb as a string
    Error handling: checks to see if the verb ends in -ere, then checks to see if the verb is irregular
    Returns error message if one of those conditions is true
    """
    avere = {"io": "ho", "tu": "hai", "lui": "ha", "lei": "ha", "noi": "abbiamo", "voi": "avete", "loro": "hanno"}

    irregulars = ["avere"]
    if verb in irregulars:
        if verb == "avere":
            return avere[pronoun]

    ere_endings = {"io": "o", "tu": "i", "lui": "e", "lei": "e", "noi": "iamo", "voi": "ete", "loro": "ono"}
    compiere_endings = {"io": "o", "tu": "", "lei": "e", "lui": "e", "noi": "amo", "voi": "ete", "loro": "ono"}

    if verb == "compiere":
        if tense == "presente":
            stripped_verb = strip_off_ending(verb, tense)
            new_verb = stripped_verb + compiere_endings[pronoun]
            return new_verb
        else:
            stripped_verb = strip_off_ending(verb, tense)
            new_verb = stripped_verb + ere_endings[pronoun]
            return new_verb
    else:
        stripped_verb = strip_off_ending(verb, tense)
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
    uscire = {"io": "esco", "tu": "esci", "lei": "esce", "lui": "esce", "noi": "usciamo", "voi": "uscite",
              "loro": "escono"}
    dire = {"io": "dico", "tu": "dici", "lui": "dice", "lei": "dice", "noi": "diciamo", "voi": "dite",
            "loro": "dicono"}
    ire_endings = {"io": "o", "tu": "i", "lui": "e", "lei": "e", "noi": "iamo", "voi": "ite", "loro": "ono"}
    isco_endings = {"io": "isco", "tu": "isci", "lui": "isce", "lei": "isce", "noi": "iamo", "voi": "ite",
                    "loro": "iscono"}
    isco_verbs = ["capire", "finire", "pulire", "construire", "preferire", "obedire"]
    irregular = ["uscire", "dire"]
    if verb in irregular:
        if verb == "usicre":
            return uscire[pronoun]
        if verb == "dire":
            return dire[pronoun]
    if verb in isco_verbs:
        stripped_verb = strip_off_ending(verb, tense)
        new_verb = stripped_verb + isco_endings[pronoun]
        return new_verb
    else:
        stripped_verb = strip_off_ending(verb, tense)
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


# imperfect tense


def display_imperfect_are_endings():
    are_endings = {"io": "-avo", "tu": "-avi", "lei": "-ava", "lui": "-ava", "noi": "-avamo", "voi": "-avate",
                   "loro": "-avano"}
    for keys in are_endings:
        print(f'{keys}: {are_endings[keys]}')


def display_imperfect_ere_endings():
    ere_endings = {"io": "-evo", "tu": "-evi", "lei": "-eva", "lui": "-eva", "noi": "-evamo", "voi": "-evate",
                   "loro": "-evano"}
    for keys in ere_endings:
        print(f'{keys}: {ere_endings[keys]}')


def display_imperfect_ire_endings():
    ire_endings = {"io": "-ivo", "tu": "-ivi", "lei": "-iva", "lui": "-iva", "noi": "-ivamo", "voi": "-ivate",
                   "loro": "-ivano"}
    for keys in ire_endings:
        print(f'{keys}: {ire_endings[keys]}')


def conjugate_imperfect_are_verb(verb, pronoun, tense):
    are_endings = {"io": "avo", "tu": "avi", "lui": "ava", "lei": "ava", "noi": "avamo", "voi": "avate",
                   "loro": "avano"}
    irregular_are = ["fare", "andare"]
    fare = {"io": "facevo", "tu": "facevi", "lei": "faceva", "lui": "faceva", "noi": "facevamo", "voi": "facevate",
            "loro": "facevano"}
    andare = {"io": "andavo", "tu": "andavi", "lui": "andava", "lei": "andava", "noi": "andavamo", "voi": "andavate",
              "loro": "andavano"}

    # this section checks for the irregular verbs fare, andare
    if verb in irregular_are:
        if verb == "fare":
            return fare[pronoun]
        else:
            return andare[pronoun]

    # this section checks for spelling issues like with mancare in order to preserve hard "k" sound of infinitive
    # if it's a verb like mancare then the if section adds an "h" for the spelling to preserve hard "k" sound
    # if it's a normal -are verb, then the else section conjugates it normally

    stripped_verb = strip_off_ending(verb, tense)
    new_verb = stripped_verb + are_endings[pronoun]
    return new_verb


def conjugate_imperfect_ere_verb(verb, pronoun, tense):
    ere_endings = {"io": "evo", "tu": "evi", "lei": "eva", "lui": "eva", "noi": "evamo", "voi": "evate",
                   "loro": "evano"}
    compiere_endings = {"io": "vo", "tu": "vi", "lei": "va", "lui": "va", "noi": "vamo", "voi": "vate",
                        "loro": "vano"}

    if verb == "compiere":
        stripped_verb = strip_off_ending(verb, tense)
        new_verb = stripped_verb + compiere_endings[pronoun]
        return new_verb
    else:
        stripped_verb = strip_off_ending(verb, tense)
        new_verb = stripped_verb + ere_endings[pronoun]
        return new_verb


def conjugate_imperfect_ire_verb(verb, pronoun, tense):
    """
    Conjugates -ire verbs in the imperfect tense.
    Raises a type error if the verb parameter isn't an -ire verb.
    :param verb: string, should be a -ire verb
    :param pronoun: string
    :param tense: string
    :return: A string object, the conjugated verb
    """

    ending = verb_ending(verb)
    if ending != "ire":
        raise TypeError
    irregulars = ["dire"]
    dire = {"io": "dicevo", "tu": "dicevi", "lui": "diceva", "lei": "diceva", "noi": "dicevamo", "voi": "dicevate",
            "loro": "dicevano"}
    if verb in irregulars:
        if verb == "dire":
            return dire[pronoun]
    ire_endings = {"io": "ivo", "tu": "ivi", "lei": "iva", "lui": "iva", "noi": "ivamo", "voi": "ivate",
                   "loro": "ivano"}
    stripped_verb = strip_off_ending(verb, tense)
    new_verb = stripped_verb + ire_endings[pronoun]
    return new_verb


# future tense


def display_future_are_ere_endings():
    endings = {"io": "-erò", "tu": "-erai", "lei": "-erà", "lui": "-erà", "noi": "-eremo", "voi": "-erete",
               "loro": "-eranno"}
    for keys in endings:
        print(f'{keys}: {endings[keys]}')


def display_future_ire_endings():
    are_endings = {"io": "-irò", "tu": "-irai", "lei": "-irà", "lui": "-irà", "noi": "-iremo", "voi": "-irete",
                   "loro": "-iranno"}
    for keys in are_endings:
        print(f'{keys}: {are_endings[keys]}')


def conjugate_future_are_ere_verb(verb, pronoun, tense):
    endings = {"io": "erò", "tu": "erai", "lei": "erà", "lui": "erà", "noi": "eremo", "voi": "erete",
               "loro": "eranno"}
    irregular_are = ["fare", "andare", "compiere"]
    add_h = {"io": "herò", "tu": "herai", "lui": "herà", "lei": "herà", "noi": "heremo", "voi": "herete",
             "loro": "heranno"}
    fare = {"io": "farò", "tu": "farai", "lei": "farà", "lui": "farà", "noi": "faremo", "voi": "farete",
            "loro": "faranno"}
    andare = {"io": "andrò", "tu": "andrai", "lui": "andrà", "lei": "andrà", "noi": "andremo", "voi": "andrete",
              "loro": "andranno"}
    compiere = {"io": "rò", "tu": "rai", "lei": "rà", "lui": "rà", "noi": "remo", "voi": "rete", "loro": "ranno"}

    # this section checks for the irregular verbs fare, andare
    if verb in irregular_are:
        if verb == "fare":
            return fare[pronoun]
        elif verb == "andare":
            return andare[pronoun]
        elif verb == "compiere":
            stripped_verb = strip_off_ending(verb, tense)
            new_verb = stripped_verb + compiere[pronoun]
            return new_verb

    # normal conjugation section
    is_verb = verb_ending(verb)
    if is_verb == "are":
        if verb[-4:] == "care" or verb[-4:] == "gare":
            stripped_verb = strip_off_ending(verb, tense)
            new_verb = stripped_verb + add_h[pronoun]
            return new_verb
        else:
            stripped_verb = strip_off_ending(verb, tense)
            new_verb = stripped_verb + endings[pronoun]
            return new_verb
    if is_verb == "ere":
        stripped_verb = strip_off_ending(verb, tense)
        new_verb = stripped_verb + endings[pronoun]
        return new_verb


def conjugate_future_ire_verb(verb, pronoun, tense):
    """
    Conjugates -ire verbs in the future tense.
    Raises a type error if the verb parameters isn't an -ire verb.
    :param verb: string, -ire verb
    :param pronoun: string
    :param tense: string
    :return: Returns the conjugated verb as a string.
    """

    ending = verb_ending(verb)
    if ending != "ire":
        raise TypeError
    ire_endings = {"io": "irò", "tu": "irai", "lei": "irà", "lui": "irà", "noi": "iremo", "voi": "irete",
                   "loro": "iranno"}

    stripped_verb = strip_off_ending(verb, tense)
    new_verb = stripped_verb + ire_endings[pronoun]
    return new_verb


# conditional present tense


def display_conditionalpr_are_ere_verb():
    endings = {"io": "-erei", "tu": "-eresti", "lei": "-erebbe", "lui": "-erebbe", "noi": "-eremmo", "voi": "-ereste",
               "loro": "-erebbero"}
    for keys in endings:
        print(f'{keys}: {endings[keys]}')


def display_conditionalpr_ire_verb():
    endings = {"io": "-irei", "tu": "-iresti", "lei": "-irebbe", "lui": "-irebbe", "noi": "-iremmo", "voi": "-ireste",
               "loro": "-irebbero"}
    for keys in endings:
        print(f'{keys}: {endings[keys]}')


def conjugate_conditionalpr_are_ere_verb(verb, pronoun, tense):
    """
    This function conjugates -are, -ere verbs in the conditional present tense.
    Parameters: accepts all parameters as strings.
    Returns: returns strings
    """
    if verb[-3:] != "are" and verb[-3:] != "ere":
        raise ValueError
    endings = {"io": "erei", "tu": "eresti", "lei": "erebbe", "lui": "erebbe", "noi": "eremmo", "voi": "ereste",
               "loro": "erebbero"}
    compiere_endings = {"io": "rei", "tu": "resti", "lei": "rebbe", "lui": "rebbe", "noi": "remmo", "voi": "reste",
                        "loro": "rebbero"}
    irregular_are = ["fare", "andare"]
    add_h = {"io": "herei", "tu": "heresti", "lui": "herebbe", "lei": "herebbe", "noi": "heremmo", "voi": "hereste",
             "loro": "herebbero"}
    fare = {"io": "farei", "tu": "faresti", "lei": "farebbe", "lui": "farebbe", "noi": "faremmo", "voi": "fareste",
            "loro": "farebbero"}
    andare = {"io": "andrei", "tu": "andresti", "lui": "andrebbe", "lei": "andrebbe", "noi": "andremmo",
              "voi": "andreste", "loro": "andrebbero"}

    # this section checks for the irregular verbs fare, andare
    if verb in irregular_are:
        if verb == "fare":
            return fare[pronoun]
        else:
            return andare[pronoun]

    # normal conjugation section for -are
    if verb[-3:] == "are":
        if verb[-4:] == "care" or verb[-4:] == "gare":
            stripped_verb = strip_off_ending(verb, tense)
            new_verb = stripped_verb + add_h[pronoun]
            return new_verb
        else:
            stripped_verb = strip_off_ending(verb, tense)
            new_verb = stripped_verb + endings[pronoun]
            return new_verb

    # normal conjugation section for -ere
    if verb[-3:] == "ere":
        if verb == "compiere":
            stripped_verb = strip_off_ending(verb, tense)
            new_verb = stripped_verb + compiere_endings[pronoun]
            return new_verb
        else:
            stripped_verb = strip_off_ending(verb, tense)
            new_verb = stripped_verb + endings[pronoun]
            return new_verb


def conjugate_conditionalpr_ire_verb(verb, pronoun, tense):
    """
    This function conjugates -ire verbs in the conditional present tense.
    Parameter: verb - string, pronoun - string, tense - string.
    Returns: a string
    """

    if verb[-3:] != "ire":
        raise ValueError
    ire_endings = {"io": "irei", "tu": "iresti", "lei": "irebbe", "lui": "irebbe", "noi": "iremmo", "voi": "ireste",
                   "loro": "irebbero"}

    stripped_verb = strip_off_ending(verb, tense)
    new_verb = stripped_verb + ire_endings[pronoun]
    return new_verb


# present subjunctive tense


def display_subjunctivepr_are_verb():
    endings = {"io": "-i", "tu": "-i", "lei": "-i", "lui": "-i", "noi": "-iamo", "voi": "-iate", "loro": "-ino"}
    for keys in endings:
        print(f'{keys}: {endings[keys]}')


def display_subjunctivepr_ere_verb():
    endings = {"io": "-a", "tu": "-a", "lei": "-a", "lui": "-a", "noi": "-iamo", "voi": "-iate", "loro": "-ano"}
    for keys in endings:
        print(f'{keys}: {endings[keys]}')


def display_subjunctivepr_ire_verb():
    endings = {"io": "-a", "tu": "-a", "lei": "-a", "lui": "-a", "noi": "-iamo", "voi": "-iate", "loro": "-ano"}
    for keys in endings:
        print(f'{keys}: {endings[keys]}')


def conjugate_subjunctivepr_ire_verb(verb, pronoun, tense):
    ending = verb_ending(verb)
    if ending != "ire":
        raise TypeError

    uscire = {"io": "esca", "tu": "esca", "lei": "esca", "lui": "esca", "noi": "usciamo", "voi": "usciate",
              "loro": "escano"}
    dire = {"io": "dica", "tu": "dica", "lei": "dica", "lui": "dica", "noi": "diciamo", "voi": "diciate",
            "loro": "dicano"}
    ire_endings = {"io": "a", "tu": "a", "lei": "a", "lui": "a", "noi": "iamo", "voi": "iate", "loro": "ano"}
    isco_endings = {"io": "isca", "tu": "isca", "lui": "isca", "lei": "isca", "noi": "iamo", "voi": "iate",
                    "loro": "iscano"}
    isco_verbs = ["capire", "finire", "pulire", "construire", "preferire", "obedire"]
    irregulars = ["uscire", "dire"]
    if verb in irregulars:
        if verb == "uscire":
            return uscire[pronoun]
        if verb == "dire":
            return dire[pronoun]
    if verb in isco_verbs:
        stripped_verb = strip_off_ending(verb, tense)
        new_verb = stripped_verb + isco_endings[pronoun]
        return new_verb
    else:
        stripped_verb = strip_off_ending(verb, tense)
        new_verb = stripped_verb + ire_endings[pronoun]
        return new_verb


def conjugate_subjunctivepr_are_verb(verb, pronoun, tense):
    are_endings = {"io": "i", "tu": "i", "lui": "i", "lei": "i", "noi": "iamo", "voi": "iate", "loro": "ino"}
    irregular_are = ["fare", "andare"]
    add_h = {"io": "hi", "tu": "hi", "lui": "hi", "lei": "hi", "noi": "hiamo", "voi": "hiate", "loro": "hino"}
    fare = {"io": "faccia", "tu": "faccia", "lei": "faccia", "lui": "faccia", "noi": "facciamo", "voi": "facciate",
            "loro": "facciano"}
    andare = {"io": "vada", "tu": "vada", "lui": "vada", "lei": "vada", "noi": "andiamo", "voi": "andiate",
              "loro": "vadano"}

    # this section checks for the irregular verbs fare, andare
    if verb in irregular_are:
        if verb == "fare":
            return fare[pronoun]
        else:
            return andare[pronoun]

    # this section checks for spelling issues like with mancare in order to preserve hard "k" sound of infinitive
    # if it's a verb like mancare then the if section adds an "h" for the spelling to preserve hard "k" sound
    # if it's a normal -are verb, then the else section conjugates it normally

    if verb[-4:] == "care" or verb[-4:] == "gare":
        stripped_verb = strip_off_ending(verb, tense)
        new_verb = stripped_verb + add_h[pronoun]
        return new_verb
    else:
        stripped_verb = strip_off_ending(verb, tense)
        new_verb = stripped_verb + are_endings[pronoun]
        return new_verb


def conjugate_subjunctivepr_ere_verb(verb, pronoun, tense):
    if verb[-3:] != "ere":
        raise ValueError

    ere_endings = {"io": "a", "tu": "a", "lei": "a", "lui": "a", "noi": "iamo", "voi": "iate", "loro": "ano"}
    compiere_endings = {"io": "a", "tu": "a", "lei": "a", "lui": "a", "noi": "amo", "voi": "ate", "loro": "ano"}

    if verb == "compiere":
        stripped_verb = strip_off_ending(verb, tense)
        new_verb = stripped_verb + compiere_endings[pronoun]
        return new_verb
    else:
        stripped_verb = strip_off_ending(verb, tense)
        new_verb = stripped_verb + ere_endings[pronoun]
        return new_verb


# imperfect subjunctive tense


def display_subjunctiveimp_are_verb():
    endings = {"io": "-assi", "tu": "-assi", "lei": "-asse", "lui": "-asse", "noi": "-assimo", "voi": "-aste",
               "loro": "-assero"}
    for keys in endings:
        print(f'{keys}: {endings[keys]}')


def display_subjunctiveimp_ere_verb():
    endings = {"io": "-essi", "tu": "-essi", "lei": "-esse", "lui": "-esse", "noi": "-essimo", "voi": "-este",
               "loro": "-essero"}
    for keys in endings:
        print(f'{keys}: {endings[keys]}')


def display_subjunctiveimp_ire_verb():
    endings = {"io": "-issi", "tu": "-issi", "lei": "-isse", "lui": "-isse", "noi": "-issimo", "voi": "-iste",
               "loro": "-issero"}
    for keys in endings:
        print(f'{keys}: {endings[keys]}')


def conjugate_subjunctiveimp_are_verb(verb, pronoun, tense):
    are_endings = {"io": "assi", "tu": "assi", "lui": "asse", "lei": "asse", "noi": "assimo", "voi": "aste",
                   "loro": "assero"}
    irregular_are = ["fare"]
    fare = {"io": "facessi", "tu": "facessi", "lei": "facesse", "lui": "facesse", "noi": "facessimo", "voi": "faceste",
            "loro": "facessero"}

    # this section checks for the irregular verbs fare, andare
    if verb in irregular_are:
        if verb == "fare":
            return fare[pronoun]

    # this section checks for spelling issues like with mancare in order to preserve hard "k" sound of infinitive
    # if it's a verb like mancare then the if section adds an "h" for the spelling to preserve hard "k" sound
    # if it's a normal -are verb, then the else section conjugates it normally

    stripped_verb = strip_off_ending(verb, tense)
    new_verb = stripped_verb + are_endings[pronoun]
    return new_verb


def conjugate_subjunctiveimp_ere_verb(verb, pronoun, tense):
    ere_endings = {"io": "essi", "tu": "essi", "lei": "esse", "lui": "esse", "noi": "essimo", "voi": "este",
                   "loro": "essero"}
    compiere_endings = {"io": "ssi", "tu": "ssi", "lei": "sse", "lui": "sse", "noi": "ssimo", "voi": "ste",
                        "loro": "ssero"}
    irregular_verb = ["essere", "compiere"]
    essere = {"io": "fossi", "tu": "fossi", "lei": "fosse", "lui": "fosse", "noi": "fossimo", "voi": "foste",
              "loro": "fossero"}

    if verb[-3:] != "ere":
        raise ValueError
    if verb in irregular_verb:
        if verb == "essere":
            return essere[pronoun]
        if verb == "compiere":
            stripped_verb = strip_off_ending(verb, tense)
            new_verb = stripped_verb + compiere_endings[pronoun]
            return new_verb
    else:
        stripped_verb = strip_off_ending(verb, tense)
        new_verb = stripped_verb + ere_endings[pronoun]
        return new_verb


def conjugate_subjunctiveimp_ire_verb(verb, pronoun, tense):
    ending = verb_ending(verb)
    if ending != "ire":
        raise TypeError

    ere_endings = {"io": "issi", "tu": "issi", "lei": "isse", "lui": "isse", "noi": "issimo", "voi": "iste",
                   "loro": "issero"}
    irregulars = ["dire"]
    dire = {"io": "dicessi", "tu": "dicessi", "lei": "dicesse", "lui": "dicesse", "noi": "dicessimo", "voi": "diceste",
            "loro": "dicessero"}

    if verb in irregulars:
        if verb == "dire":
            return dire[pronoun]
    stripped_verb = strip_off_ending(verb, tense)
    new_verb = stripped_verb + ere_endings[pronoun]
    return new_verb


# test functions

def review_verb(verb):
    ending = verb_ending(verb)
    if not ending:
        raise ValueError
    pronouns = ["io", "tu", "lei", "lui", "noi", "voi", "loro"]
    if ending == "are":
        print(f'{verb} present tense\n' + '********')
        for pronoun in pronouns:
            present = conjugate_present_are_verb(verb, pronoun, "presente")
            print(f'{pronoun} {present}')
        print('\n' + f'{verb} imperfect tense\n' + '********')
        for pronoun in pronouns:
            imperfect = conjugate_imperfect_are_verb(verb, pronoun, "imperfetto")
            print(f'{pronoun} {imperfect}')
        print('\n' + f'{verb} future tense\n' + '********')
        for pronoun in pronouns:
            future = conjugate_future_are_ere_verb(verb, pronoun, "futuro")
            print(f'{pronoun} {future}')
        print('\n' + f'{verb} subjunctive present tense\n' + '********')
        for pronoun in pronouns:
            subjpr = conjugate_subjunctivepr_are_verb(verb, pronoun, "congiuntivopr")
            print(f'{pronoun} {subjpr}')
        print('\n' + f'{verb} subjunctive imperfect tense\n' + '********')
        for pronoun in pronouns:
            subjimp = conjugate_subjunctiveimp_are_verb(verb, pronoun, "congiuntivoimp")
            print(f'{pronoun} {subjimp}')
        print('\n' + f'{verb} conditional present tense\n' + '********')
        for pronoun in pronouns:
            conditional = conjugate_conditionalpr_are_ere_verb(verb, pronoun, "condizionale")
            print(f'{pronoun} {conditional}')
    if ending == "ere":
        print(f'{verb} present tense\n' + '********')
        for pronoun in pronouns:
            present = conjugate_present_ere_verb(verb, pronoun, "presente")
            print(f'{pronoun} {present}')
        print('\n' + f'{verb} imperfect tense\n' + '********')
        for pronoun in pronouns:
            imperfect = conjugate_imperfect_ere_verb(verb, pronoun, "imperfetto")
            print(f'{pronoun} {imperfect}')
        print('\n' + f'{verb} future tense\n' + '********')
        for pronoun in pronouns:
            future = conjugate_future_are_ere_verb(verb, pronoun, "futuro")
            print(f'{pronoun} {future}')
        print('\n' + f'{verb} subjunctive present tense\n' + '********')
        for pronoun in pronouns:
            subjpr = conjugate_subjunctivepr_ere_verb(verb, pronoun, "congiuntivopr")
            print(f'{pronoun} {subjpr}')
        print('\n' + f'{verb} subjunctive imperfect tense\n' + '********')
        for pronoun in pronouns:
            subjimp = conjugate_subjunctiveimp_ere_verb(verb, pronoun, "congiuntivoimp")
            print(f'{pronoun} {subjimp}')
        print('\n' + f'{verb} conditional present tense\n' + '********')
        for pronoun in pronouns:
            conditional = conjugate_conditionalpr_are_ere_verb(verb, pronoun, "condizionale")
            print(f'{pronoun} {conditional}')
    if ending == "ire":
        print(f'{verb} present tense\n' + '********')
        for pronoun in pronouns:
            present = conjugate_present_ire_verb(verb, pronoun, "presente")
            print(f'{pronoun} {present}')
        print('\n' + f'{verb} imperfect tense\n' + '********')
        for pronoun in pronouns:
            imperfect = conjugate_imperfect_ire_verb(verb, pronoun, "imperfetto")
            print(f'{pronoun} {imperfect}')
        print('\n' + f'{verb} future tense\n' + '********')
        for pronoun in pronouns:
            future = conjugate_future_ire_verb(verb, pronoun, "futuro")
            print(f'{pronoun} {future}')
        print('\n' + f'{verb} subjunctive present tense\n' + '********')
        for pronoun in pronouns:
            subjpr = conjugate_subjunctivepr_ire_verb(verb, pronoun, "congiuntivopr")
            print(f'{pronoun} {subjpr}')
        print('\n' + f'{verb} subjunctive imperfect tense\n' + '********')
        for pronoun in pronouns:
            subjimp = conjugate_subjunctiveimp_ire_verb(verb, pronoun, "congiuntivoimp")
            print(f'{pronoun} {subjimp}')
        print('\n' + f'{verb} conditional present tense\n' + '********')
        for pronoun in pronouns:
            conditional = conjugate_conditionalpr_ire_verb(verb, pronoun, "condizionale")
            print(f'{pronoun} {conditional}')


# api_call_tracker()
# print(conjugate_subjunctivepr_ire_verb("uscire", "loro", "presente"))
# review_verb("compiere")
# print(conjugate_conditionalpr_are_ere_verb("cambiare", "noi", "presente"))
# review_verb('mangiare')

print(conjugate_subjunctiveimp_are_verb('mangiare', 'loro', 'congiuntivoimp'))
