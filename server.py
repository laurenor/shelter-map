from flask import Flask, render_template, redirect, json, request, session, jsonify

app = Flask(__name__)

@app.route('/')
def render_home():
    return render_template('index.html')

if __name__ == "__main__":
    # app.debug = True
    # connect_to_db(app)
    app.run()