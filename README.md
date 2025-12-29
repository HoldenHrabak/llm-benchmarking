# Local LLM Energy Benchmarking (M4 Max)

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
