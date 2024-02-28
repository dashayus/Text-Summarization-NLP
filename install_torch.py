import subprocess

def install_torch():
    try:
        subprocess.run(["pip", "install", "torch==2.2.1"])
        print("torch package installed successfully.")
    except subprocess.CalledProcessError as e:
        print("Error occurred while installing torch package:", e)
    except Exception as e:
        print("An unexpected error occurred:", e)

if __name__ == "__main__":
    install_torch()
