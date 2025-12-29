![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![macOS](https://img.shields.io/badge/mac%20os-000000?style=for-the-badge&logo=apple&logoColor=white)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)
# Local LLM Energy Benchmarking (macOS M4 Max)

## Overview
A software engineering tool designed to quantify the computational and energy cost of running Large Language Models (LLMs) locally on Apple Silicon. 

## Key Features
* **Real-time Energy Tracking:** Uses `zeus-apple-silicon` to measure energy usage.
* **Hardware-Specific Profiling:** Optimized for M4 Max Unified Memory.

## Tech Stack
* **Language:** Python 3.14+
* **Core Library:** `zeus-apple-silicon`

## Installation & Usage
1. **Clone and Setup:**

   ```bash
   git clone <your-repo-link>
   cd llm-benchmarking
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt

   ```
## 📊 Benchmark Results (M4 Max)

| Workload | Duration (s) | Total Energy (J) | GPU Energy (J) |
| :--- | :---: | :---: | :---: |
| Llama-3-8B (Simulated) | 5.01 | 0.07 | 0.03 |
| Idle Baseline | 5.00 | ~0.01 | 0.00 |

| Qwen 2.5 32B | 5.01s | 174.33 J | 170.46 J | 1.937 J/Tok |
