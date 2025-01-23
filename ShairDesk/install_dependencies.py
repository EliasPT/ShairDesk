import subprocess
import sys

# Die zu installierenden Pakete
packages = [
    "blinker==1.9.0",
    "click==8.1.8",
    "colorama==0.4.6",
    "Flask==3.1.0",
    "Flask-Login==0.6.3",
    "Flask-WTF==1.2.2",
    "itsdangerous==2.2.0",
    "Jinja2==3.1.5",
    "MarkupSafe==3.0.2",
    "Werkzeug==3.1.3",
    "WTForms==3.2.1"
]

# Funktion zum Installieren der Pakete
def install_packages(packages):
    for package in packages:
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])

if __name__ == "__main__":
    install_packages(packages)
