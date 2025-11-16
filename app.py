from flask import Flask, render_template

import random



app = Flask(__name__)



quotes = [

    "Dream big, start small, act now.",

    "The only limit to our realization of tomorrow is our doubts today.",

    "Don't watch the clock; do what it does. Keep going.",

    "Success is not final; failure is not fatal.",

    "Everything you can imagine is real."

]



affirmations = [

    "I am capable.",

    "I attract positivity.",

    "I am becoming the best version of myself.",

    "I choose peace.",

    "I am improving every day."

]



colors = ["#FF6F61", "#6B5B95", "#88B04B", "#F7CAC9", "#92A8D1", "#955251", "#B565A7"]



@app.route("/")

def index():

    quote = random.choice(quotes)

    affirmation = random.choice(affirmations)

    color = random.choice(colors)

    return render_template("index.html", quote=quote, affirmation=affirmation, color=color)



if __name__ == "__main__":

    app.run(host="0.0.0.0", port=5000)
