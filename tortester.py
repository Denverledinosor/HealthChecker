import requests
import concurrent.futures

def check_health(target):
    try:
        response = requests.get(target)
        if response.status_code == 200:
            return f"{target} is healthy"
        else:
            return f"{target} is not healthy (Status code: {response.status_code})"
    except requests.exceptions.RequestException as e:
        return f"{target} is not healthy ({e})"

# Specify the path to your text file containing the target URLs
file_path = "target_list.txt"

# Read target URLs from the file
with open(file_path, "r") as file:
    targets = file.read().splitlines()

# Adjust the max_workers parameter to control the degree of parallelism
max_workers = 5  # You can increase or decrease this value

with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
    results = list(executor.map(check_health, targets))

for result in results:
    print(result)