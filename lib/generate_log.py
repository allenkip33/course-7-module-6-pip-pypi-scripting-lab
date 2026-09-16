from datetime import datetime
import os

def generate_log(data):
    if not isinstance(data, list):
        raise ValueError("Input data must be a list.")

    today_date = datetime.now().strftime("%Y%m%d")
    filename = f"log_{today_date}.txt"

    with open(filename, "w") as file:
        for entry in data:
            file.write(f"{entry}\n")

    print(f"Confirmation: Log written to {filename}")
    return filename
