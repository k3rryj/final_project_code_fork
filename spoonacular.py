import requests
import json



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