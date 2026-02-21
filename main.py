import requests

def does_it_exist(version):
    url = f"https://osu.ai/api/download-desktop-client?url=https%3A%2F%2Fcdn-releases.osu.ai%2FOsuAI_{version}_x64_en-US.msi"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print(f"Version {version}: It exists!")
        else:
            pass
    except requests.exceptions.RequestException as e:
        print(f"Version {version}: Request failed ({e})")

for major in range(4):
    does_it_exist(f"{major}")
    if major == 3:
        does_it_exist("3.0")
        does_it_exist("3.0.0")
        break
        
    for minor in range(10):
        does_it_exist(f"{major}.{minor}")
        for patch in range(10):
            does_it_exist(f"{major}.{minor}.{patch}")
