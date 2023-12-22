from flask import Flask, render_template, request, redirect, url_for, jsonify
import pandas as pd

app = Flask(__name__)

all_words = {}      # Dictionnaire pour toutes les cartes
known_words = {}    # Dictionnaire pour les cartes connues

# Page d'accueil
@app.route('/')
def index():
    return render_template('index.html')

# Route pour le traitement du fichier Excel
@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return redirect(request.url)

    file = request.files['file']

    if file.filename == '':
        return redirect(request.url)

    if file:
        convert_excel_to_flashcards(file)
        flashcards = list(all_words.keys())  # Liste de tous les mots
        return render_template('study.html', flashcards=flashcards, all_words=all_words)


# Nouvelle route pour traiter la réponse de l'utilisateur
@app.route('/submit_response', methods=['POST'])
def submit_response():
    data = request.get_json()
    word = data['word']
    response = data['response']

    if response == 'known':
        known_words[word] = all_words[word]
    else:
        known_words.pop(word, None)

    return jsonify(success=True)

# Fonction pour convertir le fichier Excel en flashcards
def convert_excel_to_flashcards(file):
    global all_words, known_words  # Accès aux variables globales

    # Charger le fichier Excel
    df = pd.read_excel(file)

    # Convertir les données en format de flashcards
    for index, row in df.iterrows():
        word = row.iloc[0]         # Première colonne (indice 0) pour les mots
        definition = row.iloc[2]   # Troisième colonne (indice 2) pour les définitions
        all_words[word] = definition

    known_words.clear()  # Réinitialiser le dictionnaire des mots connus

    return all_words

if __name__ == '__main__':
    app.run(debug=True)
