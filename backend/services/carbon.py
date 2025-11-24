import requests

# Replace YOUR_TOKEN_HERE with your free auth token from ElectricityMap
ELECTRICITYMAP_TOKEN = "rjaNmOLRULXira3g0fOj"
ZONE = "TN"  # Tunisia

def carbon_intensity():
    """
    Fetches latest carbon intensity (gCO2/kWh) for Tunisia from ElectricityMap API
    Returns: dict with carbon_g_per_kWh
    """
    url = f"https://api.electricitymaps.com/v3/carbon-intensity/latest?zone={ZONE}"
    headers = {"auth-token": ELECTRICITYMAP_TOKEN}

    try:
        response = requests.get(url, headers=headers, timeout=5)
        response.raise_for_status()  # raise error if not 200
        data = response.json()
        carbon_g_per_kWh = data.get("carbonIntensity", 0)  # fallback to 0
        return {"carbon_g_per_kWh": carbon_g_per_kWh}
    except requests.RequestException as e:
        print(f"Error fetching carbon data: {e}")
        return {"carbon_g_per_kWh": 0}
