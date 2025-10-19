from flask import Flask, jsonify, render_template


app = Flask(__name__)



@app.route("/")
def homepage():
    return render_template('home.html')



# route for destination pages
@app.route("/destinations")
def destinations():
    return render_template('destinations.html')

# route for blog post pages
@app.route("/blog-post")
def blog_post():
    return "<h1>Blog Post Page</h1><p>This is a sample blog post.</p>"

# route for home page
@app.route("/home")
def home():
    return render_template('home.html')

# route for experiences page
@app.route("/experiences")
def experiences():
    return "<h1>Experiences Page</h1><p>Discover unique experiences in Canada.</p>"

# route for support page
@app.route("/support")
def support():
    return "<h1>Support Page</h1><p>Get help and support for your travel plans.</p>"

# route for learn more page
@app.route("/learn-more")
def learn_more():
    return "<h1>Learn More</h1><p>More information about exploring Canada.</p>"

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)