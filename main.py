from flask import Flask, render_template, request, redirect, url_for
import pymongo

app = Flask(__name__)

mongo_uri = "mongodb+srv://gopung:t2hVVXV0LVJSi50q@gopung.7dxrsoj.mongodb.net/?retryWrites=true&w=majority"
client = pymongo.MongoClient(mongo_uri)
db = client["gopung"]
collection = db["guestbook"]

@app.route('/upload', methods=['POST'])
def upload_message():
    name = request.form['name']
    message = request.form['message']
    message_data = {"name": name, "message": message}
    collection.insert_one(message_data)
    return redirect(url_for('index'))

@app.route('/')
def index():
    messages = collection.find()
    return render_template('index.html', messages=messages)

if __name__ == "__main__":
    app.run(debug=True)
