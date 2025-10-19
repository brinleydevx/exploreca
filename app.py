from flask import Flask, jsonify, render_template


app = Flask(__name__)


# route for homepage         --- done ---
@app.route("/")
def homepage():
    return render_template('home.html')



# route for destination pages       --- done ---
@app.route("/destinations")
def destinations():
    return render_template('destinations.html')

# route for blog post pages
@app.route("/blog-post")
def blog_post():
    return render_template('blog_post.html')

# route for home page      --- done ---
@app.route("/home")
def home():
    return render_template('home.html')

# route for experiences page  --- done ---
@app.route("/experiences")
def experiences():
    return render_template('experience.html')

@app.route("/discover")
def discover():
    return render_template('discover.html')

# route for support page
@app.route("/support")
def support():
    return render_template('contact.html')

# route for learn more page --- done ---
@app.route("/learn-more")
def learn_more():
    return "<h1>Learn More</h1><p>More information about exploring Canada.</p>"

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)