import requests
import sqlite3
from api_key.txt import spoonacular_api


limit = 25

def offset_recipes(): #pagination #avoid duplicates
    conn = sqlite3.connect("project.db")
    cur = conn.cursor()
    cur.execute("SELECT COUNT(*) FROM recipes")
    offset = cur.fetchone()[0]
    conn.close()
    return offset
    

def spoonacular_recipes(api_key, cuisine, num):
    base = 'https://api.spoonacular.com/recipes/complexSearch'
    params = {
        'apiKey': api_key, 
        'addRecipeInformation': True,
        'number': num
        }
    

    response = requests.get(base, params=params)
    info = response.json()


    results = info.get('results', [])

    for recipe in results:
        rec_id = recipe['id']


        title = recipe.get('title')
        cuisine = recipe.get('cuisine')
        ready_time = recipe.get('readyInMinutes')
        link = recipe.get('sourceURL')

        ingredients = recipe.get('extendedIngredients')
        








key = 'e844287625d74e3fb4c74a4b55d9e923'