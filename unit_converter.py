import streamlit as st

st.set_page_config(page_title="Unit Converter", page_icon="🔁", layout="centered")

st.markdown("<h1 style='text-align: center; color: #4CAF50;'>🔁 Unit Converter</h1>", unsafe_allow_html=True)

def convert_units(value, unit_from, unit_to):
    conversions = {
        "meters_kilometers": 0.001,
        "kilometers_meters": 1000,
        "grams_kilograms": 0.001,
        "kilograms_grams": 1000,
    }

    key = f"{unit_from}_{unit_to}"
    if key in conversions:
        return value * conversions[key]
    elif unit_from == unit_to:
        return value
    else:
        return None

st.write("### Enter the value and select the units you want to convert:")

value = st.number_input("🔢 Enter the Value:", min_value=0.0, format="%.2f")

unit_from = st.selectbox("Convert from:", ["meters", "kilometers", "grams", "kilograms"])
unit_to = st.selectbox("Convert to:", ["meters", "kilometers", "grams", "kilograms"])

if st.button("Convert"):
    result = convert_units(value, unit_from, unit_to)
    if result is not None:
        st.success(f"✅ Converted Value: **{result:.4f} {unit_to}**")
    else:
        st.error("❌ Conversion not available between selected units.")
