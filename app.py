
App · PY
"""
app.py
------
Entry point for the Healthcare Operations Intelligence dashboard.
 
Sets the page up and builds the navigation. Every chart and every
calculation lives in the dashboards and src folders, so this file
stays small.
 
Run with:  streamlit run app.py
"""
 
from pathlib import Path
 
import streamlit as st
 
 
st.set_page_config(
    page_title="Healthcare Operations Intelligence",
    page_icon="🩺",
    layout="wide",
    initial_sidebar_state="expanded",
)
 
 
# Every .py file in the dashboards folder becomes a page. The number at
# the front of the file name sets the order and is removed from the
# label, so 4_Health_Programs_Population_Vulnerability.py is shown as
# "Health Programs Population Vulnerability".
 
DASHBOARD_DIR = Path(__file__).parent / "dashboards"
 
 
def page_title(file_path):
    """Turn 4_Health_Programs.py into 'Health Programs'."""
 
    name = file_path.stem
 
    if "_" in name and name.split("_")[0].isdigit():
        name = name.split("_", 1)[1]
 
    return name.replace("_", " ")
 
 
dashboard_files = sorted(
    f for f in DASHBOARD_DIR.glob("*.py")
    if not f.name.startswith("_")
)
 
 
if not dashboard_files:
    st.error("No dashboards were found in the dashboards folder.")
    st.stop()
 
 
pages = [
    st.Page(str(f), title=page_title(f), icon="🩺")
    for f in dashboard_files
]
 
 
navigation = st.navigation(pages, position="sidebar")
 
navigation.run()
 
