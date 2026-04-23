import streamlit as st

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
    </style>
    """, unsafe_allow_index=True)

st.title("🏛️ DC Heroes Database")
st.write("Welcome to the Justice League archive. Select a hero to view their dossier.")

dc_heroes = {
    "Batman (Bruce Wayne)": {
        "powers": "Intelligence, detective skills, master martial artist",
        "city": "Gotham City",
        "first_appearance": "Detective Comics #27 (1939)",
        "color": "#2c3e50",
        "icon": "🦇"
    },
    "Superman (Clark Kent)": {
        "powers": "Flight, super strength, heat vision",
        "city": "Metropolis",
        "first_appearance": "Action Comics #1 (1938)",
        "color": "#e74c3c",
        "icon": "🦸‍♂️"
    },
    "Wonder Woman (Diana)": {
        "powers": "Divine strength, Lasso of Truth",
        "city": "Themyscira",
        "first_appearance": "All Star Comics #8 (1941)",
        "color": "#f1c40f",
        "icon": "🛡️"
    },
    "The Flash (Barry Allen)": {
        "powers": "Superhuman speed",
        "city": "Central City",
        "first_appearance": "Showcase #4 (1956)",
        "color": "#d35400",
        "icon": "⚡"
    }
}

st.sidebar.header("Filters")
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
            """, unsafe_allow_index=True)

st.divider()
st.caption("Application developed for the deployment lab.")