import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="DC Heroes Catalog",
    page_icon="🦇",
    layout="wide"
)

st.markdown("""
    <style>
    .hero-card {
        background-color: #1e1e1e;
        padding: 20px;
        border-radius: 10px;
        border-left: 5px solid #0078ff;
        margin-bottom: 20px;
    }
    .stMetric {
        background-color: #262730;
        padding: 10px;
        border-radius: 5px;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🏛️ DC Heroes Database")
st.write("Welcome to the Justice League archive. Select a hero to view their dossier.")

dc_heroes = {
    "Batman (Bruce Wayne)": {
        "powers": "Intelligence, detective skills, master martial artist",
        "city": "Gotham City",
        "first_appearance": "1939",
        "power_level": 85,
        "icon": "🦇"
    },
    "Superman (Clark Kent)": {
        "powers": "Flight, super strength, heat vision",
        "city": "Metropolis",
        "first_appearance": "1938",
        "power_level": 100,
        "icon": "🦸‍♂️"
    },
    "Wonder Woman (Diana)": {
        "powers": "Divine strength, Lasso of Truth",
        "city": "Themyscira",
        "first_appearance": "1941",
        "power_level": 95,
        "icon": "🛡️"
    },
    "The Flash (Barry Allen)": {
        "powers": "Superhuman speed",
        "city": "Central City",
        "first_appearance": "1956",
        "power_level": 90,
        "icon": "⚡"
    }
}

st.sidebar.header("Navigation")
page = st.sidebar.radio("Go to", ["Hero Catalog", "Power Analysis", "Request Hero"])

if page == "Hero Catalog":
    search_query = st.sidebar.text_input("Search Hero", "")
    for name, info in dc_heroes.items():
        if search_query.lower() in name.lower():
            with st.container():
                st.markdown(f"""
                <div class="hero-card">
                    <h2>{info['icon']} {name}</h2>
                    <p><b>Powers:</b> {info['powers']}</p>
                    <p><b>Home City:</b> {info['city']}</p>
                    <p><b>First Appearance:</b> {info['first_appearance']}</p>
                </div>
                """, unsafe_allow_html=True)

elif page == "Power Analysis":
    st.subheader("📊 Hero Power Level Comparison")
    df = pd.DataFrame([
        {"Hero": name, "Power Level": info["power_level"]} 
        for name, info in dc_heroes.items()
    ])
    st.bar_chart(df.set_index("Hero"))
    st.write("This chart represents a comparative analysis of hero capabilities based on Justice League archives.")

elif page == "Request Hero":
    st.subheader("📩 Request New Hero Dossier")
    with st.form("hero_request"):
        hero_name = st.text_input("Hero Name")
        reason = st.text_area("Why should we add this hero?")
        submitted = st.form_submit_button("Submit Request")
        if submitted:
            if hero_name:
                st.success(f"Request for {hero_name} has been sent to the Watchtower.")
            else:
                st.error("Please enter a hero name.")

st.divider()
st.caption("Phase 2: Added Visualization, Navigation, and Interactive Forms.")