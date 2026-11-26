import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# --- 1. Page Configuration ---
st.set_page_config(page_title="Bihar Health PMU | Monitoring Dashboard", layout="wide")

# --- 2. Mock Data Generation (FIXED) ---
def load_data():
    districts = [
        "Patna", "Gaya", "Muzaffarpur", "Bhagalpur", "Darbhanga", 
        "Purnia", "Begusarai", "Katihar", "Nalanda", "Madhubani"
    ]
    
    data = {
        'District': districts,
        'ANC_Registration_Target': np.random.randint(5000, 15000, 10),
        'ANC_Registered_Actual': np.random.randint(4000, 14000, 10),
        'Immunization_Coverage_Pct': np.random.uniform(65.0, 95.0, 10),
        'Medicine_Stockout_Rate_Pct': np.random.uniform(2.0, 15.0, 10),
        'Data_Quality_Score': np.random.randint(60, 100, 10)
    }
    
    df = pd.DataFrame(data)
    
    # Calculate Gap
    df['Coverage_Gap'] = df['ANC_Registration_Target'] - df['ANC_Registered_Actual']
    
    # --- THE FIX: Create an Absolute Value column for Plotly Size ---
    # Plotly crashes if size is negative. This fixes it.
    df['Gap_Magnitude'] = df['Coverage_Gap'].abs()
    
    return df

df = load_data()

# --- 3. Sidebar ---
st.sidebar.title("🔍 PMU Filter Controls")
st.sidebar.info("Data Source: HMIS / ANMOL (Mock)")
selected_district = st.sidebar.multiselect(
    "Select District for Deep Dive:",
    options=df["District"].unique(),
    default=df["District"].unique()
)

if not selected_district:
    st.warning("Please select at least one district.")
    st.stop()

df_filtered = df[df["District"].isin(selected_district)]

# --- 4. Main Dashboard UI ---
st.title("🏥 SHSB: Key Performance Indicators (KPIs)")
st.markdown("### Real-time Monitoring of RMNCH+A Indicators")
st.markdown("---")

# Metrics
c1, c2, c3, c4 = st.columns(4)
c1.metric("Avg Immunization", f"{df_filtered['Immunization_Coverage_Pct'].mean():.1f}%", "1.2%")
c2.metric("Total ANC Gap", f"{df_filtered['Coverage_Gap'].sum():,}", "-500", delta_color="inverse")
c3.metric("Avg Stockout Rate", f"{df_filtered['Medicine_Stockout_Rate_Pct'].mean():.1f}%", "-0.5%")
c4.metric("Data Quality Score", f"{df_filtered['Data_Quality_Score'].mean():.0f}/100", "Stable")

st.markdown("---")

# --- 5. The Charts ---
col_left, col_right = st.columns(2)

with col_left:
    st.subheader("⚠️ The 'Delivery' Gap")
    st.caption("Target vs. Actual Registrations")
    fig_gap = px.bar(
        df_filtered, 
        x="District", 
        y=["ANC_Registration_Target", "ANC_Registered_Actual"],
        barmode='group',
        color_discrete_sequence=["#E0E0E0", "#FF4B4B"],
        title="Target vs Actual"
    )
    # Using 'use_container_width' to prevent warnings
    st.plotly_chart(fig_gap, use_container_width=True)

with col_right:
    st.subheader("📉 Correlation: Stockouts vs Coverage")
    st.caption("Larger Bubble = Larger Deviation from Target")
    
    # FIXED: Using 'Gap_Magnitude' (always positive) for size
    fig_scatter = px.scatter(
        df_filtered,
        x="Medicine_Stockout_Rate_Pct",
        y="Immunization_Coverage_Pct",
        size="Gap_Magnitude",  # <--- This was the crasher. Now fixed.
        color="District",
        title="Stockout Impact Analysis"
    )
    st.plotly_chart(fig_scatter, use_container_width=True)

# --- 6. Raw Data ---
with st.expander("📂 View Raw District Data (Forensic Audit View)"):
    st.dataframe(df_filtered)