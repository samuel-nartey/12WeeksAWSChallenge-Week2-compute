from flask import Flask, render_template
import requests

application = Flask(__name__)

# Backend API URL (your Beanstalk backend)
BACKEND_URL = "http://newone.eu-north-1.elasticbeanstalk.com/data"

@application.route('/')
def home():
    try:
        response = requests.get(BACKEND_URL)
        data = response.json()
    except Exception as e:
        data = {"error": str(e), "message": "Failed to fetch backend data"}
    
    return render_template('index.html', data=data)

if __name__ == '__main__':
    application.run(host='0.0.0.0', port=8080)
