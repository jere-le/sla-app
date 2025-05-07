import streamlit as st

st.title("Azure SLA -laskuri")

# Lue palvelutiedot tiedostosta
def load_slas(filename="azure_sla_reference.txt"):
    services = {}
    try:
        with open(filename, "r") as f:
            for line in f:
                if ":" in line:
                    name, value = line.strip().split(":")
                    services[f"{name.strip()} ({float(value)*100:.3f}%)"] = float(value)
    except FileNotFoundError:
        st.error(f"Tiedostoa {filename} ei löydy.")
    return services

services = load_slas()

# Käyttäjä valitsee palvelut
selected = st.multiselect("Valitse käytössä olevat Azure-palvelut:", list(services.keys()))

# Lasketaan yhdistetty SLA
if selected:
    combined_sla = 1.0
    for service in selected:
        combined_sla *= services[service]

    downtime_minutes_per_month = (1 - combined_sla) * 30 * 24 * 60

    st.metric("Yhdistetty SLA", f"{combined_sla * 100:.5f} %")
    st.caption(f"Arvioitu kuukausittainen katko: {downtime_minutes_per_month:.2f} minuuttia")
else:
    st.info("Valitse vähintään yksi palvelu ylhäältä.")
