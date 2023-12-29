from flask import Flask, render_template, jsonify
import json

def load_ingredients():
    with open('data/ingredients.json') as file:
        data = json.load(file)
    return data

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def hello():
    ingredients = load_ingredients()
    return render_template('home.html', ingredients=ingredients)


@app.route('/get-sauces/<ingredient>')
def get_sauces(ingredient):
    with open('data/sauces.json') as file:
        sauces = json.load(file)
    matching_sauces = [sauce for sauce in sauces if ingredient in sauce["ingredients"]]
    return jsonify(matching_sauces)


if __name__ == '__main__':
    app.run(debug=True)