🚀 DevOps Automation Project (Terraform + Ansible + CI/CD)
📌 Overview

This project demonstrates a complete Infrastructure as Code (IaC) and Configuration Management workflow using modern DevOps tools.

It automates the provisioning, configuration, and basic hardening of a multi-server environment, including application deployment and CI validation pipelines.

The goal was not just to “make things work”, but to simulate how a real-world DevOps setup looks like — where infrastructure, configuration, deployment, and observability all come together.

🏗 Architecture

The system is built as a small but realistic multi-node environment:

Web Server (web-1) → serves the application via Nginx
Application / Monitoring Server (app-1) → hosts services and monitoring stack

Core components:

Infrastructure Layer → Terraform
Configuration Management → Ansible
Automation Bridge → Python (Terraform → Ansible Inventory)
CI/CD Pipeline → GitHub Actions
Application Layer → Nginx
Monitoring Stack → Node Exporter + Prometheus + Grafana
🔄 Workflow

Terraform provisions the infrastructure in Hetzner Cloud.
A Python script extracts the outputs and generates a dynamic Ansible inventory.
Ansible then configures the servers, deploys the application, and applies security settings.
GitHub Actions validates the setup automatically on each push.

This separation keeps infrastructure and configuration cleanly decoupled, which reflects real-world DevOps practices.

🧱 Infrastructure (Terraform)

Provisioning includes:

Virtual machines (Hetzner Cloud)
SSH key-based access
Region and instance configuration

Two main nodes are created:

web-1 → public-facing web server
app-1 → backend + monitoring node
⚙ Configuration Management (Ansible)

Ansible is used to fully automate server configuration in a modular way.

Implemented roles:

common → base packages and system setup
users → user creation with Vault-managed passwords
sudoers → privilege configuration
ntp → time synchronization
firewall → UFW configuration
fail2ban → intrusion prevention
nginx → application deployment
monitoring → metrics collection setup
prometheus → metrics aggregation
grafana → visualization layer

The setup is fully idempotent and can be re-run safely at any time.

🔐 Security

Basic security best practices are implemented:

SSH key authentication (no password login)
Ansible Vault for secret management
UFW firewall rules (restricted ports)
Fail2Ban for intrusion prevention
Separation of user privileges
🌐 Application

A simple Nginx-based web application is deployed:

Dynamic index page via Ansible templates
Displays hostname and deployment metadata
Acts as a lightweight demo application
📊 Monitoring & Observability

To move beyond deployment into real operations, a lightweight monitoring stack was added.

What is monitored?

Each server runs Node Exporter, which exposes system-level metrics such as:

CPU usage
Memory usage
Disk utilization
Network activity
Metrics Collection

A central Prometheus instance (running on app-1) collects metrics from both servers.

This follows a pull-based model, where Prometheus periodically scrapes metrics endpoints from each node.

Visualization

Grafana is used to visualize the data:

Pre-built dashboards for system metrics
Real-time visibility into server health
Easy identification of bottlenecks

This turns the project from “deployment automation” into a real operational system.

🔄 CI/CD Pipeline

Implemented using GitHub Actions.

The pipeline focuses on validation rather than provisioning:

Terraform validation
Ansible syntax checks

This ensures:

Early detection of errors
Consistent infrastructure definitions
Safe configuration changes

Infrastructure provisioning (Terraform apply) is intentionally kept outside the pipeline, as it is not part of frequent deployments.

🐍 Automation Bridge

A small Python script connects Terraform and Ansible:

Reads Terraform outputs
Generates a dynamic inventory file
Keeps both layers loosely coupled

This reflects a common real-world pattern where tools are integrated instead of tightly coupled.

🧪 How to Use
Provision infrastructure
Navigate to the Terraform directory and apply the configuration
Generate inventory
Run the Python script to create the Ansible inventory
Configure servers
Execute the Ansible playbook with Vault password
Validate via CI/CD
Push changes to trigger GitHub Actions
🎯 Key Learnings
Infrastructure as Code with Terraform
Configuration Management with Ansible
Secure secret handling using Ansible Vault
CI/CD validation pipelines
Monitoring with Prometheus and Grafana
Separation of infrastructure and configuration
Designing modular and maintainable DevOps systems
🚀 Future Improvements
Centralized logging (ELK / Loki)
Alerting with Prometheus Alertmanager
SSH hardening role
Auto-scaling infrastructure
Containerization with Docker
Migration to Kubernetes
👤 Author

Sertac Engin

DevOps automation project built to simulate production-like infrastructure workflows and demonstrate practical, end-to-end system design.
