# 🛡️ Simple SSH Honeypot Simulator

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Experimental-orange)

A lightweight **Python honeypot** that simulates a fake SSH service on port `2222`.  
It captures attacker inputs (like usernames and passwords) and logs all activity for analysis.  

> **Disclaimer:** For educational and research purposes only. Do **not** deploy in production or expose to the internet without proper isolation.

---

## 🚀 Features
- Listens on TCP port **2222** and pretends to be an SSH server.  
- Sends a **fake SSH banner** (`SSH-2.0-OpenSSH_8.2`) to trick attackers.  
- Captures and logs all attacker inputs.  
- Logs are timestamped and stored in `honeypot_log.txt`.  
- Graceful shutdown via **Ctrl+C**.  

---

## 🛠️ Technologies Used
- **Python 3.x**  
- **socket** → for creating the network service  
- **datetime** → for timestamps  
- **File Logging** → stores captured input  

---

## 📂 File Structure
honeypot/
│
├── honeypot.py # main honeypot script
├── honeypot_log.txt # log file generated at runtime
└── README.md # project documentation


---

## ⚡ Usage

### 1. Run the honeypot
```bash
python honeypot.py


Output example:

[2025-09-14 00:41:41] [STARTED] Honeypot running on port 2222...

2. Simulate an attack (local test)

Open another terminal:

telnet 127.0.0.1 2222


You should see:

SSH-2.0-OpenSSH_8.2


Type credentials (e.g., root or password123) and press Enter.

3. Check the logs

Open honeypot_log.txt:

[2025-09-14 00:41:41] Connection from 127.0.0.1:49336
[2025-09-14 00:41:41] Input from 127.0.0.1: root
[2025-09-14 00:41:42] Input from 127.0.0.1: password123
[2025-09-14 00:41:42] Closed connection 127.0.0.1:49336

🧪 Example Use Cases

Cybersecurity training – observe how attackers interact with fake services.

Research – collect brute-force attempts and common credentials.

Detection – identify unauthorized access attempts.

📊 Architecture / Flow Diagram
          ┌───────────────┐
          │   Attacker    │
          └───────┬───────┘
                  │ Connects
                  ▼
          ┌───────────────┐
          │   Honeypot    │
          │  (Fake SSH)   │
          └───────┬───────┘
                  │ Logs
                  ▼
          ┌───────────────┐
          │ honeypot_log  │
          │  (Text File)  │
          └───────────────┘

⚠️ Disclaimer

This honeypot does not provide real SSH access.
Use only in isolated/test environments. Exposing it publicly can be risky.

