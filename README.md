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
