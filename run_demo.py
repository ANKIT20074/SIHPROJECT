"""
DoctorKavach (डॉक्टर कवच) — Unified Demo Launcher (Node.js + Express + React + SQLite)
Starts Node.js Express backend on http://127.0.0.1:8000
Starts Vite frontend on http://localhost:5173
Opens browser automatically for the SIH presentation.
"""

import os
import sys
import subprocess
import time
import webbrowser

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
        sys.stderr.reconfigure(encoding='utf-8', errors='replace')
    except Exception:
        pass

SERVER_DIR = os.path.join(ROOT_DIR, "server")
FRONTEND_DIR = os.path.join(ROOT_DIR, "frontend")

def print_banner():
    print("=" * 72)
    print("   DoctorKavach (डॉक्टर कवच) - SIH 2026 Full System Prototype Launcher   ")
    print("=" * 72)
    print("  [Backend]  Node.js + Express + SQLite WAL -> http://127.0.0.1:8000")
    print("  [Frontend] React + Tailwind CSS + Recharts -> http://localhost:5173")
    print("=" * 72)
    print("  5 Seeded Demo Accounts (Use 1-Click Role Switcher on Top Nav):")
    print("   1. Govt Health Officer: officer@health.gov.in    / Admin@2026")
    print("   2. Hospital Admin:      admin@safdarjung.in     / Hospital@2026")
    print("   3. Diagnostic Lab:      admin@lalpathlabs.in    / Lab@2026")
    print("   4. Doctor (NMC):        dr.sharma@doctorkavach.in / Doctor@2026")
    print("   5. Patient (ABHA):      ramesh@gmail.com        / Patient@2026")
    print("=" * 72)
    print("Press Ctrl+C to terminate both servers at any time.\n")

def main():
    print_banner()

    node_cmd = "node.exe" if os.name == "nt" else "node"
    npm_cmd = "npm.cmd" if os.name == "nt" else "npm"

    # 1. Start Node.js Express backend
    print(">>> [1/3] Starting Node.js Express Backend on port 8000...")
    backend_proc = subprocess.Popen(
        [node_cmd, "src/index.js"],
        cwd=SERVER_DIR,
        shell=False
    )

    # 2. Start Vite frontend
    print(">>> [2/3] Starting Vite Frontend on port 5173...")
    frontend_proc = subprocess.Popen(
        [npm_cmd, "run", "dev"],
        cwd=FRONTEND_DIR,
        shell=False
    )

    # 3. Give servers a moment to bind and open browser
    time.sleep(2)
    print(">>> [3/3] Opening browser at http://localhost:5173 ...")
    webbrowser.open("http://localhost:5173")

    print("\n[OK] DoctorKavach prototype is live! Press Ctrl+C in this console to stop.\n")

    try:
        while True:
            time.sleep(1)
            if backend_proc.poll() is not None:
                print("Backend stopped with code:", backend_proc.poll())
                break
            if frontend_proc.poll() is not None:
                print("Frontend stopped with code:", frontend_proc.poll())
                break
    except KeyboardInterrupt:
        print("\nShutting down DoctorKavach servers gracefully...")
    finally:
        try:
            backend_proc.terminate()
            backend_proc.wait(timeout=3)
        except Exception:
            backend_proc.kill()

        try:
            frontend_proc.terminate()
            frontend_proc.wait(timeout=3)
        except Exception:
            frontend_proc.kill()
        print("DoctorKavach shutdown complete.")

if __name__ == "__main__":
    main()
