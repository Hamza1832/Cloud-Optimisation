import json
import random
import time

FILE_PATH = "usage.json"

def generate_usage():
    services = [
        {
            "name": "VM1",
            "cpu_usage": round(random.uniform(5, 90), 2),
            "ram_gb": random.choice([2, 4, 8]),
            "hours": 1,
            "cost": round(random.uniform(0.05, 0.3), 2)
        },
        {
            "name": "VM2",
            "cpu_usage": round(random.uniform(10, 95), 2),
            "ram_gb": random.choice([4, 8, 16]),
            "hours": 1,
            "cost": round(random.uniform(0.1, 0.5), 2)
        },
        {
            "name": "Storage1",
            "size_gb": random.randint(50, 500),
            "cost": round(random.uniform(0.01, 0.2), 2)
        }
    ]
    return {"services": services}

def main():
    while True:
        usage_data = generate_usage()
        with open(FILE_PATH, "w") as f:
            json.dump(usage_data, f, indent=2)
        print(f"Updated {FILE_PATH}")
        time.sleep(30)  # update every 30 seconds

if __name__ == "__main__":
    main()
