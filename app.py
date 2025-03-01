import streamlit as st
from pint import UnitRegistry

# Initialize the Unit Registry
ureg = UnitRegistry()

# Set page layout
st.set_page_config(page_title="Unit Converter", page_icon="🔄")

# Title and subtitle
st.title("🔄 Unit Converter")
st.markdown("Convert units across **Length**, **Weight**, **Area**, **Volume**, **Speed**, **Time**, and **Temperature** categories.")

# Define unit categories and units
categories = {
    "Length": ["meter", "kilometer", "centimeter", "millimeter", "mile", "yard", "foot", "inch", "nanometer"],
    "Weight": ["gram", "kilogram", "milligram", "pound", "ounce", "stone"],
    "Area": ["square meter", "square kilometer", "hectare", "acre", "square mile", "square foot", "square yard"],
    "Volume": ["liter", "milliliter", "cubic meter", "cubic centimeter", "gallon", "quart", "pint", "cup"],
    "Speed": ["meter/second", "kilometer/hour", "mile/hour", "knot"],
    "Time": ["second", "minute", "hour", "day", "week", "year"],
    "Temperature": ["celsius", "fahrenheit", "kelvin"],
}

# Sidebar for category selection
category = st.sidebar.selectbox("Select a category:", list(categories.keys()))

# Get units for the selected category
units = categories[category]

# Input section
st.header(f"Convert {category}")
col1, col2, col3 = st.columns([1, 1, 1])

with col1:
    value = st.number_input("Enter value:", value=0.0, step=1.0)
with col2:
    from_unit = st.selectbox("From unit:", units)
with col3:
    to_unit = st.selectbox("To unit:", units)

# Conversion button and result
if st.button("Convert"):
    try:
        from_quantity = value * ureg(from_unit)
        result = from_quantity.to(to_unit).magnitude
        st.success(f"{value} {from_unit} = {result:.4f} {to_unit}")
    except Exception as e:
        st.error(f"Conversion error: {e}")

# Footer
st.markdown("---")
st.caption("Made with ❤️ using Streamlit.")
