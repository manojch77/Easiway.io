from flask import Flask, request
import firebase_admin
from firebase_admin import credentials, db

app = Flask(__name__)

# Initialize Firebase only once
cred = credentials.Certificate("serviceAccountKey.json")   
if not firebase_admin._apps:
    firebase_admin.initialize_app(cred, {
        'databaseURL': 'https://easy-22b8-default-rtdb.firebaseio.com/'
    })

@app.route('/', methods=['GET'])
def index():
    return "✅ Flask server is running and ready to receive GPS POST data.", 200

@app.route('/', methods=['POST'])
def receive_data():
    device_id = request.form.get('id')
    lat = request.form.get('lat')
    lon = request.form.get('lon')

    print(f"Received data: ID={device_id}, lat={lat}, lon={lon}")

    if device_id and lat and lon:
        try:
            ref = db.reference(f'buses/{device_id}')
            ref.set({'lat': float(lat), 'lng': float(lon)})
            print(f"✅ Successfully wrote to Firebase: buses/{device_id}")
            return "Location updated", 200
        except Exception as e:
            print(f"❌ Firebase error: {e}")
            return "Firebase error", 500

    return "Missing data", 400

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5500, debug=True)
