# save this as app.py
from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def hello():
    return "<p>Hello, World</p> "

@app.route("/hello")
def hello2():
    return "Hello, World Its a ME R.G. !"

@app.route("/contact")
def contact():
    return "Stranka kontaktu "

@app.route("/user/<username>")
def show_user_profile(username):
    return f'Profil pouzivatela {username}'

@app.route("/post/<int:post_id>")
def show_post_id(post_id):
    return f'Id postu:  {post_id}'

# @app.route("/poloha-objednavky/<int:id_objednavky>")
# def show_user_profile(id_objednavky):
#     return f'Id objednavky {id_objednavky}'

@app.route("/poloha-objednavky/<int:id_objednavky>/<string:hash>")
def show(id_objednavky,hash):
    return f'Id objednavky {id_objednavky} a hash {hash}'

@app.route("/search")   # http://localhost:5000/search?query=pes
def search():
    query = request.args.get('query')
    id = request.args.get('id')
    return f"Searching for: {query} and id : {id}"

@app.route("/submit", methods=['POST'])
def submit():
    username = request.form['username']
    password = request.form['password']
    return f'Username: {username}, Password: {password}'

@app.route("/submit-json", methods=['POST'])
def submit_json():
    json = request.get_json()
    username=json['username']
    return f"Json : {username}"

@app.route('/upload', methods=["POST"])
def upload_file():
    file = request.files['file']
    # file.save(f"/path/to/save/{file.filename}")
    return "File uploaded sucessfully!"

if __name__ == "__main__":
    app.run()
#flask run
# * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)