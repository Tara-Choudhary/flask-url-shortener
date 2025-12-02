# 🚀 Flask URL Shortener (Deployed on AWS EC2)

A simple and clean **URL Shortener Web Application** built with **Python Flask** and deployed manually on **AWS EC2** using the Free Tier.  

This project demonstrates:
- Python backend development  
- Flask web framework  
- AWS EC2 deployment  
- Linux server setup  
- Git & GitHub workflow  

All steps and screenshots are included for learning and portfolio purposes.


## 📸 Live Deployment Screenshots

All AWS screenshots are stored inside the **`/aws-setup`** folder:

- EC2 Instance (Running)
- Instance Details + Public IP
- Security Group Inbound Rules
- SSH terminal logs
- Flask installation
- Web app running on browser
- Short URL generation output (success)

These screenshots serve as proof of actual AWS deployment.

## 📝 Features

- 🔗 Shorten any long URL
- 🔁 Redirect using short unique code
- 🗑️ Delete shortened URLs
- 🧠 JSON file used as a storage DB (no external DB needed)
- 🌐 Deployed on AWS EC2 instance
- 🖥️ Clean UI with HTML + CSS (Jinja2 templating)

## 🏗️ Project Structure
```
flask-url-shortener/
│
├── app.py
├── urls.json
├── requirements.txt
│
├── templates/
│ └── index.html
│
├── static/
│ └── style.css
│
└── aws-setup/
└── (AWS screenshots)
```

## 🏛️ Architecture Diagram
```
    ┌───────────────────────────────────────┐
    │             User Browser               │
    │    http://<EC2 Public IP>:5000         │
    └───────────────────────────────────────┘
                    │
                    ▼
    ┌───────────────────────────────────────┐
    │             AWS EC2 Instance           │
    │   Amazon Linux 2023 (t2.micro/t3.micro)│
    │                                        │
    │   ┌─────────────────────────────────┐  │
    │   │        Flask Application        │  │
    │   │  - app.py                       │  │
    │   │  - urls.json (data storage)     │  │
    │   │  - HTML + CSS templates         │  │
    │   └─────────────────────────────────┘  │
    │                                        │
    │  Security Group:                       │
    │  - Port 22 (SSH)                       │
    │  - Port 5000 (Flask App)               │
    └───────────────────────────────────────┘

```

## 🖥️ Run Locally (Development Setup)

### 1 Clone the repository
```
git clone https://github.com/Tara-Choudhary/flask-url-shortener.git
cd flask-url-shortener
```

### 2 Create virtual environment
```
python3 -m venv venv
source venv/bin/activate
```

### 3 Install dependencies
```
pip install -r requirements.txt
```

### 4 Run Flask app
```
python3 app.py
```
```
Visit the app locally at:
👉 http://127.0.0.1:5000
```

## ☁️ Deploy to AWS EC2

### Step 1: Launch EC2 Instance

- Amazon Linux 2023

- Instance type: t2.micro / t3.micro (Free Tier)

- Key pair: **.pem** file

- Configure Security Group:

   - SSH → **Port 22**
   - Custom TCP → **Port 5000**


### Step 2: SSH into instance

```
chmod 400 flask-key.pem
ssh -i flask-key.pem ec2-user@<YOUR_PUBLIC_IP>
```


### Step 3: Install Python, pip, Git 

```
sudo yum update -y
sudo yum install python3 python3-pip git -y
```

### Step 4: Clone repository

```
git clone https://github.com/Tara-Choudhary/flask-url-shortener.git
cd flask-url-shortener
```

### Step 5: Install Flask dependencies

```
pip3 install -r requirements.txt
```

### Step 6: Run the Flask app

```
python3 app.py
```
#### You'll see: 

```
Running on http://0.0.0.0:5000
```

### Step 7: Open app in browser

```
http://<EC@-PUBLIC-IP>:5000
```

<!-- ## Tech Stack

- Python 3
- Flask 3
- HTML, CSS, Jinja2
- AWS EC2
- Amazon Linux
- Git & GitHub -->
## 🛠️ Tech Stack

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-3.x-black?logo=flask&logoColor=white)
![HTML](https://img.shields.io/badge/HTML-5-orange?logo=html5&logoColor=white)
![CSS](https://img.shields.io/badge/CSS-3-264de4?logo=css3&logoColor=white)
![Jinja2](https://img.shields.io/badge/Jinja2-Template_Engine-red?logo=jinja&logoColor=white)

![AWS EC2](https://img.shields.io/badge/AWS-EC2-F8981D?logo=amazon-aws&logoColor=white)
![Amazon Linux](https://img.shields.io/badge/Amazon%20Linux-2023-232F3E?logo=linux&logoColor=white)

![Git](https://img.shields.io/badge/Git-Tool-F05033?logo=git&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-Repository-181717?logo=github&logoColor=white)


## 📬 Contact

**Author:** Tara Choudhary  

**GitHub:** [Tara-Choudhary](https://github.com/Tara-Choudhary)  

**LinkedIn:** [Tara Choudhary](https://www.linkedin.com/in/tara-choudhary00/)  

**Email:** developer.tarachoudhary@gmail.com

## License
This project is licensed under the MIT License.
