def calculate_statistics(data):
    if not data:
        return None
    return {
        "mean": sum(data) / len(data),
        "min": min(data),
        "max": max(data),
        "count": len(data)
    }
