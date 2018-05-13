import functions
import random

pronouns = ["io", "tu", "lei", "lui", "noi", "voi", "loro"]
tenses = ["presente", "imperfetto", "futuro", "condizionale presente", "condizionale imperfetto"]
verb_options = ["mangiare", "lavorare", "andare", "fare", "caminare", "abandonare", "portare", "cambiare", "contare",
                "tagliare", "disegnare", "guidare", "spiegare", "trovare", "ritornare", "imparare", "guardare",
                "organizzare", "pagare", "giocare", "ascoltare", "cantare", "fumare", "parlare"]

# TODO: create logger to record progress (incorrect answers, correct answers, most common missed ones, etc.)


def begin_present_are_quiz():

    print("Get ready for a quiz.\nInstructions: You'll be shown a verb and a pronoun. Conjugate it in the present tense"
          ".\n")
    verb_good = False
    verb = ""
    pronoun = ""
    go_again = True
    while go_again:
        while not verb_good:
            verb = random.choice(verb_options)
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


def are_present_quiz(verb, pronoun):
    return functions.conjugate_present_are_verb(verb, pronoun, "presente")



begin_present_are_quiz()

