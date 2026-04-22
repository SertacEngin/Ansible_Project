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
