from flask import Flask, render_template, jsonify, request
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


@app.route('/get-sauces')
def get_sauces():
    ingredients = request.args.getlist('ingredients[]')
    with open('data/sauces.json') as file:
        sauces = json.load(file)
    matching_sauces = [sauce for sauce in sauces if any(ing in sauce["ingredients"] for ing in ingredients)]
    return jsonify(matching_sauces)


if __name__ == '__main__':
    app.run(debug=True)