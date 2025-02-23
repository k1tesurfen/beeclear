# utils.py
import os
from datetime import datetime


def create_output_dir():
    timestamp = datetime.now().strftime("%Y-%m-%d-%H%M")
    output_dir = f"beeclear-{timestamp}"
    os.makedirs(output_dir, exist_ok=True)
    return output_dir
