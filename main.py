import json

with open('data.json', 'r', encoding='utf-8') as f:
    donnees_json = json.load(f)

def obtenir_reponse(question):
    question = question.lower()

    for cle in donnees_json:
        if cle in question:
            return donnees_json[cle]

    return "Désolé, je n'ai pas compris votre question."

if __name__ == "__main__":
    while True:
        question = input("Vous: ")

        if question.lower() in ['exit', 'quit']:
            print("Au revoir!")
            break

        reponse = obtenir_reponse(question)
        print("Chatbot:", reponse)
