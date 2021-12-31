from app import app
from app import custom_filters
from flask import render_template
from datetime import datetime


@app.route("/")
def index():
    return render_template("public/index.html")

@app.route("/jinja")
def jinja():

    my_name = "Lloyd Turk"
    age = 31
    langs = ["Python", "HTML", "CSS", "Bash", "C"]
    friends = {
        "Tom": 30,
        "Steve": 60,
        "Mike": 56,
        "Rebecca": 23
    }
    colours = ("Red", "Green")

    cool = True

    class GitRemote:
        def __init__(self, name, description, url):
            self.name = name
            self.description = description
            self.url = url

        def pull(self):
            return f"Pullin repo {self.name}"
            
        def clone(self):
            return f"Cloning into {self.url}"
    
    my_remote = GitRemote(
        name="Flask Jinja", 
        description="Template design tutorial", 
        url="https://github.com/julian-nash/jinja.git"
        )
        
    def repeat(x, qty):
        return x * qty

    date = datetime.utcnow()

    my_html = "<h1>THIS IS SOME HTML</h1>"

    suspicious = "<script>alert('YOU GOT HACKED')</script>"

    return render_template(
        "public/jinja.html", my_name=my_name, age=age,
        langs=langs, friends=friends, colours=colours,
        cool=cool, GitRemote=GitRemote, repeat=repeat,
        my_remote=my_remote, date=date, my_html=my_html,
        suspicious=suspicious
        )

@app.route("/about")
def about():
    return render_template("public/about.html")