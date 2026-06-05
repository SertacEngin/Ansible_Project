# Ansible Infrastructure Automation Platform

## Overview

This project demonstrates a fully automated infrastructure provisioning and configuration management system using Terraform and Ansible.

It provisions cloud servers on Hetzner and configures them into a production-like environment with web services, monitoring, logging, security hardening, and system services.

The goal is to simulate real-world Infrastructure as Code (IaC) and Configuration Management workflows.

---

## Architecture

Terraform provisions the infrastructure, and Ansible configures and manages the system state:

Terraform → Hetzner Cloud → Ubuntu Servers → Ansible Configuration → Services (Web + App + Monitoring)

---

## Infrastructure Provisioning (Terraform)

Infrastructure is provisioned using Terraform on Hetzner Cloud.

It creates:

* 2 Ubuntu servers (web + app)
* SSH key-based access
* Standardized server configuration
* Output-driven inventory generation for Ansible automation

The infrastructure is fully reproducible and can be recreated from scratch using a single Terraform apply.

---

## Configuration Management (Ansible)

Ansible is used to configure and standardize all servers after provisioning.

### Core responsibilities:

* System updates and base tools installation
* User and security management
* Firewall configuration (UFW)
* Fail2ban for brute-force protection
* NTP synchronization (chrony)
* MOTD standardization
* Web server provisioning (Nginx)

---

## Web Layer (Nginx)

The web server is configured using Ansible:

* Nginx installation and service management
* Automated deployment of static content via templates
* Health check endpoint for monitoring
* Fully automated configuration rollout

---

## Monitoring Stack

A lightweight observability stack is deployed:

### Components:

* Node Exporter (system metrics collection)
* Prometheus (metrics aggregation and scraping)
* Grafana (visualization dashboard)

### Features:

* System-level metrics monitoring
* Multi-server scraping configuration
* Service-based monitoring via systemd
* Centralized observability setup

---

## Security Hardening

The infrastructure includes basic security best practices:

* UFW firewall with restricted ports (SSH, HTTP, monitoring ports)
* Fail2ban for SSH brute-force protection
* Dedicated system users for services
* Disabled interactive login for service accounts

---

## Automation Flow

### End-to-end workflow:

1. Terraform provisions cloud infrastructure (Hetzner)
2. Inventory is generated dynamically
3. GitHub Actions triggers Ansible pipeline
4. SSH key is injected securely via CI/CD secrets
5. Ansible configures all servers automatically
6. Monitoring + services are deployed and started

---

## CI/CD Pipeline (GitHub Actions)

An automated deployment pipeline is implemented using GitHub Actions.

### Pipeline flow:

1. Code is pushed to main branch
2. GitHub Actions runner installs Ansible dependencies
3. SSH key is securely loaded from secrets
4. Ansible playbook is executed against infrastructure
5. Configuration is applied in a fully automated way

### Features:

* Zero manual server configuration
* Secure SSH-based deployment
* Reproducible infrastructure state
* Fully automated configuration management

---

## Key Concepts Demonstrated

* Infrastructure as Code (Terraform)
* Configuration Management (Ansible)
* Idempotent system design
* Immutable infrastructure principles
* Service orchestration
* Monitoring & observability
* Security hardening
* CI/CD automation

---

## Roles Structure (Ansible Design)

The system is modular and role-based:

* common → base system setup
* firewall → security layer
* fail2ban → intrusion protection
* nginx → web server setup
* monitoring → Prometheus + Node Exporter
* grafana → visualization
* prometheus → metrics backend
* ntp → time synchronization
* motd → system standardization

---

## Monitoring & Observability

The system exposes:

* CPU / memory / disk usage (Node Exporter)
* Application metrics via Prometheus scraping
* Grafana dashboards for visualization

Targets are dynamically configured using Ansible inventory variables.

---

## Technologies Used

* Terraform
* Ansible
* Hetzner Cloud API
* Ubuntu Linux
* Nginx
* Prometheus
* Grafana
* Node Exporter
* GitHub Actions
* UFW / Fail2ban / Chrony

---

## Purpose of this Project

This project was built to simulate real-world DevOps and infrastructure automation scenarios, including:

* Cloud provisioning
* Configuration management
* Security hardening
* Monitoring systems
* CI/CD deployment pipelines

---

## Future Improvements

* Add Docker-based deployments
* Centralized logging (ELK / Loki)
* Role-based access control (RBAC)
* Ansible Vault for secrets management
* Multi-environment support (dev/staging/prod)
* High availability architecture
