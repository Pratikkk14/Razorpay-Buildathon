"""Development server launcher: Runs FastAPI backend and Vite frontend concurrently."""
import subprocess
import sys
import time
import os
import signal


def run_dev():
    print("==================================================================")
    print("Starting Recovery Intelligence & Allocation Engine (Dev Mode)")
    print("==================================================================")

    root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    backend_dir = os.path.join(root_dir, "backend")
    frontend_dir = os.path.join(root_dir, "frontend")

    # Auto-detect myvenv if present
    python_exe = sys.executable
    if sys.platform == "win32":
        venv_py = os.path.join(root_dir, "myvenv", "Scripts", "python.exe")
    else:
        venv_py = os.path.join(root_dir, "myvenv", "bin", "python")
    
    if os.path.exists(venv_py):
        python_exe = venv_py
        print(f"[Environment] Using virtualenv Python: {python_exe}")

    # Start FastAPI Backend
    backend_cmd = [python_exe, "-m", "uvicorn", "app.main:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]
    env = os.environ.copy()
    env["PYTHONPATH"] = backend_dir
    print(f"[Backend] Starting on http://localhost:8000 (API docs: http://localhost:8000/docs)...")
    backend_proc = subprocess.Popen(backend_cmd, cwd=root_dir, env=env)

    # Start Vite Frontend
    npm_cmd = "npm.cmd" if sys.platform == "win32" else "npm"
    frontend_cmd = [npm_cmd, "run", "dev", "--", "--host"]
    print(f"[Frontend] Starting on http://localhost:5173...")
    frontend_proc = subprocess.Popen(frontend_cmd, cwd=frontend_dir)

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nStopping services...")
        backend_proc.terminate()
        frontend_proc.terminate()
        sys.exit(0)


if __name__ == "__main__":
    run_dev()
