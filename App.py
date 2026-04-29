from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

# Base de données des vêtements avec images, likes et albums photos
CLOTHES_DATABASE = {
    "Homme": [
        {
            "name": "T-shirt Cotton", "price": "15.000 Ar", 
            "img": "/static/T-shirt.PNG", "likes": 124, "dislikes": 5, 
            "album": ["/static/T-shirt.PNG", "/static/Jeans.PNG"]
        },
        {
            "name": "Pantalon Jeans", "price": "45.000 Ar", 
            "img": "/static/Jeans.PNG", "likes": 86, "dislikes": 2, 
            "album": ["/static/Jeans.PNG"]
        }
    ],
    "Femme": [
        {
            "name": "Robe longue", "price": "35.000 Ar", 
            "img": "/static/Robe femme.PNG", "likes": 210, "dislikes": 8, 
            "album": ["/static/Robe femme.PNG"]
        },
            {
            "name": "Robe longue", "price": "35.000 Ar", 
            "img": "/static/Robe femme1.PNG", "likes": 210, "dislikes": 8, 
            "album": ["/static/Robe femme1.PNG"]
        },
            {
            "name": "Robe longue", "price": "35.000 Ar", 
            "img": "/static/Robe femme2.PNG", "likes": 210, "dislikes": 8, 
            "album": ["/static/Robe femme2.PNG"]
        },
            {
            "name": "Robe longue", "price": "35.000 Ar", 
            "img": "/static/Robe femme3.PNG", "likes": 210, "dislikes": 8, 
            "album": ["/static/Robe femme3.PNG"]
        },
            {
            "name": "Jupe enfant", "price": "35.000 Ar", 
            "img": "/static/jupe enfant.PNG", "likes": 210, "dislikes": 8, 
            "album": ["/static/jupe enfant.PNG"]
        }
    ],
    "Jeune": [
        {
            "name": "Capuche Style", "price": "18.000 Ar", 
            "img": "/static/Capuche.PNG", "likes": 45, "dislikes": 3, 
            "album": ["/static/Capuche.PNG"]
        },
            {
            "name": "Capuche Style", "price": "18.000 Ar", 
            "img": "/static/Capuche1.PNG", "likes": 45, "dislikes": 3, 
            "album": ["/static/Capuche1.PNG"]
        },
            {
            "name": "Capuche Style", "price": "18.000 Ar", 
            "img": "/static/Capuche2.PNG", "likes": 45, "dislikes": 3, 
            "album": ["/static/Capuche2.PNG"]
        },
            {
            "name": "Capuche Style", "price": "18.000 Ar", 
            "img": "/static/Capuche3.PNG", "likes": 45, "dislikes": 3, 
            "album": ["/static/Capuche3.PNG"]
        }
    ],
    "Sport": [
        {
            "name": "Maillot Foot", "price": "12.000 Ar", 
            "img": "/static/maillot.PNG", "likes": 98, "dislikes": 4, 
            "album": ["/static/maillot.PNG"]
        }
    ]
}

# Statistiques de l'IA (Initialisées à 25% par défaut)
ia_stats = {"Homme": 25, "Femme": 25, "Jeune": 25, "Sport": 25}

@app.route('/')
def index():
    # Sélectionne le premier article de chaque catégorie pour l'affichage initial
    initial_items = {cat: items[0] for cat, items in CLOTHES_DATABASE.items()}
    return render_template('index.html', display=initial_items, full_catalog=CLOTHES_DATABASE, stats=ia_stats)

@app.route('/click_item', methods=['POST'])
def click_item():
    data = request.json
    category = data['category']
    reaction = data.get('reaction') # Récupère 'like', 'dislike' ou None
    
    if reaction == 'like':
        # Augmente l'intérêt de la catégorie de 5% lors d'un clic sur J'aime
        ia_stats[category] = min(100, ia_stats[category] + 5)
    elif reaction == 'dislike':
        # Diminue l'intérêt de 3%
        ia_stats[category] = max(0, ia_stats[category] - 3)
    else:
        # Calcul standard lors d'un simple clic sur le bouton "Voir plus"
        for cat in ia_stats:
            if cat == category:
                ia_stats[cat] = min(100, ia_stats[cat] + 10)
            else:
                ia_stats[cat] = max(0, ia_stats[cat] - 2)
            
    # Sélectionne un nouvel article aléatoire pour la catégorie
    new_item = random.choice(CLOTHES_DATABASE[category])
    return jsonify({'item': new_item, 'scores': ia_stats})

if __name__ == '__main__':
    # Lance le serveur Flask
    app.run(debug=True, port=5000)