def generate_recommendations(usage):
    recs = []
    for s in usage["services"]:
        if s["name"].startswith("VM") and s["cpu_usage"] < 20:
            recs.append(f"Rightsize {s['name']} (low CPU).")
        if s["name"].startswith("Storage") and s["size_gb"] > 80:
            recs.append(f"Move {s['name']} to cold storage.")
    return recs
