import ollama
import time
from zeus_apple_silicon import AppleEnergyMonitor

monitor = AppleEnergyMonitor()

def benchmark_real_llm(model_name, user_prompt):
    print(f"🚀 Running benchmark for: {model_name}")
    print(f"📝 Prompt: {user_prompt}")
    
    # 1. Start the energy "window"
    monitor.begin_window("llm_inference")
    start_time = time.time()

    # 2. Trigger the local LLM
    response = ollama.generate(model=model_name, prompt=user_prompt)

    # 3. End the energy "window"
    duration = time.time() - start_time
    metrics = monitor.end_window("llm_inference")

    # 4. Extract data
    total_j = (metrics.cpu_total_mj + metrics.gpu_mj + metrics.ane_mj) / 1000
    token_count = response.get('eval_count', 1) # Total tokens generated
    j_per_token = total_j / token_count

    print(f"\n✅ Benchmark Complete!")
    print(f"⏱️  Duration: {duration:.2f}s")
    print(f"⚡ Total Energy: {total_j:.2f} Joules")
    print(f"🔋 Efficiency: {j_per_token:.4f} Joules/Token")
    print("-" * 30)

if __name__ == "__main__":
    # Test your 32B model with a real coding prompt
    benchmark_real_llm("qwen2.5-coder:32b", "Write a Python script for a binary search tree.")
