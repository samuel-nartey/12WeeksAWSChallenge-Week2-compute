# 12WeeksAWSChallenge-Week2-compute
Week 2 of 12 Weeks of AWS Challenge: Deploying a scalable frontend-backend architecture using AWS Elastic Beanstalk with proper networking, private/public subnets, and multi-tier deployment."
Absolutely! Here's a **summarized and polished version** of your README with a **new title**, keeping the core concept intact but making it shorter, more digestible, and recruiter-friendly:

---

# Deploying a Scalable Frontend-Backend Architecture with AWS Elastic Beanstalk

## Overview

In this project, we explore **AWS Elastic Beanstalk (EB)** and how it simplifies deployment of web applications by automatically managing infrastructure. We'll build a **two-tier architecture**:

* **Backend:** Flask API in a **private subnet**
* **Frontend:** Flask web app in a **public subnet**, connected securely to the backend

By the end, you'll understand:

* EB's architecture and automated resource provisioning
* How to structure and deploy frontend and backend apps
* Networking best practices (public vs private subnets)
* Common troubleshooting steps

---

## Architecture

Elastic Beanstalk automates provisioning of:

* **EC2** for compute
* **Auto Scaling Groups** for high availability
* **Elastic Load Balancers** for traffic distribution
* **S3** for storing app versions
* **CloudWatch** for monitoring

### Custom Setup

* **Frontend:** Public subnet, internet-facing
* **Backend:** Private subnet, internal API
* **Security Groups:** Frontend allows public access, Backend allows access only from Frontend

> Diagram placeholder: *Frontend in public subnet, Backend in private subnet, connected via internal ALB.*

---

## Project Structure

```
12WEEKSAWSCHALLENGE-WK2/
│
├── backend/
│   ├── application.py
│   ├── requirements.txt
│   └── Procfile
│
└── frontend/
    ├── application.py
    ├── templates/index.html
    ├── requirements.txt
    └── Procfile
```

---

## Backend Setup (Private API)

**application.py**

```python
from flask import Flask, jsonify
application = Flask(__name__)

@application.route('/')
def home():
    return jsonify({"message": "Hello from Backend!"})

@application.route('/data')
def data():
    return jsonify({"users": ["IT_Sammy", "Samuel", "Paula"], "message": "Backend running smoothly"})
    
if __name__ == '__main__':
    application.run(host='0.0.0.0', port=8080)
```

**requirements.txt**

```
Flask==3.0.2
flask-cors==4.0.0
gunicorn==21.2.0
```

**Procfile**

```
web: gunicorn application:application
```

**Deploy:** Zip and upload to EB as **private/internal environment**

---

## Frontend Setup (Public Web App)

**application.py**

```python
from flask import Flask, render_template
import requests

application = Flask(__name__)
BACKEND_URL = "http://internal-backend-env.abcdefg.elb.amazonaws.com/data"

@application.route('/')
def home():
    try:
        data = requests.get(BACKEND_URL).json()
    except:
        data = {"error": "Backend unreachable"}
    return render_template('index.html', data=data)

if __name__ == '__main__':
    application.run(host='0.0.0.0', port=8080)
```

**index.html** – Simple frontend displaying backend data.

**requirements.txt**

```
Flask==3.0.2
gunicorn==21.2.0
requests==2.32.3
```

**Procfile**

```
web: gunicorn application:application
```

**Deploy:** Zip and upload to EB as **public environment**

---

## Networking

* **VPC** with public & private subnets
* **Internet Gateway** for public subnet
* **NAT Gateway** for private subnet internet access
* **Route Tables:** Public → IGW, Private → NAT
* **Security Groups:** Frontend allows public access; Backend only allows Frontend access

> For detailed VPC setup: [AWS VPC Guide](https://medium.com/@IT_Sammy/deploying-a-secure-web-app-on-aws-ec2-with-vpc-ssm-nat-12weekawshandsonchallenge-c65d560c84ec)

---

## Connecting Frontend and Backend

1. Copy backend internal ALB DNS
2. EB Console → Frontend → Configuration → Software → Environment Properties
3. Add: `BACKEND_URL=http://internal-backend-env.abcdefg.elb.amazonaws.com/data`
4. Apply changes & redeploy

---

## Troubleshooting

* **502 Bad Gateway:** Check Procfile, gunicorn in requirements.txt, ZIP structure
* **ModuleNotFoundError:** Ensure Procfile points to correct Flask instance
* **Frontend cannot reach Backend:** Confirm backend in private subnet, security groups allow access, and correct internal ALB URL used

---

## Conclusion

Elastic Beanstalk abstracts infrastructure management, allowing developers to focus on **application logic** while still deploying **scalable, secure, multi-tier architectures**. This project demonstrates real-world deployment of a frontend-backend web app using EB with proper networking and security.

---

If you want, I can also create a **super concise “one-page README with diagrams, commands, and screenshots”** that’s fully recruiter-ready and visually appealing. This would condense it even further while keeping all key information.


