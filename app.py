import streamlit as st

st.set_page_config(page_title="MSTY Tracker", layout="wide")
st.title("📊 MSTY Tracker App – All-in-One")

tabs = st.tabs([
    "📊 Compounding Simulator",
    "📈 Market Monitoring",
    "📐 Cost Basis Tools",
    "🛡️ Hedging Tools",
    "📤 Export Center"
])

with tabs[0]:
    exec(open("projection_tool.py").read(), globals())

with tabs[1]:
    exec(open("market_monitoring_tab.py").read(), globals())

with tabs[2]:
    exec(open("cost_basis_tab.py").read(), globals())

with tabs[3]:
    exec(open("hedging_tools_tab.py").read(), globals())

with tabs[4]:
    exec(open("export_center_tab.py").read(), globals())