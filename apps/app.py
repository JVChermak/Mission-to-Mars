# Import dependencies
from flask import Flask, render_template
from flask_pymongo import PyMongo
import scraping

# Set up Flask
app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)

# Define the route for the HTML page
@app.route("/")
def index():
    mars = mongo.db.mars.find_one()
    return render_template("index.html", mars=mars)

# Add next route for scraping
@app.route("/scrape")
def scrape():
    mars = mongo.db.mars
    mars_data = scraping.scrape_all()
    mars.update({}, mars_data, upsert=True)
    return render_template("scrape.html")

# Add routes for hemisphere images
@app.route("/img1")
def img1():
    mars = mongo.db.mars.find_one()
    return render_template("img1.html", mars=mars)

@app.route("/img2")
def img2():
    mars = mongo.db.mars.find_one()
    return render_template("img2.html", mars=mars)

@app.route("/img3")
def img3():
    mars = mongo.db.mars.find_one()
    return render_template("img3.html", mars=mars)

@app.route("/img4")
def img4():
    mars = mongo.db.mars.find_one()
    return render_template("img4.html", mars=mars)

if __name__ == "__main__":
    app.run(debug=True)