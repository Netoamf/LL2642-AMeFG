import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import os
from scipy.stats import pearsonr, spearmanr

# Set page config
st.set_page_config(
    page_title="Linguistic Acquisition Dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Custom CSS for aesthetics
st.markdown("""
<style>
    .main {
        background-color: #f8f9fa;
    }
    .stMetric {
        background-color: #ffffff;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    [data-testid="stMetricLabel"] {
        color: black !important;
        font-weight: bold !important;
        font-size: 1.1rem !important;
    }
    [data-testid="stMetricValue"] {
        color: black !important;
        font-weight: bold !important;
    }
    h1, h2, h3 {
        color: #1f77b4;
    }
</style>
""", unsafe_allow_html=True)

# Function to load data
@st.cache_data
def load_data():
    path = os.path.join("corpus", "Corpora_Comparison_Stats", "combined_corpora_comparison_data.csv")
    if not os.path.exists(path):
        st.error(f"Data file not found at {path}. Please run the analysis notebook first.")
        return None
    df = pd.read_csv(path)
    return df

# Title and introduction
st.title("📊 Temporal Expression Acquisition Dashboard")
st.markdown("""
Explore the relationship between **Child Directed Speech (CDS)** and **Child Speech (CHI)** in Brazilian Portuguese and English.
This dashboard visualizes how children acquire time-related concepts through linguistic input.
""")

df = load_data()

if df is not None:
    # --- Sidebar Filters ---
    st.sidebar.header("🔍 Filters")
    
    languages = st.sidebar.multiselect(
        "Select Languages",
        options=df['corpus_language'].unique(),
        default=df['corpus_language'].unique()
    )
    
    filtered_df = df[df['corpus_language'].isin(languages)]
    
    children = st.sidebar.multiselect(
        "Select Children",
        options=sorted(filtered_df['child_name'].unique()),
        default=[]
    )
    
    if children:
        filtered_df = filtered_df[filtered_df['child_name'].isin(children)]
        
    age_range = st.sidebar.slider(
        "Age Range (Months)",
        min_value=float(df['child_age_months'].min()),
        max_value=float(df['child_age_months'].max()),
        value=(float(df['child_age_months'].min()), float(df['child_age_months'].max()))
    )
    
    filtered_df = filtered_df[
        (filtered_df['child_age_months'] >= age_range[0]) & 
        (filtered_df['child_age_months'] <= age_range[1])
    ]

    # --- KPI Metrics ---
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Total Sessions", len(filtered_df))
    with col2:
        avg_chi_freq = filtered_df['chi_deictic_freq_per_1k'].mean()
        st.metric("Avg CHI Freq", f"{avg_chi_freq:.2f}")
    with col3:
        avg_cds_freq = filtered_df['cds_deictic_freq_per_1k'].mean()
        st.metric("Avg CDS Freq", f"{avg_cds_freq:.2f}")
    with col4:
        total_words = filtered_df['chi_total_words'].sum() + filtered_df['cds_total_words'].sum()
        st.metric("Total Words Analyzed", f"{total_words:,}")

    # --- Main Content Tabs ---
    tab1, tab2, tab3 = st.tabs(["📈 Developmental Trajectories", "🔗 Input-Output Correlation", "🧠 Discussion & Stats"])

    with tab1:
        st.subheader("Frequency of Temporal Expressions over Age")
        fig_age = px.scatter(
            filtered_df,
            x='child_age_months',
            y='chi_deictic_freq_per_1k',
            color='corpus_language',
            size='chi_total_words',
            hover_data=['child_name', 'filename'],
            labels={
                'child_age_months': 'Age (Months)',
                'chi_deictic_freq_per_1k': 'CHI Frequency (per 1k words)',
                'corpus_language': 'Language'
            },
            template="plotly_white",
            trendline="ols"
        )
        st.plotly_chart(fig_age, use_container_width=True)
        st.info("**Discussion:** Usage frequency typically increases with age, reflecting the child's developing lexical and cognitive abstracting capabilities.")

    with tab2:
        st.subheader("Correlation: Parent Input (CDS) vs. Child Output (CHI)")
        fig_corr = px.scatter(
            filtered_df,
            x='cds_deictic_freq_per_1k',
            y='chi_deictic_freq_per_1k',
            color='corpus_language',
            size='child_age_months',
            hover_data=['child_name', 'filename'],
            labels={
                'cds_deictic_freq_per_1k': 'CDS Frequency (per 1k words)',
                'chi_deictic_freq_per_1k': 'CHI Frequency (per 1k words)',
                'corpus_language': 'Language'
            },
            template="plotly_white",
            trendline="ols"
        )
        # Add 1:1 reference line
        max_val = max(filtered_df['cds_deictic_freq_per_1k'].max(), filtered_df['chi_deictic_freq_per_1k'].max())
        fig_corr.add_shape(type="line", x0=0, y0=0, x1=max_val, y1=max_val, line=dict(color="Gray", dash="dashdot"))
        
        st.plotly_chart(fig_corr, use_container_width=True)
        st.info("**Discussion:** Data points clustered near the diagonal line (or following a similar slope) suggest that children's usage is closely mirrors the parents' input frequency.")

    with tab3:
        st.subheader("Statistical Tests Summary")
        
        if len(filtered_df) > 2:
            # Correlation Analysis
            c_cds_chi = filtered_df[['cds_deictic_freq_per_1k', 'chi_deictic_freq_per_1k']].dropna()
            r, p = pearsonr(c_cds_chi['cds_deictic_freq_per_1k'], c_cds_chi['chi_deictic_freq_per_1k'])
            rho, p_rho = spearmanr(c_cds_chi['cds_deictic_freq_per_1k'], c_cds_chi['chi_deictic_freq_per_1k'])

            s_col1, s_col2 = st.columns(2)
            with s_col1:
                st.write("**Pearson Correlation (Linear)**")
                st.code(f"r = {r:.3f}\np-value = {p:.4f}")
            with s_col2:
                st.write("**Spearman Correlation (Rank)**")
                st.code(f"rho = {rho:.3f}\np-value = {p_rho:.4f}")

            st.write("---")
            st.subheader("Discussion of Results")
            st.markdown(f"""
            - **Finding 1:** The Pearson correlation of **{r:.2f}** indicates a {'strong' if abs(r) > 0.6 else 'moderate' if abs(r) > 0.4 else 'weak'} relationship between parent input and child output.
            - **Finding 2:** Comparing across languages, we can observe if specific linguistic structures in **{', '.join(languages)}** facilitate or delay the acquisition of deictic markers.
            - **Conclusion:** Temporal acquisition is a social process. The frequency with which markers are used in the environmental input correlates significantly with the child's productive repertoire.
            """)
        else:
            st.warning("Not enough data points for statistical tests in the current selection.")

    # --- Footer ---
    st.markdown("---")
    st.caption("Dashboard developed for Data Analyst Portfolio. Data sourced from CHILDES Database.")
else:
    st.info("Please ensure the CSV data is generated by running the main Jupyter Notebook.")
