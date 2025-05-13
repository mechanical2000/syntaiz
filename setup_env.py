import platform
import subprocess
import sys

def install_requirements():
    try:
        print("Installing Python dependencies from requirements.txt...")
        subprocess.run([sys.executable, "-m", "pip", "install", "--upgrade", "pip"], check=True)
        subprocess.run([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"], check=True)
    except subprocess.CalledProcessError:
        print("⚠️ Error installing dependencies via pip.")
        sys.exit(1)

def install_sentencepiece_mac_arm():
    try:
        print("Detected Mac ARM (M1/M2) → Installing sentencepiece via Homebrew (safe path).")
        subprocess.run(["brew", "install", "sentencepiece"], check=True)
    except subprocess.CalledProcessError:
        print("⚠️ Error installing sentencepiece via Homebrew.")
        sys.exit(1)

def main():
    system = platform.system()
    machine = platform.machine()

    print(f"Detected system: {system}, architecture: {machine}")

    if system == "Darwin" and machine == "arm64":
        install_sentencepiece_mac_arm()
        install_requirements()
        print("✅ Setup completed for Mac ARM (Homebrew + pip).")
    else:
        install_requirements()
        print("✅ Setup completed for Linux/AMD64 or compatible (pip only).")

if __name__ == "__main__":
    main()
