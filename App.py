from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

# Angon-drakitra miaraka amin'ny sary local sy ny reaction
CLOTHES_DATABASE = {
    "Homme": [
        {
            "id": 1, "name": "T-shirt Cotton Premium", "price": "15.000 Ar", 
            "img": "/static/T-shirt.PNG", "likes": 124, "dislikes": 5,
            "album": ["/static/T-shirt.PNG"]
        },
        {
            "id": 2, "name": "Pantalon", "price": "45.000 Ar", 
            "img": "/static/Jeans.PNG", "likes": 86, "dislikes": 2,
            "album": ["/static/Jeans.PNG"]
        },
        {
            "id":3 , "name": "Pantalon", "price": "15.000 Ar", 
            "img": "/static/Jeans homme.PNG", "likes": 124, "dislikes": 5,
            "album": ["/static/Jeans homme.PNG"]
        },
    ],
    "Femme": [
        {
            "id": 4, "name": "Robe long", "price": "45.000 Ar", 
            "img": "/static/Robe femme.PNG", "likes": 210, "dislikes": 8,
            "album": ["/static/Robe femme.PNG"]
        },
           {
            "id": 5, "name": "Robe long", "price": "45.000 Ar", 
            "img": "/static/Robe femme1.PNG", "likes": 210, "dislikes": 8,
            "album": ["/static/Robe femme1.PNG"]
        },
           {
            "id": 6, "name": "Robe long", "price": "45.000 Ar", 
            "img": "/static/Robe femme2.PNG", "likes": 210, "dislikes": 8,
            "album": ["/static/Robe femme2.PNG"]
        },
           {
            "id": 7, "name": "Robe long", "price": "45.000 Ar", 
            "img": "/static/Robe femme3.PNG", "likes": 210, "dislikes": 8,
            "album": ["/static/Robe femme3.PNG"]
        }
    ],
    "Jeune": [
        {
            "id": 8, "name": "Capuche", "price": "18.000 Ar", 
            "img": "/static/Capuche.PNG", "likes": 45, "dislikes": 3,
            "album": ["/static/Capuche.PNG"]
        },
          {
            "id": 9, "name": "Capuche", "price": "18.000 Ar", 
            "img": "/static/Capuche1.PNG", "likes": 45, "dislikes": 3,
            "album": ["/static/Capuche1.PNG"]
        },
          {
            "id": 10, "name": "Capuche", "price": "18.000 Ar", 
            "img": "/static/Capuche2.PNG", "likes": 45, "dislikes": 3,
            "album": ["/static/Capuche2.PNG"]
        },
          {
            "id": 11, "name": "Capuche", "price": "18.000 Ar", 
            "img": "/static/Capuche3.PNG", "likes": 45, "dislikes": 3,
            "album": ["/static/Capuche3.PNG"]
        }
    ],
    "Sport": [
        {
            "id": 12, "name": "Maillot Foot", "price": "12.000 Ar", 
            "img": "/static/maillot.PNG", "likes": 98, "dislikes": 4,
            "album": ["/static/maillot.PNG"]
        }
    ]
}

# IA Stats (Sokajy tiana indrindra)
ia_stats = {"Lehilahy": 25, "Vehivavy": 25, "Jeune": 25, "Sport": 25}

@app.route('/')
def index():
    # Mampiseho ny akanjo voalohany isaky ny sokajy eo ambony
    display_items = {cat: items[0] for cat, items in CLOTHES_DATABASE.items()}
    return render_template('index.html', display=display_items, full_catalog=CLOTHES_DATABASE, stats=ia_stats)

@app.route('/react', methods=['POST'])
def react():
    data = request.json
    category = data['category']
    reaction_type = data['type']
    
    # Manavao ny IA stats arakaraka ny reaction
    if reaction_type == 'like':
        ia_stats[category] = min(100, ia_stats[category] + 5)
    else:
        ia_stats[category] = max(0, ia_stats[category] - 3)
        
    return jsonify({'scores': ia_stats})

if __name__ == '__main__':
    app.run(debug=True, port=5000)