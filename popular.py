import json

def install_sort(package):
    return package['analytics']['30d']

with open('packages_info.json', 'r') as f:
    data = json.load(f)

data.sort(key=install_sort, reverse=True)

data_str = json.dumps(data, indent=2)