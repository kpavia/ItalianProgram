import functions
import quizzes
import requests

irregular_ere = ["avere", "essere", "potere", "volere", "sapere", "bere"]
irregular_ire = ["uscire", "dire", "venire"]
mangiare = dict({"verb": "Mangiare", "translation": "to eat"})
mangiare["presente"] = {"io": "mangio", "tu": "mangi", "lui": "mangia", "lei": "mangia", "noi": "mangiamo",
                        "voi": "mangiate", "loro": "mangiano"}
mangiare["imperfetto"] = {"io": "mangiavo", "tu": "mangiavi", "lui": "mangiava", "lei": "mangiava", "noi": "mangiavamo",
                          "voi": "mangiavate", "loro": "mangiavano"}
mangiare["futuro"] = {"io": "mangierò", "tu": "mangerai", "lui": "mangerà", "lei": "mangerà", "noi": "mangeremo",
                      "voi": "mangerete", "loro": "mangeranno"}

api_key = "PVj9iCBg4ec50k9ecMQyrtMdSoTWHCSGljxzOyQLwjZZXRAOp9VnmEwuAsrWUIt7"
italian_english_url = "http://api.collinsdictionary.com/api/v1/dictionaries/italian-english/"
english_italian_url = "http://api.collinsdictionary.com/api/v1/dictionaries/english-italian/"

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
# quizzes.begin()

# verb_file = open("lavorare.txt", "w")
# verb_file.write(functions.create_verb_dict("lavorare", "presente"))
# verb_file.close()

# functions.create_verb_file("fare", "presente")

def api_call():
    functions.api_call_tracker()
    call = requests.get(italian_english_url + "italian-english")
    print(call)
    print("done")


api_call()

