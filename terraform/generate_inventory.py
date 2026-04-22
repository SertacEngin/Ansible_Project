import json
import subprocess
import os

# -----------------------------
# Terraform Output holen
# -----------------------------
result = subprocess.run(
    ["terraform", "output", "-json"],
    capture_output=True,
    text=True,
    cwd="."  # wichtig: im terraform folder ausführen
)

data = json.loads(result.stdout)

servers = data["servers"]["value"]

web_ip = servers["web"]["ip"]
app_ip = servers["app"]["ip"]

# -----------------------------
# Zielpfad für Ansible Inventory
# -----------------------------
inventory_path = "../ansible/inventories/production/inventory.yml"

# Ordner erstellen falls nicht existiert
os.makedirs(os.path.dirname(inventory_path), exist_ok=True)

# -----------------------------
# Inventory Inhalt
# -----------------------------
inventory = f"""
all:
  vars:
    ansible_user: root
    ansible_ssh_private_key_file: /home/sertac/.ssh/hetzner_key

  children:
    web:
      hosts:
        web-1:
          ansible_host: {web_ip}

    app:
      hosts:
        app-1:
          ansible_host: {app_ip}
"""

# -----------------------------
# Datei schreiben
# -----------------------------
with open(inventory_path, "w") as f:
    f.write(inventory)

print(f"Inventory created at {inventory_path}")
