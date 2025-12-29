import ollama
import time
import sys
from zeus_apple_silicon import AppleEnergyMonitor

# Initialize the hardware monitor
monitor = AppleEnergyMonitor()

def run_benchmarked_query(model_name, prompt):
    print(f"\nTarget Model: {model_name}")
    print(f"Sending Prompt: \"{prompt[:50]}...\"")
    print("-" * 40)

    try:
        # 1. Start the hardware measurement window
        monitor.begin_window("ai_inference")
        start_time = time.time()

        # 2. Trigger the Local LLM (Non-streaming for precise measurement)
        # We use ollama.generate to get the usage metadata (token counts)
        response = ollama.generate(model=model_name, prompt=prompt)

        # 3. Stop the hardware measurement window
        duration = time.time() - start_time
        metrics = monitor.end_window("ai_inference")

        # 4. Extract Energy Data (mJ to Joules)
        total_j = (metrics.cpu_total_mj + metrics.gpu_mj + metrics.ane_mj) / 1000
        gpu_j = metrics.gpu_mj / 1000

        # 5. Extract Token Data from Ollama
        # eval_count is the number of tokens generated
        tokens = response.get('eval_count', 1) 
        tps = tokens / duration if duration > 0 else 0

        # 6. Calculate Efficiency
        joules_per_token = total_j / tokens if tokens > 0 else 0

        # PRINT RESULTS
        print(f"AI Response Received ({tokens} tokens)")
        print(f"Inference Time: {duration:.2f} seconds")
        print(f"Speed: {tps:.2f} tokens/sec")
        print(f"GPU Energy: {gpu_j:.2f} J")
        print(f"Total Energy: {total_j:.2f} J")
        print(f"Efficiency: {joules_per_token:.4f} Joules/Token")
        print("-" * 40)
        
        # Return the summary line for your README
        return f"| {model_name} | {duration:.2f}s | {total_j:.2f} J | {gpu_j:.2f} J | {joules_per_token:.4f} |"

    except Exception as e:
        print(f"Error during benchmark: {e}")
        return None

if __name__ == "__main__":
    # Ensure Ollama is running before starting!
    MODEL = "qwen2.5-coder:32b"
    TEST_PROMPT = "Write a highly optimized Python implementation of a 3D Mandelbrot fractal renderer."
    
    # Run the benchmark
    summary_row = run_benchmarked_query(MODEL, TEST_PROMPT)
    
    if summary_row:
        print(summary_row)
