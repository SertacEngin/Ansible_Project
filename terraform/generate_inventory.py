import json
import subprocess

result = subprocess.run(
    ["terraform", "output", "-json"],
    capture_output=True,
    text=True
)

data = json.loads(result.stdout)

master_ip = data["master_ip"]["value"]
worker_ip = data["worker_ip"]["value"]

inventory = f"""
all:
  vars:
    ansible_user: root
    ansible_ssh_private_key_file: ~/.ssh/hetzner_key

  children:
    web:
      hosts:
        web-1:
          ansible_host: {master_ip}

    app:
      hosts:
        app-1:
          ansible_host: {worker_ip}
"""

with open("inventory.yml", "w") as f:
    f.write(inventory)

print("Inventory created!")
