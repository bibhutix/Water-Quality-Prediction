import stqdm
import pickle
import pandas as pd
from PIL import Image
from time import sleep
import streamlit as st
from stqdm import stqdm
from streamlit_option_menu import option_menu


@st.cache_resource
def load_model():
    with open('assets/model.pkl', 'rb') as f:
        return pickle.load(f)


st.set_page_config(page_title="Omdena Rwanda", page_icon="🇷🇼", initial_sidebar_state="expanded")

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)
css_style = {
    "icon": {"color": "white"},
    "nav-link": {"--hover-color": "grey"},
    "nav-link-selected": {"background-color": "#FF4C1B"},
}



def home_page():
    st.write(f"""# Water Inspection System""", unsafe_allow_html=True)

    st.write(f"""<h2>The Problem</h2>   
    <p>Access to clean water is a critical challenge in many parts of the world, 
    including Rwanda. Water quality prediction is important for ensuring the availability of safe and clean water for 
    drinking, agriculture, and other purposes. However, traditional methods for water quality prediction are often 
    time-consuming and costly, and they may not provide accurate and timely information.This project focuses to develop an automated water quality prediction system using 
    machine learning.</p> """, unsafe_allow_html=True)





def model_section():
    st.write("""<h1>Predict Water Quality</h1>
    <p>Enter these values of the parameters to know if the water quality is suitable to drink or not.</p><hr>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3, gap="large")
    with col1:
        ColourTCU = st.number_input(label="Colour (TCU)", min_value=0.0, max_value=1000.0, step=50.0, format="%f",
                                    key="test_slider0")
        TurbidityNTU = st.number_input(label="Turbidity (NTU)", min_value=0.0, max_value=1000.0, step=50.0, format="%f",
                                       key="test_slider1")
        pH = st.number_input(label="pH", min_value=0.0, max_value=1000.0, step=50.0, format="%f", key="test_slider2")
        ConductivityuS = st.number_input(label="Conductivity (uS/cm)", min_value=0.0, max_value=1000.0, step=50.0,
                                         format="%f", key="test_slider3")
        TotalDissolvedSolids = st.number_input(label="Total Dissolved Solids (mg/l)", min_value=0.0, max_value=1000.0,
                                               step=50.0, format="%f", key="test_slider4")
        TotalHardness = st.number_input(label="Total Hardness (mg/l as CaCO3)", min_value=0.0, max_value=1000.0,
                                        step=50.0, format="%f", key="test_slider5")

    with col2:
        Aluminium = st.number_input(label="Aluminium (mg/l)", min_value=0.0, max_value=1000.0, step=50.0, format="%f",
                                    key="test_slider6")
        Chloride = st.number_input(label="Chloride (mg/l)", min_value=0.0, max_value=1000.0, step=50.0, format="%f",
                                   key="test_slider7")
        Iron = st.number_input(label="Iron (mg/l)", min_value=0.0, max_value=1000.0, step=50.0, format="%f",
                               key="test_slider8")
        Sodium = st.number_input(label="Sodium (mg/l)", min_value=0.0, max_value=1000.0, step=50.0, format="%f",
                                 key="test_slider9")
        Sulphate = st.number_input(label="Sulphate (mg/l)", min_value=0.0, max_value=1000.0, step=50.0, format="%f",
                                   key="test_slider10")
        Zinc = st.number_input(label="Zinc (mg/l)", min_value=0.0, max_value=1000.0, step=50.0, format="%f",
                               key="test_slider11")

    with col3:
        Magnesium = st.number_input(label="Magnesium (mg/l)", min_value=0.0, max_value=1000.0, step=50.0, format="%f",
                                    key="test_slider12")
        Calcium = st.number_input(label="Calcium (mg/l)", min_value=0.0, max_value=1000.0, step=50.0, format="%f",
                                  key="test_slider13")
        Potassium = st.number_input(label="Potassium (mg/l)", min_value=0.0, max_value=1000.0, step=50.0, format="%f",
                                    key="test_slider14")
        Nitrate = st.number_input(label="Nitrate (mg/l)", min_value=0.0, max_value=1000.0, step=50.0, format="%f",
                                  key="test_slider15")
        Phosphate = st.number_input(label="Phosphate (mg/l)", min_value=0.0, max_value=1000.0, step=50.0, format="%f",
                                    key="test_slider16")
        st.write("<br>", unsafe_allow_html=True)
        predict_button = st.button('  Predict Water Quality  ')

    dataframe = pd.DataFrame({'Colour (TCU)': [ColourTCU], 'Turbidity (NTU)': [TurbidityNTU], 'pH': [pH],
                              'Conductivity (uS/cm)': [ConductivityuS],
                              'Total Dissolved Solids (mg/l)': [TotalDissolvedSolids],
                              'Total Hardness (mg/l as CaCO3)': [TotalHardness], 'Aluminium (mg/l)': [Aluminium],
                              'Chloride (mg/l)': [Chloride], 'Total Iron (mg/l)': [Iron],
                              'Sodium (mg/l)': [Sodium], 'Sulphate (mg/l)': [Sulphate], 'Zinc (mg/l)': [Zinc],
                              'Magnesium (mg/l)': [Magnesium], 'Calcium (mg/l)': [Calcium],
                              'Potassium (mg/l)': [Potassium], 'Nitrate (mg/l)': [Nitrate],
                              'Phosphate (mg/l)': [Phosphate]})

    if predict_button:
        model = load_model()
        result = model.predict(dataframe)
        for _ in stqdm(range(50)):
            sleep(0.015)
        if result[0] == 1.0:
            st.error("This Water Quality is Non-Potable")
        else:
            st.success('This Water Quality is Potable')




with st.sidebar:
    selected = option_menu(
        menu_title=None,
        options=["Home", "Check Water Quality", "About", ],
        icons=["house", "droplet", "info-circle"],
        styles=css_style
    )

if selected == "Home":
    home_page()

elif selected == "Check Water Quality":
    model_section()



