import pandas as pd
import ollama

# Load your two data files
df32 = pd.read_csv("benchmarks_32b.csv")
df7 = pd.read_csv("benchmarks_7b.csv")

def get_judge_score(prompt, answer):
    judge_prompt = f"""
    You are a technical judge. Rate the following AI answer on a scale of 1-10 
    based on technical accuracy, code quality, and how well it followed the prompt.
    
    ORIGINAL PROMPT: {prompt}
    AI ANSWER: {answer}
    
    Provide ONLY a single number as your response (e.g., '8').
    """
    response = ollama.generate(model="qwen2.5-coder:32b", prompt=judge_prompt)
    return response['response'].strip()

# Grade the last entry in each file
print(f"32B Score: {get_judge_score(df32.iloc[-1]['Prompt'], df32.iloc[-1]['Response'])}")
print(f"7B Score: {get_judge_score(df7.iloc[-1]['Prompt'], df7.iloc[-1]['Response'])}")
