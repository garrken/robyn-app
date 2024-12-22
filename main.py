import os
import sys
import subprocess
import streamlit as st

# Klona Robyn-repositoryt om det inte redan finns
robyn_code_path = os.path.join(os.getcwd(), "robyn_code")
if not os.path.exists(robyn_code_path):
    st.info("Cloning Robyn repository...")
    try:
        subprocess.run(
            ["git", "clone", "--depth", "1", "--filter=blob:none", "--sparse", "https://github.com/facebookexperimental/Robyn.git", "robyn_code"],
            check=True,
        )
        subprocess.run(["git", "-C", "robyn_code", "sparse-checkout", "set", "python"], check=True)
        st.success("Successfully cloned Robyn repository.")
    except subprocess.CalledProcessError as e:
        st.error(f"Failed to clone Robyn repository: {e}")
        st.stop()

# Kontrollera om requirements.txt finns
requirements_file = os.path.join(robyn_code_path, "python", "requirements.txt")
if not os.path.exists(requirements_file):
    st.error("requirements.txt not found in robyn_code/python folder.")
    st.stop()

# Lägg till robyn_code/python till sys.path
python_path = os.path.join(robyn_code_path, "python")
if python_path not in sys.path:
    sys.path.append(python_path)

# Installera beroenden
try:
    st.info("Installing dependencies...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", requirements_file])
    st.success("Dependencies installed successfully.")
except subprocess.CalledProcessError as e:
    st.error(f"Dependency installation failed: {e}")
    st.stop()

# Importera Robyn
try:
    from robyn.robyn import Robyn
    st.success("Successfully imported Robyn.")
except ImportError as e:
    st.error(f"Failed to import Robyn: {e}")
    st.stop()

st.title("Robyn SaaS - Marketing Mix Modeling")

# Exempel på användning av Robyn
if 'robyn_instance' not in st.session_state:
    working_dir = "./robyn_work
