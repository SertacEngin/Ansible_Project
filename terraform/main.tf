terraform {
  required_providers {
    hcloud = {
      source  = "hetznercloud/hcloud"
      version = "~> 1.45"
    }
  }
}

provider "hcloud" {
  token = var.hcloud_token
}

# =========================
# VARIABLES
# =========================

variable "hcloud_token" {
  type      = string
  sensitive = true
}

variable "ssh_public_key_path" {
  type    = string
  default = "/home/sertac/.ssh/hetzner_key.pub"
}

variable "server_type" {
  type    = string
  default = "cx23"
}

variable "image" {
  type    = string
  default = "ubuntu-22.04"
}

variable "location" {
  type    = string
  default = "nbg1"
}

# =========================
# SSH KEY
# =========================

resource "hcloud_ssh_key" "default" {
  name       = "ansible-project-key"
  public_key = trimspace(file(var.ssh_public_key_path))
}

# =========================
# SERVERS
# =========================

resource "hcloud_server" "web" {
  name        = "web-1"
  image       = var.image
  server_type = var.server_type
  location    = var.location

  ssh_keys = [hcloud_ssh_key.default.id]
}

resource "hcloud_server" "app" {
  name        = "app-1"
  image       = var.image
  server_type = var.server_type
  location    = var.location

  ssh_keys = [hcloud_ssh_key.default.id]
}

# =========================
# OUTPUTS (für Python Script)
# =========================

output "servers" {
  value = {
    web = {
      name = hcloud_server.web.name
      ip   = hcloud_server.web.ipv4_address
    }
    app = {
      name = hcloud_server.app.name
      ip   = hcloud_server.app.ipv4_address
    }
  }
}
