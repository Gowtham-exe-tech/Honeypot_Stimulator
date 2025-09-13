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

