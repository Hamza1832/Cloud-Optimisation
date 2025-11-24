from fastapi import FastAPI
import json
from services.cost import calculate_total_cost
from services.energy import calculate_energy
from services.recommendations import generate_recommendations
from services.carbon import carbon_intensity

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Cloud Optimizer API running"}

@app.get("/usage")
def get_usage():
    with open("../mock-data/usage.json") as f:
        data = json.load(f)
    return data

@app.get("/carbon")
def carbon_route():
    return carbon_intensity()

@app.get("/analysis")
def analysis():
    usage = get_usage()

    total_cost = calculate_total_cost(usage)
    cpu_hours = sum(item.get("hours", 0) for item in usage["services"])
    energy = calculate_energy(cpu_hours)
    carbon = carbon_intensity()
    recommendations = generate_recommendations(usage)
    print(cpu_hours)
    print(total_cost)
    print(energy)
    print(recommendations)
    return {
        "total_cost": total_cost,
        "energy_kWh": energy,
        "carbon": carbon,
        "recommendations": recommendations
    }
