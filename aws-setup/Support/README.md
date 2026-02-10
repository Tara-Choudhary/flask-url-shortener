# 🛠️ What We Have Done (Application Support Work)

This section documents the practical steps performed to run, manage, and support
The Flask URL Shortener application in a production-like environment.

---

## 1️⃣ Environment Setup (AWS EC2)

- Created a **dedicated IAM user** for this project to follow least-privilege access
- Launched an **AWS EC2 instance** using:
  - Amazon Linux 2023
  - t2.micro / t3.micro (Free Tier eligible)
- Configured Security Group:
  - SSH (22) → restricted to personal IP
  - Application Port (5000) → open for testing

## 2️⃣ Secure Server Access

- Connected to EC2 using SSH and `.pem` key
- Verified server identity and health using:
  - `whoami`
  - `hostname`
  - `uptime`
  - `uname -a`
  - `df -h`
  - `free -m`

This confirms:
- Correct user access
- OS and kernel version
- CPU, memory, and disk health

## 3️⃣ Application Deployment

- Cloned the Flask URL Shortener project on EC2
- Installed Python dependencies using `pip`
- Ran the Flask application and verified:
  - App starts successfully
  - Port 5000 is listening
  - Application responds locally using `curl`

## 4️⃣ Production-Style Process Management

- Converted the Flask application into a **systemd-managed service**
- Created a systemd service file:
  - `flask-url-shortener.service`
- Configured the service to:
  - Run under `ec2-user`
  - Restart automatically on failure
  - Start automatically on system reboot

This removes manual app startup and simulates real production behavior.



## 5️⃣ Service Validation

- Verified service status using:
  ```bash
  sudo systemctl status flask-url-shortener
  ```
- Confirmed application process is running and bound to port 5000
- Validated service persistence after restarts

## 6️⃣ Log Monitoring & Troubleshooting

- Used journalctl to inspect application logs:
```bash
sudo journalctl -u flask-url-shortener
```
- Verified:
   - Application startup logs
   - HTTP request logs
   - Error-free operation
- This simulates real incident investigation and log-based debugging.

## 7️⃣ Network & Access Validation

- Verified application access via:
   - Local server (127.0.0.1:5000)
   - Public EC2 IP (<EC2_PUBLIC_IP>:5000)
- Confirmed Security Group and network path are working correctly

## 8️⃣ Evidence Collection
- Captured screenshots showing:
   - EC2 instance running
   - Application accessible in a browser
   - systemd service status
   - Application logs
   - Port listening status
- All screenshots are stored in:
```bash
support/screenshots/
```

## 9️⃣ Support Role Skills Demonstrated

### Through this work, the following real-world skills were practiced:
- Linux system administration
- Application lifecycle management
- Service monitoring and restart handling
- Log analysis and troubleshooting
- AWS EC2 operations
- Production support mindset

## ✅ Current Status
- Application is running successfully
- Managed via systemd
- Accessible via public IP
- Logs monitored and verified
- Ready for support and troubleshooting scenarios  
