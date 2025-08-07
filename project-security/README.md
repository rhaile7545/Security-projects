# 🛡️ Project Security: Offensive & Defensive Lab

A comprehensive home lab project that simulates a small enterprise environment for red and blue team practice. The lab showcases the full cyber kill chain and defense-in-depth strategies.

## 🧰 Lab Stack
- **VirtualBox**: Hosting 7 interconnected VMs.
- **Windows Server 2025**: AD, DNS, DHCP.
- **Ubuntu (Postfix SMTP Server)**: Mail delivery.
- **Security Onion & Wazuh**: Detection, alerting, and log analysis.
- **Kali Linux**: Red team operations using Evil-WinRM, Hydra, NetExec, and SecLists.

## 📌 Key Activities
- Built a **NAT-based network** with enterprise-grade components.
- Configured **Active Directory** and core infrastructure.
- Deployed **Wazuh & Security Onion** for endpoint and network detection.
- Simulated real-world attacks: **brute force**, **privilege escalation**, and **lateral movement**.
- Demonstrated **full attack lifecycle**, from initial access to post-exploitation.

## 🧪 Red Team Tools
- Evil-WinRM
- Hydra
- NetExec
- SecLists

## 🎯 Blue Team Tools
- Security Onion
- Wazuh
- Syslog / Elastic Stack

## 📎 Files Included
- `network-diagram.png`: Visual overview of lab topology.
- `VM-configurations/`: Screenshots and setup guides.
- `attack-playbooks/`: Step-by-step attack methodology.
- `logs-and-alerts/`: Sample detection logs.

## ✅ Learning Outcomes
- Understood enterprise system design and implementation.
- Practiced both offensive tactics and defensive monitoring.
- Improved incident response skills and log analysis techniques.
