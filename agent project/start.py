import subprocess
import sys

def main():
    script_path = "app.py"
    
    # 使用streamlit运行
    subprocess.run([sys.executable, "-m", "streamlit", "run", script_path])

if __name__ == "__main__":
    main()