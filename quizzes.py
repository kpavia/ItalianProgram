import functions

pronouns = ["io", "tu", "lei", "lui", "noi", "voi", "loro"]
tenses = ["presente", "imperfetto", "futuro", "condizionale presente", "condizionale imperfetto"]

# TODO: create logger to record progress (incorrect answers, correct answers, most commen missed ones, etc.)


def begin():

    print("Get ready for a quiz.\n")
    verb_good = False
    verb = ""
    tense = ""
    pronoun = ""
    go_again = True
    while go_again:
        while not verb_good:
            verb = input("What verb?\n").lower()
            checker = functions.verb_ending_good(verb)
            if checker is True:
                verb_good = True
            else:
                print("Please enter a verb.")
        tense_good = False
        while not tense_good:
            tense = input("What tense? Presente, Imperfetto, Futuro, etc.?\n").lower()
            if tense in tenses:
                tense_good = True
            else:
                print("Please enter a verb tense.")
        pronoun_good = False
        while not pronoun_good:
            pronoun = input("What pronoun?\n").lower()
            if pronoun in pronouns:
                pronoun_good = True
            else:
                print("Please enter a pronoun.")
        ending = functions.verb_ending(verb)
        if ending == "are" and tense == "presente":
            answer = are_present_quiz(verb, pronoun)
            checker = input(f'Presente tense, {verb}, {pronoun}...\n')
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
    return functions.conjugate_present_are_verb(verb, pronoun)


begin()
