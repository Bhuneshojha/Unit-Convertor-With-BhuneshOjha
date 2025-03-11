
import streamlit as st

st.markdown(
    """
    <style>
    body {
        background-color: rgb(154, 138, 183);
        color: white;
    }
    .stApp {
        background: linear-gradient(to right, #56CCF2, rgb(252, 183, 148));
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 0 10px 30px rgba(0, 0, 0, 0.2);
    }
    h1 {
        text-align: center;
        color: white;
        font-size: 30px;
    }
    .stButton>button {
        background: linear-gradient(to right, rgb(253, 177, 177), rgb(175, 245, 247));
        padding: 10px 20px;
        font-size: 18px;
        border-radius: 12px;
        transition: background-color 0.3s ease;
        box-shadow: 0 4px 14px rgba(65, 113, 67, 0.8);
    }
    .stButton>button:hover {
        transform: scale(1.05);
        background: linear-gradient(45deg, rgb(176, 185, 212), rgb(184, 162, 162));
        color: black;
    }
    .result-box {
        font-size: 20px;
        font-weight: bold;
        padding: 25px;
        text-align: center;
        margin-top: 20px;
        border-radius: 8px;
        background: rgba(69, 67, 67, 0.1);
        box-shadow: 0 2px 10px rgba(19, 19, 59, 0.3);
    }
    .footer {
        text-align: center;
        margin-top: 20px;
        color: black;
        font-size: 17px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown("<h1>🌌 Unit Converter</h1>", unsafe_allow_html=True)
st.write("Easily convert between different units of measurement (Length, Weight, and Temperature)")

# Sidebar Menu
conversion_type = st.sidebar.selectbox("Select Conversion Type", ["Length", "Weight", "Temperature"])

# Input field for value
value = st.number_input("Enter the Value", value=0.0, min_value=0.0, step=0.1)

col1, col2 = st.columns(2)

if conversion_type == "Length":
    with col1:
        from_unit = st.selectbox("From Unit", ["Meter", "Kilometer", "Centimeter", "Millimeter", "Miles", "Yards", "Feet", "Inches"])
    with col2:
        to_unit = st.selectbox("To Unit", ["Meter", "Kilometer", "Centimeter", "Millimeter", "Miles", "Yards", "Feet", "Inches"])

elif conversion_type == "Weight":
    with col1:
        from_unit = st.selectbox("From Unit", ["Kilogram", "Gram", "Milligram", "Pounds", "Ounce"])
    with col2:
        to_unit = st.selectbox("To Unit", ["Kilogram", "Gram", "Milligram", "Pounds", "Ounce"])

elif conversion_type == "Temperature":
    with col1:
        from_unit = st.selectbox("From Unit", ["Celsius", "Fahrenheit", "Kelvin"])
    with col2:
        to_unit = st.selectbox("To Unit", ["Celsius", "Fahrenheit", "Kelvin"])

# Conversion Functions
def length_converter(value, from_unit, to_unit):
    length_units = {
        "Meter": 1, "Kilometer": 0.001, "Centimeter": 100, "Millimeter": 1000,
        "Miles": 0.000621371, "Yards": 1.09361, "Feet": 3.28084, "Inches": 39.3701
    }
    return (value / length_units[from_unit]) * length_units[to_unit]

def weight_converter(value, from_unit, to_unit):
    weight_units = {
        "Kilogram": 1, "Gram": 1000, "Milligram": 1000000, "Pounds": 2.20462, "Ounce": 35.274  
    }
    return (value / weight_units[from_unit]) * weight_units[to_unit]

def temp_converter(value, from_unit, to_unit):
    if from_unit == "Celsius": 
        return (value * 9/5 + 32) if to_unit == "Fahrenheit" else (value + 273.15) if to_unit == "Kelvin" else value
    elif from_unit == "Fahrenheit": 
        return ((value - 32) * 5/9) if to_unit == "Celsius" else ((value - 32) * 5/9 + 273.15) if to_unit == "Kelvin" else value
    elif from_unit == "Kelvin":
        return (value - 273.15) if to_unit == "Celsius" else ((value - 273.15) * 9/5 + 32) if to_unit == "Fahrenheit" else value
    return value

# Initialize result variable
result = 0.0

if st.button("Convert 🔄"):
    if conversion_type == "Length":
        result = length_converter(value, from_unit, to_unit)
    elif conversion_type == "Weight": 
        result = weight_converter(value, from_unit, to_unit)
    elif conversion_type == "Temperature":
        result = temp_converter(value, from_unit, to_unit)

    st.markdown(f"<div class='result-box'>{value} {from_unit} = {result:.4f} {to_unit}</div>", unsafe_allow_html=True)

st.markdown("<div class='footer'>Developed by Bhunesh Ojha 🖥️✨</div>", unsafe_allow_html=True)