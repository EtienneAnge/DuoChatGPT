import os
import openai

keyFile = open('key.txt', 'r+')
key = keyFile.read().strip()

if(key == ""):
    key = input("Please enter your OpenAI key: ")
    keyFile.write(key)

keyFile.close()
print("your key is: " + key)

openai.api_key = key
#openai.api_key = os.getenv("OPENAI_API_KEY")


def completion(prompt):
    response = openai.Completion.create(
    model="text-davinci-003",
    prompt=prompt,
    temperature=0.7,
    max_tokens=400,
    top_p=1,
    frequency_penalty=0.5,
    presence_penalty=0
    )
    return response.choices[0].text



def duochat(story_title):
    filename = "histoires/" + story_title + ".txt"
    with open(filename, "r") as f:
      prompt = f.read()
    ai = story_title
    print("ia :", ai)

    while True:
        input_user = input("\nVous: ")
        prompt = prompt + "\nPersonne: " + input_user + "\n" + ai + ":"

        ans = completion(prompt)
        print("\n" + ai + ":" + ans)
        prompt = prompt + ans

def write_story(story_title, story_text):
    # Crée un fichier avec le titre de l'histoire comme nom, dans le répertoire 'histoires'
    filename = "histoires/" + story_title + ".txt"
    with open(filename, "w+") as f:
        # Écrit le titre de l'histoire et le texte dans le fichier
        f.write(story_title + "\n\n")
        f.write(story_text)

def delete_story(story_title):
    # Supprime le fichier avec le titre de l'histoire comme nom, dans le répertoire 'histoires'
    filename = "histoires/" + story_title + ".txt"
    os.remove(filename)
    print("l'histoire: " + filename + "a bien été suprimé")

def retrieve_stories():
    # Récupère la liste de tous les fichiers dans le répertoire 'histoires'
    files = os.listdir("histoires/")
    # Filtre la liste pour ne garder que les fichiers .txt
    txt_files = [f for f in files if f.endswith(".txt")]
    stories = []
    # Pour chaque fichier .txt, ouvre le fichier et ajoute son contenu à la liste 'stories'
    for txt_file in txt_files:
        with open("histoires/" + txt_file, "r") as f:
            stories.append(f.read())
            stories.append("\n\n")
    return stories

def read_stories(stories):
    # Affiche chaque histoire dans la liste
    for story in stories:
        print(story)

# Menu permettant à l'utilisateur de choisir une action à réaliser
os.system("clear")
while True:
    print("\n1. Ajouter un personnage")
    print("2. Supprimer un personnage")
    print("3. Lire tout les personnages")
    print("4. lancer la conversation")
    print("5. Quitter")
    choice = input("Choisissez une option: ")

    if choice == "1":
        # Demander le titre et le texte de l'histoire à l'utilisateur
        os.system("clear")
        print("Exemple:\nNom du personnage: Harry Potter")
        print("Détail du personnage: Harry Potter est le personnage principale du roman de J. K. Rowling (il est important de situer le personnage)")
        print("Harry Potter vient juste de vaincre Voldemort (n'hesitez pas à donner des instructions au context et a être très précis)")
        story_title = input("\nNom du personnage: ")
        story_text = input("Détail du personnage: ")
        # Écrire l'histoire
        write_story(story_title, story_text)

    elif choice == "2":
        os.system("clear")
        # Récupère la liste de tous les fichiers dans le répertoire 'histoires'
        files = os.listdir("histoires/")
        # Filtre la liste pour ne garder que les fichiers .txt
        txt_files = [f for f in files if f.endswith(".txt")]
        print(txt_files)
        # Demander le titre de l'histoire à l'utilisateur
        story_title = input("Quel personnage voulez-vous supprimer: ")
        # Supprimer l'histoire
        delete_story(story_title)

    elif choice == "3":
        os.system("clear")
        # Récupérer toutes les histoires
        stories = retrieve_stories()
        # Afficher toutes les histoires
        read_stories(stories)

    elif choice == "4":
        os.system("clear")
        print("Voici tout les personnes enregirstré:")
        # Récupère la liste de tous les fichiers dans le répertoire 'histoires'
        files = os.listdir("histoires/")
        # Filtre la liste pour ne garder que les fichiers .txt
        txt_files = [f for f in files if f.endswith(".txt")]
        for filename in txt_files:
            filename_without_extension = os.path.splitext(filename)[0]
            print(filename_without_extension)
        # Demander le titre de l'histoire à l'utilisateur
        story_title = input("\nAvec quel personnage voulez-vous lancer le dialogue: ")
        duochat(story_title)

    elif choice == "5":
        exit()
    else:
        os.system("clear")
        print("choix incorrecte")