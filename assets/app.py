from flask import Flask, request, render_template
from pymongo import MongoClient

app = Flask(__name__)

# Replace with your MongoDB connection string
client = MongoClient("mongodb+srv://sahiluk77:sahil4pf@cluster0.z0mgj3v.mongodb.net/")
db = client['portfolio']
collection = db['contacts']

@app.route('/')
def index():
    return render_template('port.html')  # your full portfolio page

@app.route('/submit', methods=['POST'])
def submit():
    data = {
        "name": request.form['Name'],
        "email": request.form['Email'],
        "mobile": request.form['Mobile'],
        "subject": request.form['Subject'],
        "message": request.form['Message']
    }
    collection.insert_one(data)
    return "Message sent to Sahil Ullah successfully!"

if __name__ == '__main__':
    app.run(debug=True)
