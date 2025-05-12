import streamlit as st

# Title and description
st.title("LLM Agent Risk Scoring & Actionability Demo")
st.markdown("Simulate agent-to-action interactions and dynamically assess risk and trust scores.")

# Agent and Action selection
agent = st.selectbox("Select Agent", ["Agent 1", "Agent 2"])
action = st.selectbox("Select Action", ["Refund $5000", "Update HR Record", "Access Financial Report"])

# User-defined thresholds
st.sidebar.header("Policy Thresholds")
trust_threshold = st.sidebar.slider("Minimum Trust Score to Proceed", 0, 5, 3)
risk_threshold = st.sidebar.slider("Maximum Action Risk Score to Proceed", 0, 5, 3)

# Simulated scoring logic (could be replaced by real model or API)
action_risk_scores = {
    "Refund $5000": 4,
    "Update HR Record": 3,
    "Access Financial Report": 2,
}
agent_trust_scores = {
    "Agent 1": 4,
    "Agent 2": 2,
}

# Show scores
risk_score = action_risk_scores[action]
trust_score = agent_trust_scores[agent]

st.metric("Action Risk Score", risk_score)
st.metric("Agent Trust Score", trust_score)

# Decision Logic
if trust_score >= trust_threshold and risk_score <= risk_threshold:
    st.success("✅ Action Allowed")
else:
    st.error("❌ Action Flagged or Blocked")

# Explanation
with st.expander("Explanation"):
    st.write(f"**{agent}** tried to perform **{action}**.")
    st.write(f"Action Risk Score is **{risk_score}**, Trust Score is **{trust_score}**.")
    st.write(f"Policy allows action if Trust Score ≥ {trust_threshold} and Risk Score ≤ {risk_threshold}.")
