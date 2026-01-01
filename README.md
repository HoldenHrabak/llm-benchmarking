# Local LLM Energy Benchmarking (M4 Max)

### Key Features
* **Real-time Energy Tracking:** Uses `zeus-apple-silicon` to measure actual hardware draw.
* **Hardware-Specific Profiling:** Optimized for the M4 Max Unified Memory architecture.

---

## Benchmark Summary Table

| Model | Efficiency (J/Tok) | Avg. Total Energy (J) | Technical Score | Primary Use Case |
| :--- | :---: | :---: | :---: | :--- |
| **Qwen 2.5 7B** | ~0.45 | ~295 | 3/10 | Low-latency, basic scripts |
| **Qwen 2.5 32B** | ~2.14 | ~3823 | 10/10 | Complex math, Metal/MLX GPU optimization |


---

## Tech Stack
* **Language:** Python 3.12+
* **Framework:** Ollama (Local Inference)
* **Energy API:** `zeus-apple-silicon`

##️ Installation & Usage
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

### Energy Efficiency Results
![Energy Efficiency Comparison](energy_comparison.png)

Project Findings: M4 Max LLM Performance
My benchmarking of Qwen 2.5 Coder (7B vs 32B) on Apple Silicon reveals the "Intelligence Tax" associated with high-reasoning tasks:

Efficiency Threshold: The 7B model achieved a ~5x improvement in energy efficiency, consuming only ~0.45 J/Token compared to the 32B model's ~2.14 J/Token.

The Capability Gap: Despite the efficiency of the smaller model, it failed to produce valid Metal/MLX code for complex 3D math, often hallucinating non-existent Python libraries.

Hardware Optimization: The 32B model consistently utilized the M4 Max Unified Memory more effectively for long-context generation, maintaining a "Quality-per-Joule" score that justifies its higher power draw for systems engineering tasks.

Hardware Specifications
Device: MacBook Pro (M4 Max).

Unified Memory: 128GB (approx. 400 GB/s bandwidth).

Telemetry Tool: zeus-apple-silicon (sampling CPU, GPU, and ANE power domains).
