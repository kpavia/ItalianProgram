import functions
import random

pronouns = ["io", "tu", "lei", "lui", "noi", "voi", "loro"]
tenses = ["presente", "imperfetto", "futuro", "condizionale presente", "condizionale imperfetto"]
are_verb_options = ["mangiare", "lavorare", "andare", "fare", "caminare", "abandonare", "portare", "cambiare",
                    "contare", "tagliare", "disegnare", "guidare", "spiegare", "trovare", "ritornare", "imparare",
                    "guardare", "organizzare", "pagare", "giocare", "ascoltare", "cantare", "fumare", "parlare",
                    "chiamare", "pensare"]
ere_verb_options = ["scrivere", "leggere", "prendere", "chiedere", "decidere", "conoscere", "mettere", "vincere",
                    "perdere", "credere", "sedere"]
ire_verb_options = ["finire", "pulire", "partire", "dormire", "costruire", "capire", "offrire", "seguire", "construire",
                    "aprire", "sentire", "uscire", "salire"]


# TODO: create logger to record progress (incorrect answers, correct answers, most common missed ones, etc.)
# TODO: create complete random quizzes for all tenses
# TODO: update -are, -ere combined quizzes to select from both -are, -ere verbs
# TODO: finish subjunctive -ere, -ire quizzes

# comprehensive quizzes


def random_present_quiz_selector():
    """
    This function randomly selects the -are, -ere-, or -ire quiz and once the user decides not to continue, checks to
    see if the user wants to try another verb type. If not, then the quiz ends.
    """

    go_again = True
    while go_again:
        number = random.randint(1, 3)
        if number == 1:
            begin_present_are_quiz()
        if number == 2:
            begin_present_ere_quiz()
        if number == 3:
            begin_present_ire_quiz()
        again = input("Continue? Y/N\n").lower()
        if again == "n":
            go_again = False


def random_imperfect_quiz_selector():
    """
    This function randomly selects the -are, -ere-, or -ire quiz and once the user decides not to continue, checks to
    see if the user wants to try andother verb type. If not, then the quiz ends.
    """

    go_again = True
    while go_again:
        number = random.randint(1, 3)
        if number == 1:
            begin_imperfect_are_quiz()
        if number == 2:
            begin_imperfect_ere_quiz()
        if number == 3:
            begin_imperfect_ire_quiz()
        again = input("Continue? Y/N\n").lower()
        if again == "n":
            go_again = False


def random_future_quiz_selector():
    """
    This function randomly selects the -are, -ere-, or -ire quiz and once the user decides not to continue, checks to
    see if the user wants to try another verb type. If not, then the quiz ends.
    """

    go_again = True
    while go_again:
        number = random.randint(1, 2)
        if number == 1:
            begin_future_are_ere_quiz()
        if number == 2:
            begin_present_ire_quiz()
        again = input("Continue? Y/N\n").lower()
        if again == "n":
            go_again = False


def random_conditional_quiz_selector():
    """
    This function randomly selects the -are, -ere-, or -ire quiz and once the user decides not to continue, checks to
    see if the user wants to try another verb type. If not, then the quiz ends.
    """

    go_again = True
    while go_again:
        number = random.randint(1, 2)
        if number == 1:
            begin_conditionalpr_are_ere_quiz()
        if number == 2:
            begin_conditionalpr_ire_quiz()
        again = input("Continue? Y/N\n").lower()
        if again == "n":
            go_again = False


def random_subjunctive_quiz_selector():
    """
    This function randomly selects the -are, -ere-, or -ire quiz and once the user decides not to continue, checks to
    see if the user wants to try another verb type. If not, then the quiz ends.
    """
    # TODO: finish the -ere, -ire quizzes

    go_again = True
    while go_again:
        number = random.randint(1, 3)
        if number == 1:
            begin_subjunctiveimp_are_quiz()
        # if number == 2:
        #     begin_subj
        # if number == 3:
        #     begin_present_ire_quiz()
        again = input("Continue? Y/N\n").lower()
        if again == "n":
            go_again = False
# quiz functions


def begin_present_are_quiz():
    """
    This function runs the present tense quiz for -are verbs.
    Verbs are randomly selected from a list.
    """

    print("Get ready for a quiz.\nInstructions: You'll be shown a verb and a pronoun. Conjugate it in the present tense"
          ".\n")
    verb_good = False
    verb = ""
    pronoun = ""
    go_again = True
    while go_again:
        while not verb_good:
            verb = random.choice(are_verb_options)
            checker = functions.verb_ending_good(verb)
            if checker is True:
                verb_good = True
        pronoun_good = False
        while not pronoun_good:
            pronoun = random.choice(pronouns)
            if pronoun in pronouns:
                pronoun_good = True
        ending = functions.verb_ending(verb)
        if ending == "are":
            answer = are_present_quiz(verb, pronoun)
            checker = input(f'Tense: Presente \nVerb: {verb} \nPronoun: {pronoun}...\n')
            if answer == checker:
                print("Correct!")
            else:
                print(f'Incorrect.\nCorrect answer is {answer}')
        another = input("Go again? y/n\n").lower()
        if another != "y":
            go_again = False
            print("Quiz over.")
        else:
            verb_good = False


def begin_present_ere_quiz():
    """
    This function runs the present tense quiz for -ere verbs.
    Verbs are randomly selected from a list.
    """

    print("Get ready for a quiz.\nInstructions: You'll be shown a verb and a pronoun. Conjugate it in the present tense"
          ".\n")
    verb_good = False
    verb = ""
    pronoun = ""
    go_again = True
    while go_again:
        while not verb_good:
            verb = random.choice(ere_verb_options)
            checker = functions.verb_ending_good(verb)
            if checker is True:
                verb_good = True
        pronoun_good = False
        while not pronoun_good:
            pronoun = random.choice(pronouns)
            if pronoun in pronouns:
                pronoun_good = True
        ending = functions.verb_ending(verb)
        if ending == "ere":
            answer = ere_present_quiz(verb, pronoun)
            checker = input(f'Tense: Presente \nVerb: {verb} \nPronoun: {pronoun}...\n')
            if answer == checker:
                print("Correct!")
            else:
                print(f'Incorrect.\nCorrect answer is {answer}')
        another = input("Go again? y/n\n").lower()
        if another != "y":
            go_again = False
            print("Quiz over.")
        else:
            verb_good = False


def begin_present_ire_quiz():
    """
    This functions runs the present tense -ire quiz.
    Verbs are randomly selected from a list.
    """

    print("Get ready for a quiz.\nInstructions: You'll be shown a verb and a pronoun. Conjugate it in the present tense"
          ".\n")
    verb_good = False
    verb = ""
    pronoun = ""
    go_again = True
    while go_again:
        while not verb_good:
            verb = random.choice(ire_verb_options)
            checker = functions.verb_ending_good(verb)
            if checker is True:
                verb_good = True
        pronoun_good = False
        while not pronoun_good:
            pronoun = random.choice(pronouns)
            if pronoun in pronouns:
                pronoun_good = True
        ending = functions.verb_ending(verb)
        if ending == "ire":
            answer = ire_present_quiz(verb, pronoun)
            checker = input(f'Tense: Presente \nVerb: {verb} \nPronoun: {pronoun}...\n')
            if answer == checker:
                print("Correct!")
            else:
                print(f'Incorrect.\nCorrect answer is {answer}')
        another = input("Go again? y/n\n").lower()
        if another != "y":
            go_again = False
            print("Quiz over.")
        else:
            verb_good = False


def begin_imperfect_are_quiz():
    """
    This function runs the quiz for -are verbs in the imperfect tense.
    Verbs are randomly selected from a list.
    """

    print("Get ready for a quiz.\nInstructions: You'll be shown a verb and a pronoun. Conjugate it in the imperfect "
          "tense"
          ".\n")
    verb_good = False
    verb = ""
    pronoun = ""
    go_again = True
    while go_again:
        while not verb_good:
            verb = random.choice(are_verb_options)
            checker = functions.verb_ending_good(verb)
            if checker is True:
                verb_good = True
        pronoun_good = False
        while not pronoun_good:
            pronoun = random.choice(pronouns)
            if pronoun in pronouns:
                pronoun_good = True
        ending = functions.verb_ending(verb)
        if ending == "are":
            answer = are_imperfect_quiz(verb, pronoun)
            checker = input(f'Tense: Imperfetto \nVerb: {verb} \nPronoun: {pronoun}...\n')
            if answer == checker:
                print("Correct!")
            else:
                print(f'Incorrect.\nCorrect answer is {answer}')
        another = input("Go again? y/n\n").lower()
        if another != "y":
            go_again = False
            print("Quiz over.")
        else:
            verb_good = False


def begin_imperfect_ere_quiz():
    """
    This function runs the quiz for -ere verbs in the imperfect tense.
    Verbs are randomly selected from a list.
    """

    print("Get ready for a quiz.\nInstructions: You'll be shown a verb and a pronoun. Conjugate it in the imperfect "
          "tense"
          ".\n")
    verb_good = False
    verb = ""
    pronoun = ""
    go_again = True
    while go_again:
        while not verb_good:
            verb = random.choice(ere_verb_options)
            checker = functions.verb_ending_good(verb)
            if checker is True:
                verb_good = True
        pronoun_good = False
        while not pronoun_good:
            pronoun = random.choice(pronouns)
            if pronoun in pronouns:
                pronoun_good = True
        ending = functions.verb_ending(verb)
        if ending == "ere":
            answer = ere_imperfect_quiz(verb, pronoun)
            checker = input(f'Tense: Imperfetto \nVerb: {verb} \nPronoun: {pronoun}...\n')
            if answer == checker:
                print("Correct!")
            else:
                print(f'Incorrect.\nCorrect answer is {answer}')
        another = input("Go again? y/n\n").lower()
        if another != "y":
            go_again = False
            print("Quiz over.")
        else:
            verb_good = False


def begin_imperfect_ire_quiz():
    """
    This function runs the quiz for -ire verbs in the imperfect tense.
    Verbs are randomly selected from a list.
    """

    print("Get ready for a quiz.\nInstructions: You'll be shown a verb and a pronoun. Conjugate it in the imperfect "
          "tense"
          ".\n")
    verb_good = False
    verb = ""
    pronoun = ""
    go_again = True
    while go_again:
        while not verb_good:
            verb = random.choice(ire_verb_options)
            checker = functions.verb_ending_good(verb)
            if checker is True:
                verb_good = True
        pronoun_good = False
        while not pronoun_good:
            pronoun = random.choice(pronouns)
            if pronoun in pronouns:
                pronoun_good = True
        ending = functions.verb_ending(verb)
        if ending == "ire":
            answer = ire_imperfect_quiz(verb, pronoun)
            checker = input(f'Tense: Imperfetto \nVerb: {verb} \nPronoun: {pronoun}...\n')
            if answer == checker:
                print("Correct!")
            else:
                print(f'Incorrect.\nCorrect answer is {answer}')
        another = input("Go again? y/n\n").lower()
        if another != "y":
            go_again = False
            print("Quiz over.")
        else:
            verb_good = False


def begin_conditionalpr_ire_quiz():
    """
    This runs the present conditional quiz for -ire verbs.
    Verbs are randomly selected from a list.
    """

    print("Get ready for a quiz.\nInstructions: You'll be shown a verb and a pronoun. Conjugate it in the "
          "conditional present tense.\n")
    verb_good = False
    verb = ""
    pronoun = ""
    go_again = True
    while go_again:
        while not verb_good:
            verb = random.choice(ire_verb_options)
            checker = functions.verb_ending_good(verb)
            if checker is True:
                verb_good = True
        pronoun_good = False
        while not pronoun_good:
            pronoun = random.choice(pronouns)
            if pronoun in pronouns:
                pronoun_good = True
        ending = functions.verb_ending(verb)
        if ending == "ire":
            answer = ire_conditionalpr_quiz(verb, pronoun)
            checker = input(f'Tense: Condizionale \nVerb: {verb} \nPronoun: {pronoun}...\n')
            if answer == checker:
                print("Correct!")
            else:
                print(f'Incorrect.\nCorrect answer is {answer}')
        another = input("Go again? y/n\n").lower()
        if another != "y":
            go_again = False
            print("Quiz over.")
        else:
            verb_good = False


def begin_conditionalpr_are_ere_quiz():
    """
    This function runs the present conditional tense quiz for -are, -ere verbs.
    Verbs are randomly selected from a list.
    """

    print("Get ready for a quiz.\nInstructions: You'll be shown a verb and a pronoun. Conjugate it in the "
          "present conditional tense"
          ".\n")
    verb_good = False
    verb = ""
    pronoun = ""
    go_again = True
    while go_again:
        while not verb_good:
            ere_or_are = random.randint(1, 2)
            if ere_or_are == 1:
                verb = random.choice(are_verb_options)
            else:
                verb = random.choice(ere_verb_options)
            checker = functions.verb_ending_good(verb)
            if checker is True:
                verb_good = True
        pronoun_good = False
        while not pronoun_good:
            pronoun = random.choice(pronouns)
            if pronoun in pronouns:
                pronoun_good = True
        ending = functions.verb_ending(verb)
        if ending == "are" or "ere":
            answer = are_ere_conditionalpr_quiz(verb, pronoun)
            checker = input(f'Tense: Condizionale Presente \nVerb: {verb} \nPronoun: {pronoun}...\n')
            if answer == checker:
                print("Correct!")
            else:
                print(f'Incorrect.\nCorrect answer is {answer}')
        another = input("Go again? y/n\n").lower()
        if another != "y":
            go_again = False
            print("Quiz over.")
        else:
            verb_good = False


def begin_subjunctiveimp_are_quiz():
    """
    This function runs the subjunctive imperfect quiz for -are verbs.
    Verbs are randomly selected from a list.
    """

    print("Get ready for a quiz.\nInstructions: You'll be shown a verb and a pronoun. Conjugate it in the imperfect "
          "subjunctive tense"
          ".\n")
    verb_good = False
    verb = ""
    pronoun = ""
    go_again = True
    while go_again:
        while not verb_good:
            verb = random.choice(are_verb_options)
            checker = functions.verb_ending_good(verb)
            if checker is True:
                verb_good = True
        pronoun_good = False
        while not pronoun_good:
            pronoun = random.choice(pronouns)
            if pronoun in pronouns:
                pronoun_good = True
        ending = functions.verb_ending(verb)
        if ending == "are":
            answer = are_subjunctiveimp_quiz(verb, pronoun)
            checker = input(f'Tense: Congiuntivo Imperfetto \nVerb: {verb} \nPronoun: {pronoun}...\n')
            if answer == checker:
                print("Correct!")
            else:
                print(f'Incorrect.\nCorrect answer is {answer}')
        another = input("Go again? y/n\n").lower()
        if another != "y":
            go_again = False
            print("Quiz over.")
        else:
            verb_good = False


def begin_future_are_ere_quiz():
    """
    This function does the future tense quiz for -are, -ere verbs.
    Verbs are randomly selected from a list.

    """
    print("Get ready for a quiz.\nInstructions: You'll be shown a verb and a pronoun. Conjugate it in the future "
          "tense"
          ".\n")
    verb_good = False
    verb = ""
    pronoun = ""
    go_again = True
    while go_again:
        while not verb_good:
            verb = random.choice(are_verb_options)
            checker = functions.verb_ending_good(verb)
            if checker is True:
                verb_good = True
        pronoun_good = False
        while not pronoun_good:
            pronoun = random.choice(pronouns)
            if pronoun in pronouns:
                pronoun_good = True
        ending = functions.verb_ending(verb)
        if ending == "are":
            answer = are_ere_future_quiz(verb, pronoun)
            checker = input(f'Tense: Futuro \nVerb: {verb} \nPronoun: {pronoun}...\n')
            if answer == checker:
                print("Correct!")
            else:
                print(f'Incorrect.\nCorrect answer is {answer}')
        another = input("Go again? y/n\n").lower()
        if another != "y":
            go_again = False
            print("Quiz over.")
        else:
            verb_good = False


def begin_future_ire_quiz():
    """
    This function runs the quiz for -ire verbs in the future tense.
    Verbs are randomly selected from a list.
    """

    print("Get ready for a quiz.\nInstructions: You'll be shown a verb and a pronoun. Conjugate it in the future "
          "tense"
          ".\n")
    verb_good = False
    verb = ""
    pronoun = ""
    go_again = True
    while go_again:
        while not verb_good:
            verb = random.choice(ire_verb_options)
            checker = functions.verb_ending_good(verb)
            if checker is True:
                verb_good = True
        pronoun_good = False
        while not pronoun_good:
            pronoun = random.choice(pronouns)
            if pronoun in pronouns:
                pronoun_good = True
        ending = functions.verb_ending(verb)
        if ending == "ire":
            answer = ire_future_quiz(verb, pronoun)
            checker = input(f'Tense: Futuro \nVerb: {verb} \nPronoun: {pronoun}...\n')
            if answer == checker:
                print("Correct!")
            else:
                print(f'Incorrect.\nCorrect answer is {answer}')
        another = input("Go again? y/n\n").lower()
        if another != "y":
            go_again = False
            print("Quiz over.")
        else:
            verb_good = False


# functions that call conjugating functions


def are_present_quiz(verb, pronoun):
    """
    This function is used by the -are quiz function to call the conjugation functions from functions.py
    Parameters: verb is a string, pronoun is a string
    Returns: a string (the conjugated verb)
    """

    return functions.conjugate_present_are_verb(verb, pronoun, "presente")


def ere_present_quiz(verb, pronoun):
    """
    This function is used by the -ere quiz function to call the conjugation functions from functions.py
    Parameters: verb is a string, pronoun is a string
    Returns: a string (the conjugated verb)
    """
    return functions.conjugate_present_ere_verb(verb, pronoun, "presente")


def ire_present_quiz(verb, pronoun):
    """
    This function is used by the -ire quiz function to call the conjugation functions from functions.py
    Parameters: verb is a string, pronoun is a string
    Returns: a string (the conjugated verb)
    """
    return functions.conjugate_present_ire_verb(verb, pronoun, "presente")


def are_imperfect_quiz(verb, pronoun):
    """
    This function is used by the -are imperfect quiz function to call the conjugation functions from functions.py
    Parameters: verb is a string, pronoun is a string
    Returns: a string (the conjugated verb)
    """

    return functions.conjugate_imperfect_are_verb(verb, pronoun, "imperfetto")


def ere_imperfect_quiz(verb, pronoun):
    """
    This function is used by the -ere imperfect quiz function to call the conjugation functions from functions.py
    Parameters: verb is a string, pronoun is a string
    Returns: a string (the conjugated verb)
    """

    return functions.conjugate_imperfect_ere_verb(verb, pronoun, "imperfetto")


def ire_imperfect_quiz(verb, pronoun):
    """
    This function is used by the -ire imperfect quiz function to call the conjugation functions from functions.py
    Parameters: verb is a string, pronoun is a string
    Returns: a string (the conjugated verb)
    """

    return functions.conjugate_imperfect_ire_verb(verb, pronoun, "imperfetto")


def are_ere_conditionalpr_quiz(verb, pronoun):
    """
    This function is used by the -are, -ere present conditional
    quiz function to call the conjugation functions from functions.py
    Parameters: verb is a string, pronoun is a string
    Returns: a string (the conjugated verb)
    """
    return functions.conjugate_conditionalpr_are_ere_verb(verb, pronoun, "condizionale")


def ire_conditionalpr_quiz(verb, pronoun):
    """
    This function is used by the -ire present conditional
    quiz function to call the conjugation functions from functions.py
    Parameters: verb is a string, pronoun is a string
    Returns: a string (the conjugated verb)
    """
    return functions.conjugate_conditionalpr_ire_verb(verb, pronoun, "condizionale")


def are_subjunctiveimp_quiz(verb, pronoun):
    """
    This function is used by the -are imperfect subjunctive
    quiz function to call the conjugation functions from functions.py
    Parameters: verb is a string, pronoun is a string
    Returns: a string (the conjugated verb)
    """
    return functions.conjugate_subjunctiveimp_are_verb(verb, pronoun, "congiuntivo")


def ere_subjunctiveimp_quiz(verb, pronoun):
    """
    This function is used by the -ere imperfect subjunctive
    quiz function to call the conjugation functions from functions.py
    Parameters: verb is a string, pronoun is a string
    Returns: a string (the conjugated verb)
    """
    return functions.conjugate_subjunctiveimp_ere_verb(verb, pronoun, "congiuntivo")


def ire_subjunctiveimp_quiz(verb, pronoun):
    """
    This function is used by the -ire imperfect subjunctive
    quiz function to call the conjugation functions from functions.py
    Parameters: verb is a string, pronoun is a string
    Returns: a string (the conjugated verb)
    """
    return functions.conjugate_subjunctiveimp_ire_verb(verb, pronoun, "congiuntivo")


def are_subjunctivepr_quiz(verb, pronoun):
    """
    This function is used by the -ere imperfect subjunctive
    quiz function to call the conjugation functions from functions.py
    Parameters: verb is a string, pronoun is a string
    Returns: a string (the conjugated verb)
    """
    return functions.conjugate_subjunctivepr_ere_verb(verb, pronoun, "congiuntivo")


def ere_subjunctivepr_quiz(verb, pronoun):
    """
    This function is used by the -ere imperfect subjunctive
    quiz function to call the conjugation functions from functions.py
    Parameters: verb is a string, pronoun is a string
    Returns: a string (the conjugated verb)
    """
    return functions.conjugate_subjunctivepr_ere_verb(verb, pronoun, "congiuntivo")


def ire_subjunctivepr_quiz(verb, pronoun):
    """
    This function is used by the -ire imperfect subjunctive
    quiz function to call the conjugation functions from functions.py
    Parameters: verb is a string, pronoun is a string
    Returns: a string (the conjugated verb)
    """
    return functions.conjugate_subjunctivepr_ere_verb(verb, pronoun, "congiuntivo")


def are_ere_future_quiz(verb, pronoun):
    """
    This function is used by the -are, -ere future quiz function to call the conjugation functions from functions.py
    Parameters: verb is a string, pronoun is a string
    Returns: a string (the conjugated verb)
    """
    return functions.conjugate_future_are_ere_verb(verb, pronoun, "futuro")


def ire_future_quiz(verb, pronoun):
    """
    This function is used by the -ire future quiz function to call the conjugation functions from functions.py
    Parameters: verb is a string, pronoun is a string
    Returns: a string (the conjugated verb)
    """
    return functions.conjugate_future_ire_verb(verb, pronoun, "futuro")

