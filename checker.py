import requests
from packaging import version

def parse_requirements(file_path='requirements_sample.txt'):
    with open(file_path) as f:
        lines = f.readlines()
    return [line.strip() for line in lines if line and not line.startswith('#')]

def get_latest_version(package):
    url = f"https://pypi.org/pypi/{package}/json"
    res = requests.get(url)
    if res.status_code == 200:
        return res.json()["info"]["version"]
    return None

def check_updates():
    outdated = []
    for line in parse_requirements():
        if '==' not in line:
            continue
        pkg, current_ver = line.split('==')
        latest_ver = get_latest_version(pkg)
        if latest_ver and version.parse(current_ver) < version.parse(latest_ver):
            outdated.append({
                'package': pkg,
                'current': current_ver,
                'latest': latest_ver
            })
    return outdated
