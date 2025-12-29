import time
from zeus_apple_silicon import AppleEnergyMonitor

# 1. Initialize the monitor (needs sudo to run the script)
monitor = AppleEnergyMonitor()

def benchmark_inference():
    print("🚀 Starting local LLM inference benchmark...")
    
    # 2. Start measurement window
    monitor.begin_window("local_llm_run")
    
    # --- SIMULATE LLM INFERENCE ---
    # In a real project, put your llama-cpp or MLX code here
    start_time = time.time()
    time.sleep(5)  # Simulating 5 seconds of 100% GPU load
    end_time = time.time()
    # ------------------------------
    
    # 3. End measurement and grab metrics
    metrics = monitor.end_window("local_llm_run")
    
    # 4. Calculate total energy in Joules (mj / 1000)
    total_joules = (metrics.cpu_total_mj + metrics.gpu_mj + metrics.ane_mj) / 1000
    
    print(f"\n✅ Benchmark Complete")
    print(f"⏱️ Duration: {end_time - start_time:.2f} seconds")
    print(f"⚡ Total Energy: {total_joules:.2f} Joules")
    print(f"🔥 GPU Energy: {metrics.gpu_mj / 1000:.2f} Joules")

if __name__ == "__main__":
    benchmark_inference()
