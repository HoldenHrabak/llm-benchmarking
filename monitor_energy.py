import ollama
import time
import csv
import os
import uuid  # Used to link the two files together
from zeus_apple_silicon import AppleEnergyMonitor

# 1. Selection Menu
print("--- LLM Energy Benchmark Suite ---")
print("1) Qwen 2.5 Coder 32B")
print("2) Qwen 2.5 Coder 7B")
choice = input("Select model (1 or 2): ")

if choice == "1":
    MODEL = "qwen2.5-coder:32b"
    METRIC_FILE = "benchmarks_32b.csv"
    TEXT_FILE = "responses_32b.csv"
else:
    MODEL = "qwen2.5-coder:7b"
    METRIC_FILE = "benchmarks_7b.csv"
    TEXT_FILE = "responses_7b.csv"

monitor = AppleEnergyMonitor()

def init_logs():
    """Initializes both CSV files with appropriate headers."""
    # Initialize Metrics File (Numbers Only)
    if not os.path.exists(METRIC_FILE):
        with open(METRIC_FILE, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(["ID", "Timestamp", "Model", "Prompt_Snippet", "Duration(s)", "TotalEnergy(J)", "Tokens", "J/Token"])
    
    # Initialize Responses File (Full Text)
    if not os.path.exists(TEXT_FILE):
        with open(TEXT_FILE, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f, quoting=csv.QUOTE_MINIMAL)
            writer.writerow(["ID", "Timestamp", "Model", "Full_Prompt", "Full_Response"])

def log_data(metric_data, text_data):
    """Saves numbers to one file and text to another."""
    # Write to Metric File
    with open(METRIC_FILE, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(metric_data)
        
    # Write to Text File
    with open(TEXT_FILE, 'a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f, quoting=csv.QUOTE_MINIMAL)
        writer.writerow(text_data)

def start_benchmark():
    init_logs()
    print(f"\n🚀 Monitoring {MODEL}")
    print(f"📊 Metrics -> {METRIC_FILE}")
    print(f"📄 Full Text -> {TEXT_FILE}\n")
    
    while True:
        prompt = input("🤖 Ask AI (type 'exit' to quit): ")
        if prompt.lower() in ['exit', 'quit']: break
        
        # Generate a unique ID to link the row in the metric file to the row in the response file
        run_id = str(uuid.uuid4())[:8] 
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")

        print("⚡ Measuring...")
        monitor.begin_window("inference")
        start_t = time.time()

        try:
            response = ollama.generate(model=MODEL, prompt=prompt)
            duration = time.time() - start_t
            metrics = monitor.end_window("inference")

            total_j = (metrics.cpu_total_mj + metrics.gpu_mj + metrics.ane_mj) / 1000
            tokens = response.get('eval_count', 1)
            j_per_token = total_j / tokens

            print(f"\n--- AI RESPONSE ---\n{response['response'][:200]}...\n")
            print(f"📊 Stats: {total_j:.2f}J | {j_per_token:.4f} J/Tok\n")

            # 1. Save numbers to METRIC_FILE
            log_data(
                [run_id, timestamp, MODEL, prompt[:30], f"{duration:.2f}", f"{total_j:.2f}", tokens, f"{j_per_token:.4f}"],
                [run_id, timestamp, MODEL, prompt, response['response']]
            )

        except Exception as e:
            print(f"❌ Error: {e}")

if __name__ == "__main__":
    start_benchmark()
