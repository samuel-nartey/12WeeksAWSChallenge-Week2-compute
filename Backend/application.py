from flask import Flask, jsonify
  # Enable CORS so frontend can access backend

application = Flask(__name__)
  # Allow requests from other origins (like frontend)

@application.route('/')
def home():
    return jsonify({"message": "Hello from the Backend API!"})

@application.route('/data')
def data():
    return jsonify({
        "users": ["IT_Sammy", "Samuel", "Paula Waka"],
        "message": "Backend is running smoothly 😎"
    })

if __name__ == '__main__':
    application.run(host='0.0.0.0', port=8080)  # IMPORTANT: EB listens on port 8080
