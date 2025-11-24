def calculate_total_cost(usage):
    return sum(s.get("cost", 0) for s in usage["services"])