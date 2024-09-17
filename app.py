import json
from flask import Flask, render_template
from assets_blueprint import assets_blueprint

args = dict()
try:
    with open("args.json") as f:
        args = json.load(f)
except FileNotFoundError:
    pass

app = Flask(__name__, **args)

# Provide Vite context processors and static assets directory.
app.register_blueprint(assets_blueprint)

@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def index(path):
    return render_template('index.html')

@app.route("/increment/<int:count>")
def increment(count):
    return f"{count + 1}"

if __name__ == '__main__':
    app.run(debug=True)

