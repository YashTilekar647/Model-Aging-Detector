def generate_report(metrics, status):
    with open("reports/aging_report.txt", "a") as f:
        f.write("\n--- MODEL AGING REPORT ---\n")
        for k, v in metrics.items():
            f.write(f"{k}: {v}\n")
        f.write(f"STATUS: {status}\n")
