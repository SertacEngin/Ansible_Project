import json
import subprocess

result = subprocess.run(
    ["terraform", "output", "-json"],
    capture_output=True,
    text=True,
    cwd="../terraform"
)

data = json.loads(result.stdout)

servers = data["servers"]["value"]

web_ip = servers["web"]["ip"]
app_ip = servers["app"]["ip"]

inventory = f"""
all:
  vars:
    ansible_user: root
    ansible_ssh_private_key_file: ~/.ssh/hetzner_key

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

with open("../ansible/inventories/production/inventory.yml", "w") as f:
    f.write(inventory)

print("Inventory created!")
