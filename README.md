# Local LLM Energy Benchmarking (M4 Max)

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![macOS](https://img.shields.io/badge/mac%20os-000000?style=for-the-badge&logo=apple&logoColor=white)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)

## 📋 Overview
A software engineering tool designed to quantify the computational and energy cost of running Large Language Models (LLMs) locally on Apple Silicon.

### Key Features
* **Real-time Energy Tracking:** Uses `zeus-apple-silicon` to measure actual hardware draw.
* **Hardware-Specific Profiling:** Optimized for the M4 Max Unified Memory architecture.

---

## 📊 Benchmark Results

| Model | Duration | Total Energy | GPU Energy | Efficiency |
| :--- | :---: | :---: | :---: | :---: |
| **Qwen 2.5 32B** | 5.01s | 174.33 J | 170.46 J | **1.937 J/Tok** |
| **Idle Baseline** | 5.00s | 0.40 J | 0.10 J | N/A |

---

## 🛠️ Tech Stack
* **Language:** Python 3.12+
* **Framework:** Ollama (Local Inference)
* **Energy API:** `zeus-apple-silicon`

## ⚙️ Installation & Usage
```bash
# Clone the repository
git clone [https://github.com/HoldenHrabak/llm-benchmarking.git](https://github.com/HoldenHrabak/llm-benchmarking.git)
cd llm-benchmarking

# Setup Environment
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Run Benchmark (Requires sudo for hardware sensors)
sudo ./venv/bin/python monitor_energy.py
