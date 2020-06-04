import requests
import json

r = requests.get('https://formulae.brew.sh/api/formula.json')
packages_json = r.json()

packages_str = json.dumps(packages_json, indent=2)

print(packages_str)