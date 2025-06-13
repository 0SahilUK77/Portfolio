from flask import Flask, request, render_template
from pymongo import MongoClient
import os

app = Flask(__name__)

# Use environment variable for MongoDB URI
client = MongoClient(os.environ.get("MONGO_URI"))  # ✅ safer
db = client['portfolio']
collection = db['contacts']

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
@app.route('/submit', methods=['POST'])
def submit():
    try:
        data = {
            "name": request.form['Name'],
            "email": request.form['Email'],
            "mobile": request.form['Mobile'],
            "subject": request.form['Subject'],
            "message": request.form['Message']
        }
        result = collection.insert_one(data)
        print("✅ Inserted:", result.inserted_id)  # This will show in Render logs
        return "Message sent to Sahil Ullah successfully!"
    except Exception as e:
        print("❌ MongoDB insert error:", str(e))
        return f"❌ Error submitting: {str(e)}"
@app.route('/check-db')
def check_db():
    try:
        client.server_info()  # will throw if not connected
        return "✅ MongoDB connected"
    except Exception as e:
        return f"❌ MongoDB connection error: {str(e)}"

