import streamlit as st
import requests
import time

API_URL = "http://127.0.0.1:8000/check-prompt"

st.set_page_config(
    page_title="Prompt Signal Scanner",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# ====== CUSTOM TERMINAL STYLE ======
st.markdown("""
<style>
body { background-color: #0e1117; }
.signal-box {
    border: 1px dashed #333;
    padding: 18px;
    border-radius: 10px;
    margin-top: 20px;
}
.signal-green { color: #00ff9c; }
.signal-yellow { color: #ffd166; }
.signal-red { color: #ff4b4b; }
.scan-bar {
    height: 6px;
    background: linear-gradient(90deg,#00ff9c,#ffd166,#ff4b4b);
    animation: scan 1.2s infinite;
}
@keyframes scan {
    0% {opacity:0.2;}
    50% {opacity:1;}
    100% {opacity:0.2;}
}
</style>
""", unsafe_allow_html=True)

# ====== HEADER ======
st.markdown("## 🛡️ AI Prompt Signal Scanner")
st.caption("Live firewall scan • No LLM • No cloud • 100% local")

st.markdown("<div class='scan-bar'></div>", unsafe_allow_html=True)

# ====== INPUT ======
prompt = st.text_area(
    "Signal Input",
    height=110,
    placeholder="Transmit a prompt signal...",
    label_visibility="collapsed"
)

scan = st.button("🔍 SCAN SIGNAL", use_container_width=True)

# ====== SCAN LOGIC ======
if scan:
    if not prompt.strip():
        st.warning("⚠️ No signal detected")
    else:
        with st.spinner("Intercepting signal..."):
            time.sleep(0.6)
            res = requests.post(API_URL, json={"prompt": prompt}).json()

        decision = res["decision"]
        score = res["risk_score"]
        reason = res["reason"]

        if decision == "allow":
            color = "signal-green"
            status = "GREEN SIGNAL"
            icon = "🟢"
        elif decision == "sanitize":
            color = "signal-yellow"
            status = "YELLOW SIGNAL"
            icon = "🟡"
        else:
            color = "signal-red"
            status = "RED SIGNAL"
            icon = "🔴"

        # ====== OUTPUT ======
        st.markdown(f"""
        <div class="signal-box">
            <h3 class="{color}">{icon} {status}</h3>
            <p><b>Threat Score:</b> {score}</p>
            <p><b>Firewall Reason:</b> {reason}</p>
        </div>
        """, unsafe_allow_html=True)

# ====== FOOTER ======
st.caption("⚡ Prompt Firewall • Signal-based Security UI")
