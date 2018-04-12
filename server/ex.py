# Simple example
#
# This example (simple.py) shows the basic structure of a Flask program.
#
# To run this app do:
#
#    1. Start your app from the command line:
#
#       terminal> python simple.py
#
#    2. Invoke it on your web browser by:
#       http://127.0.0.1:5000
#       or
#       http://localhost:5000
#
#    3. ctl-C on terminal to kill the server program when you are done.


# Import Flask so that we can create an app instance
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

# All Flask app must create an app instance like this:
app = Flask(__name__)


file_path = os.path.abspath(os.getcwd())+"\meal.db"

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+file_path
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
ma = Marshmallow(app)

class Meals(db.Model):
    idMeal = db.Column(db.String(120), primary_key=True)
    strMeal = db.Column(db.String(120), unique=True)
    strCategory = db.Column(db.String(120), unique=False)
    strArea = db.Column(db.String(120), unique=False)
    strInstructions = db.Column(db.String(3000), unique=False)
    strMealThumb = db.Column(db.String(320), unique=False)
    strTags = db.Column(db.String(320), unique=False)
    strYoutube = db.Column(db.String(320), unique=False)
    strIngredient1 = db.Column(db.String(120), unique=False)
    strIngredient2 = db.Column(db.String(120), unique=False)
    strIngredient3 = db.Column(db.String(120), unique=False)
    strIngredient4 = db.Column(db.String(120), unique=False)
    strIngredient5 = db.Column(db.String(120), unique=False)
    strIngredient6 = db.Column(db.String(120), unique=False)
    strIngredient7 = db.Column(db.String(120), unique=False)
    strIngredient8 = db.Column(db.String(120), unique=False)
    strIngredient9 = db.Column(db.String(120), unique=False)
    strIngredient10 = db.Column(db.String(120), unique=False)
    strIngredient11 = db.Column(db.String(120), unique=False)
    strIngredient12 = db.Column(db.String(120), unique=False)
    strIngredient13 = db.Column(db.String(120), unique=False)
    strIngredient14 = db.Column(db.String(120), unique=False)
    strIngredient15 = db.Column(db.String(120), unique=False)
    strIngredient16 = db.Column(db.String(120), unique=False)
    strIngredient17 = db.Column(db.String(120), unique=False)
    strIngredient18 = db.Column(db.String(120), unique=False)
    strIngredient19 = db.Column(db.String(120), unique=False)
    strIngredient20 = db.Column(db.String(120), unique=False)
    strMeasure1 = db.Column(db.String(120), unique=False)
    strMeasure2 = db.Column(db.String(120), unique=False)
    strMeasure3 = db.Column(db.String(120), unique=False)
    strMeasure4 = db.Column(db.String(120), unique=False)
    strMeasure5 = db.Column(db.String(120), unique=False)
    strMeasure6 = db.Column(db.String(120), unique=False)
    strMeasure7 = db.Column(db.String(120), unique=False)
    strMeasure8 = db.Column(db.String(120), unique=False)
    strMeasure9 = db.Column(db.String(120), unique=False)
    strMeasure10 = db.Column(db.String(120), unique=False)
    strMeasure11 = db.Column(db.String(120), unique=False)
    strMeasure12 = db.Column(db.String(120), unique=False)
    strMeasure13 = db.Column(db.String(120), unique=False)
    strMeasure14 = db.Column(db.String(120), unique=False)
    strMeasure15 = db.Column(db.String(120), unique=False)
    strMeasure16 = db.Column(db.String(120), unique=False)
    strMeasure17 = db.Column(db.String(120), unique=False)
    strMeasure18 = db.Column(db.String(120), unique=False)
    strMeasure19 = db.Column(db.String(120), unique=False)
    strMeasure20 = db.Column(db.String(120), unique=False)
    strSource= db.Column(db.String(320), unique=False)
    dateModified = db.Column(db.String(120), unique=False)

    def __init__(self, idMeal, strMeal, strCategory, strArea, strInstructions, strMealThumb, strTags, strYoutube, strIngredient1, strIngredient2, strIngredient3, strIngredient4, strIngredient5, strIngredient6, strIngredient7, strIngredient8, strIngredient9, strIngredient10, strIngredient11, strIngredient12, strIngredient13, strIngredient14, strIngredient15, strIngredient16, strIngredient17, strIngredient18, strIngredient19, strIngredient20, strMeasure1, strMeasure2, strMeasure3, strMeasure4, strMeasure5, strMeasure6, strMeasure7, strMeasure8, strMeasure9, strMeasure10, strMeasure11, strMeasure12, strMeasure13, strMeasure14, strMeasure15, strMeasure16, strMeasure17, strMeasure18, strMeasure19, strMeasure20, strSource, dateModified):
        self.idMeal = idMeal
        self.strMeal = strMeal
        self.strCategory = strCategory
        self.strArea = strArea
        self.strInstructions = strInstructions
        self.strMealThumb = strMealThumb
        self.strTags = strTags
        self.strYoutube = strYoutube
        self.strIngredient1 = strIngredient1
        self.strIngredient2 = strIngredient2
        self.strIngredient3 = strIngredient3
        self.strIngredient4 = strIngredient4
        self.strIngredient5 = strIngredient5
        self.strIngredient6 = strIngredient6
        self.strIngredient7 = strIngredient7
        self.strIngredient8 = strIngredient8
        self.strIngredient9 = strIngredient9
        self.strIngredient10 = strIngredient10
        self.strIngredient11 = strIngredient11
        self.strIngredient12 = strIngredient12
        self.strIngredient13 = strIngredient13
        self.strIngredient14 = strIngredient14
        self.strIngredient15 = strIngredient15
        self.strIngredient16 = strIngredient16
        self.strIngredient17 = strIngredient17
        self.strIngredient18 = strIngredient18
        self.strIngredient19 = strIngredient19
        self.strIngredient20 = strIngredient20
        self.strMeasure1 = strMeasure1
        self.strMeasure2 = strMeasure2
        self.strMeasure3 = strMeasure3
        self.strMeasure4 = strMeasure4
        self.strMeasure5 = strMeasure5
        self.strMeasure6 = strMeasure6
        self.strMeasure7 = strMeasure7
        self.strMeasure8 = strMeasure8
        self.strMeasure9 = strMeasure9
        self.strMeasure10 = strMeasure10
        self.strMeasure11 = strMeasure11
        self.strMeasure12 = strMeasure12
        self.strMeasure13 = strMeasure13
        self.strMeasure14 = strMeasure14
        self.strMeasure15 = strMeasure15
        self.strMeasure16 = strMeasure16
        self.strMeasure17 = strMeasure17
        self.strMeasure18 = strMeasure18
        self.strMeasure19 = strMeasure19
        self.strMeasure20 = strMeasure20
        self.strSource = strSource
        self.dateModified = dateModified
        
#This part defined structure of response of our endpoint.
#We want that all of our endpoint will have JSON response.
#Here we define that our JSON response will have two keys(username, and email).
class MealSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('idMeal', 'strMeal', 'strCategory', 'strArea', 'strInstructions', 'strMealThumb', 'strTags', 'strYoutube', 'strIngredient1', 'strIngredient2', 'strIngredient3', 'strIngredient4', 'strIngredient5', 'strIngredient6', 'strIngredient7', 'strIngredient8', 'strIngredient9', 'strIngredient10', 'strIngredient11', 'strIngredient12', 'strIngredient13', 'strIngredient14', 'strIngredient15', 'strIngredient16', 'strIngredient17', 'strIngredient18', 'strIngredient19', 'strIngredient20', 'strMeasure1', 'strMeasure2', 'strMeasure3', 'strMeasure4', 'strMeasure5', 'strMeasure6', 'strMeasure7', 'strMeasure8', 'strMeasure9', 'strMeasure10', 'strMeasure11', 'strMeasure12', 'strMeasure13', 'strMeasure14', 'strMeasure15', 'strMeasure16', 'strMeasure17', 'strMeasure18', 'strMeasure19', 'strMeasure20', 'strSource', 'dateModified')

meal_schema = MealSchema()
meals_schema = MealSchema(many=True)

# endpoint to show all ingredients
@app.route("/meals", methods=["GET"])
def get_meals():
    app.logger.info("sunt in toti meals in server")
    all_meals = Meals.query.all()
    result = meals_schema.dump(all_meals)
    return jsonify(result.data)

# endpoint to create new ingredient
@app.route("/meal", methods=["POST"])
def add_meal():
    app.logger.info('sunt in add_ingr in server')
    app.logger.info("print request.json")
    app.logger.info(request.json)
    
    idMeal = request.json['idMeal']
    strMeal = request.json['strMeal']
    strCategory = request.json['strCategory']
    strArea = request.json['strArea']
    strInstructions = request.json['strInstructions']
    strMealThumb = request.json['strMealThumb']
    strTags = request.json['strTags']
    strYoutube = request.json['strYoutube']
    strIngredient1 = request.json['strIngredient1']
    strIngredient2 = request.json['strIngredient2']
    strIngredient3 = request.json['strIngredient3']
    strIngredient4 = request.json['strIngredient4']
    strIngredient5 = request.json['strIngredient5']
    strIngredient6 = request.json['strIngredient6']
    strIngredient7 = request.json['strIngredient7']
    strIngredient8 = request.json['strIngredient8']
    strIngredient9 = request.json['strIngredient9']
    strIngredient10 = request.json['strIngredient10']
    strIngredient11 = request.json['strIngredient11']
    strIngredient12 = request.json['strIngredient12']
    strIngredient13 = request.json['strIngredient13']
    strIngredient14 = request.json['strIngredient14']
    strIngredient15 = request.json['strIngredient15']
    strIngredient16 = request.json['strIngredient16']
    strIngredient17 = request.json['strIngredient17']
    strIngredient18 = request.json['strIngredient18']
    strIngredient19 = request.json['strIngredient19']
    strIngredient20 = request.json['strIngredient20']
    strMeasure1 = request.json['strMeasure1']
    strMeasure2 = request.json['strMeasure2']
    strMeasure3 = request.json['strMeasure3']
    strMeasure4 = request.json['strMeasure4']
    strMeasure5 = request.json['strMeasure5']
    strMeasure6 = request.json['strMeasure6']
    strMeasure7 = request.json['strMeasure7']
    strMeasure8 = request.json['strMeasure8']
    strMeasure9 = request.json['strMeasure9']
    strMeasure10 = request.json['strMeasure10']
    strMeasure11 = request.json['strMeasure11']
    strMeasure12 = request.json['strMeasure12']
    strMeasure13 = request.json['strMeasure13']
    strMeasure14 = request.json['strMeasure14']
    strMeasure15 = request.json['strMeasure15']
    strMeasure16 = request.json['strMeasure16']
    strMeasure17 = request.json['strMeasure17']
    strMeasure18 = request.json['strMeasure18']
    strMeasure19 = request.json['strMeasure19']
    strMeasure20 = request.json['strMeasure20']
    strSource = request.json['strSource']
    dateModified = request.json['dateModified']

    new_meal = Meals(idMeal, strMeal, strCategory, strArea, strInstructions, strMealThumb, strTags, strYoutube, strIngredient1, strIngredient2, strIngredient3, strIngredient4, strIngredient5, strIngredient6, strIngredient7, strIngredient8, strIngredient9, strIngredient10, strIngredient11, strIngredient12, strIngredient13, strIngredient14, strIngredient15, strIngredient16, strIngredient17, strIngredient18, strIngredient19, strIngredient20, strMeasure1, strMeasure2, strMeasure3, strMeasure4, strMeasure5, strMeasure6, strMeasure7, strMeasure8, strMeasure9, strMeasure10, strMeasure11, strMeasure12, strMeasure13, strMeasure14, strMeasure15, strMeasure16, strMeasure17, strMeasure18, strMeasure19, strMeasure20, strSource, dateModified)

    db.session.add(new_meal)
    db.session.commit()
# show new user in JSON form as response.
    return meal_schema.jsonify(new_meal)


#MEALS

class Ingredients(db.Model):
    idIngredient = db.Column(db.Integer, primary_key=True)
    strIngredient = db.Column(db.String(120), unique=True)
    strDescription = db.Column(db.String(120), unique=False)
    strType = db.Column(db.String(120), unique=False)

    def __init__(self, id, name, description, type):
        self.idIngredient = id
        self.strIngredient = name
        self.strDescription = description
        self.strType = type
        
#This part defined structure of response of our endpoint.
#We want that all of our endpoint will have JSON response.
#Here we define that our JSON response will have two keys(username, and email).
class IgredientSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('idIngredient', 'strIngredient', 'strDescription', 'strType')

ingredient_schema = IgredientSchema()
ingredients_schema = IgredientSchema(many=True)

# endpoint to show all ingredients
@app.route("/ingredients", methods=["GET"])
def get_ingredient():
    app.logger.info("sunt in toti user in server")
    all_ingredients = Ingredients.query.all()
    result = ingredients_schema.dump(all_ingredients)
    return jsonify(result.data)

# endpoint to create new ingredient
@app.route("/ingredient", methods=["POST"])
def add_ingredient():
    app.logger.info('sunt in add_ingr in server')
    app.logger.info("print request.json")
    app.logger.info(request.json)
    idIngredient = request.json['idIngredient']
    strIngredient = request.json['strIngredient']
    strDescription = request.json['strDescription']
    strType = request.json['strType']

    new_user = Ingredients(idIngredient, strIngredient, strDescription, strType)

    db.session.add(new_user)
    db.session.commit()
# show new user in JSON form as response.
    return ingredient_schema.jsonify(new_user)




# Invoke this one with http://127.0.0.1:5000
#@app.route('/')
#def index():
 #  return 'Index Page'

## Invoke this one with http://127.0.0.1:5000/hello
#@app.route('/hello')
#def hello():
 #   return '<h1>Hello World</h1>'


# Now, run the app as a server in debug mode
if __name__ == '__main__':
	#app.secret_key = os.urandom(12)
    app.run(host = '192.168.0.101', port = 4000)#