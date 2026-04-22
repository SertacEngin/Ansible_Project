# 🚀 DevOps Automation Project (Terraform + Ansible + CI/CD)

## 📌 Overview

This project demonstrates a complete **Infrastructure as Code (IaC)** and **Configuration Management** workflow using modern DevOps tools.

It automates the provisioning, configuration, and basic hardening of a multi-server environment, including application deployment and CI validation pipelines.

The goal of this project is to simulate a real-world cloud infrastructure setup and demonstrate end-to-end DevOps practices.

---

## 🏗 Architecture

The system consists of the following components:

- **Infrastructure Layer** → Terraform
- **Configuration Management** → Ansible
- **Automation Bridge** → Python (Terraform → Ansible Inventory)
- **CI/CD Pipeline** → GitHub Actions
- **Application Layer** → Nginx Web Server

---

## 🔄 Workflow

```text
Terraform → Provisions VMs (Hetzner Cloud)
        ↓
Python Script → Generates dynamic Ansible inventory
        ↓
Ansible → Configures servers (users, security, services)
        ↓
GitHub Actions → Validates Terraform & Ansible code

🧱 Infrastructure (Terraform)

Provisioning is done using:

Hetzner Cloud VMs
Private networking
SSH key-based access

Resources include:

Web server
Application server
⚙ Configuration Management (Ansible)

Ansible is used for automated configuration:

Roles implemented:
common → Base system setup
users → User provisioning with Vault-managed secrets
sudoers → Privilege configuration
ntp → Time synchronization
firewall → UFW configuration
fail2ban → Basic security hardening
nginx → Application deployment
monitoring → Basic system visibility (health info)
🔐 Security

Security is handled using:

SSH key authentication
Ansible Vault for secret management
UFW firewall rules
Fail2Ban intrusion prevention
Sudo privilege separation
🌐 Application

A simple Nginx web application is deployed:

Dynamic index page using Ansible templates
Displays hostname and deployment metadata
Serves as a demo application layer
🔄 CI/CD Pipeline

Implemented using GitHub Actions:

Pipeline checks:
Terraform validation
Ansible syntax check

This ensures:

Infrastructure code correctness
Configuration correctness
Early detection of errors before deployment
🐍 Automation Bridge

A Python script is used to:

Extract Terraform outputs
Generate dynamic Ansible inventory
Ensure Infrastructure and Configuration layers are decoupled
📊 Monitoring (Basic)

Basic system visibility includes:

Installed diagnostic tools (htop, net-tools)
System information file per server
Health check endpoint via Nginx
🧪 How to Use
1. Provision infrastructure
cd terraform
terraform init
terraform apply
2. Generate Ansible inventory
cd terraform
python3 generate_inventory.py
3. Run Ansible configuration
cd ansible
ansible-playbook playbooks/site.yml --ask-vault-pass
4. Run CI checks

Push to GitHub or open a Pull Request to trigger pipeline.

📁 Project Structure
terraform/
ansible/
  ├── roles/
  ├── playbooks/
  ├── inventories/
.github/
  └── workflows/
🎯 Key Learnings
Infrastructure as Code with Terraform
Configuration Management with Ansible
Secure secret handling using Ansible Vault
CI/CD automation with GitHub Actions
Separation of infrastructure and configuration layers
Modular DevOps architecture design
🚀 Future Improvements
Centralized logging (ELK / Loki)
Prometheus monitoring
SSH hardening role
Auto-scaling infrastructure
Docker containerization
Kubernetes migration
👤 Author

DevOps automation project built for learning and demonstrating production-like infrastructure workflows.


---

# 🧠 Warum diese README stark ist

Sie zeigt im Interview:

- Architekturverständnis
- Toolchain-Verständnis
- Security Awareness
- CI/CD Verständnis
- klare Strukturierung
- „production thinking“

---

# 🚀 Wenn du willst

Ich kann als nächsten Schritt noch machen:

- 🔥 :contentReference[oaicite:0]{index=0}
- 🔥 :contentReference[oaicite:1]{index=1}
- 🔥 :contentReference[oaicite:2]{index=2}

Sag einfach 👍
