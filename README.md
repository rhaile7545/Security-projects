# 🧪 So You Want to be a SOC Analyst

This project simulates a real-world Security Operations Center (SOC) environment using a home lab setup. It focuses on endpoint detection, response capabilities, and threat simulation using a C2 framework.

## 🔧 Tools & Technologies
- Sysmon
- LimaCharlie EDR
- Sliver Command & Control Framework
- Windows VM (Victim)
- Ubuntu Linux (Attacker)

## 🛠️ What I Did
- **Disabled Windows Defender** to test system exposure to threats.
- **Configured Sysmon** for detailed event logging and telemetry.
- **Deployed LimaCharlie**, enabling endpoint visibility and response.
- **Set up a C2 framework** to simulate real-world attack vectors.
- **Executed simulated attacks**, including initial access and lateral movement.
- **Developed custom detection rules** in LimaCharlie to catch malicious behavior.

## 📊 Outcomes
- Successfully detected C2 communications and privilege escalations.
- Created reusable detection rules to identify abnormal behaviors.
- Gained hands-on experience in blue team defense and red team simulation.

## 📎 Resources
- `sysmon-config.xml`: Custom Sysmon configuration.
- `lima-charlie-detections/`: YAML/JSON detection rules.
- `attack-simulation-logs/`: Event logs showing attack detection and response.
