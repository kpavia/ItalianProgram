import functions
import quizzes

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


# just commented out for testing
# code to start verb conjugator (no quizing, just display)
# starting = True
# while starting:
#     begin()
#     another = input("Choose another verb? y/n\n").lower()
#     if another == "n":
#         starting = False

# code to start quizzing section
quizzes.begin()

