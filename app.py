
import streamlit as st
import pickle
import numpy as np
from streamlit_option_menu import option_menu

# import the model
pipe_l = pickle.load(open('pipe_rf.pkl', 'rb'))
df_l = pickle.load(open('df.pkl', 'rb'))
df_m = pickle.load(open('df_mobile.pkl', 'rb'))
pipe_m = pickle.load(open('pipe_rf_mobile.pkl', 'rb'))
df_t = pickle.load(open('df_TV.pkl', 'rb'))
pipe_t = pickle.load(open('pipe_rf_TV.pkl', 'rb'))
df_s = pickle.load(open('df_smart_watch.pkl', 'rb'))
pipe_s = pickle.load(open('pipe_rf_smart_watch.pkl', 'rb'))

st.title("Price Predictor")

with st.sidebar:
    item = option_menu('Products',
                       ['Laptop', 'Mobile', 'TV', 'Smart Watch'],)
if item == "Laptop":
    st.title("Laptops")
    brand = st.selectbox('Brand', df_l['Brand'].unique())
    processor = st.selectbox('Processor', df_l['Processor'].unique())

    os = st.selectbox('OS', df_l['Operating System'].unique())
    storage = st.selectbox('storage(in GB)', [0, 128, 256, 512, 1024, 2048, 3072])

    ram = st.selectbox('RAM(in GB)', [2, 4, 6, 8, 12, 16, 24, 32, 64])

    # screen size
    screen_size = st.number_input('Screen Size')
    # Touchscreen
    touchscreen = st.selectbox('Touchscreen', ['No', 'Yes'])

    if st.button('Predict Price'):
        # query

        query = np.array([brand, processor, os, storage, ram, screen_size, touchscreen])

        query = query.reshape(1, 7)

        predicted_price = np.exp(pipe_l.predict(query)[0])

        st.title("The predicted price of this configuration is " + str(int(predicted_price)))

elif item == "Mobile":
    st.title("Mobiles")

    brand = st.selectbox('Brand', df_m['Brand'].unique())
    processor = st.selectbox('Processor', df_m['Processor'].unique())

    os = st.selectbox('OS', df_m['Operating System'].unique())
    storage = st.selectbox('storage(in GB)', [0, 32, 64, 128, 256, 512, 1024])

    ram = st.selectbox('RAM(in GB)', [2, 4, 6, 8, 12, 16, 24, 32, 64])
    display_size = st.number_input('Display Size (in cm)')
    front_camera = st.number_input('Front camera(in MP)')
    network = st.number_input('Connectivity (in G)')
    battery = st.number_input('Battery (in mAh)')
    camera1 = st.number_input('Camera (in MP)')
    camera2 = st.number_input('Camera 2 (in MP)')
    camera3 = st.number_input('Camera  3 (in MP)')
    camera4 = st.number_input('Camera 4 (in MP)')
    if st.button('Predict Price'):
        # query

        query = np.array([brand, display_size, os, processor, storage, ram, front_camera, network, battery, camera1, camera2, camera3, camera4])

        query = query.reshape(1, 13)

        predicted_price = np.exp(pipe_m.predict(query)[0])

        st.title("The predicted price of this configuration is " + str(int(predicted_price)))

elif item == "TV":
    st.title("TVs")
    brand = st.selectbox('Brand', df_t['Brand'].unique())
    display_size = st.number_input('Display Size (in cm)')
    os = st.selectbox('OS', df_t['Operating System'].unique())
    smart_tv = st.selectbox('Smart TV', ['Yes', 'No'])
    refresh_rate = st.selectbox('Refresh rate', df_t['Refresh Rate'].unique())
    screen_type = st.selectbox('Screen Type', df_t['Screen Type'].unique())
    resolution = st.selectbox('Screen Resolution',
                              ['1920x1080', '1366x768', '1600x900', '3840x2160', '3200x1800', '2880x1800', '2560x1600',
                               '2560x1440', '2304x1440'])
    hdmi = st.number_input('HDMI (no of slots)')
    usb = st.number_input('USB (no of slots)')
    if st.button('Predict Price'):

        if smart_tv == 'Yes':
            smart_tv = 1
        else:
            smart_tv = 0

        X_res = int(resolution.split('x')[0])
        Y_res = int(resolution.split('x')[1])

        query = np.array([brand, display_size, os, smart_tv, refresh_rate, screen_type, X_res, Y_res, hdmi, usb])

        query = query.reshape(1, 10)
        st.title("The predicted price of this configuration is " + str(int(np.exp(pipe_t.predict(query)[0]))))
else:
    st.title("Smart Watch")
    brand = st.selectbox('Brand', df_s['Brand'].unique())
    display_size = st.number_input('Display Size (in mm)')
    os = st.selectbox('OS', df_s['Operating System'].unique())
    call_fun = st.selectbox('Call function', ['Yes', 'No'])
    bluetooth = st.selectbox('Bluetooth', ['Yes', 'No'])
    wifi = st.selectbox('Wifi', ['Yes', 'No'])
    GPS = st.selectbox('GPS', ['Yes', 'No'])
    display_type = st.selectbox('Display Type', df_s['Display_Type'].unique())
    display_resol = st.number_input('Display Resolution (100-300)')
    touch_screen = st.selectbox('Touch Screen', ['Yes', 'No'])
    battery = st.number_input('Battery Life (in days)')
    if st.button('Predict Price'):
        if call_fun == 'Yes':
            call_fun = 1
        else:
            call_fun = 0
        if bluetooth == 'Yes':
            bluetooth = 1
        else:
            bluetooth = 0
        if wifi == 'Yes':
            wifi = 1
        else:
            wifi = 0
        if GPS == 'Yes':
            GPS = 1
        else:
            GPS = 0
        if touch_screen == 'Yes':
            touch_screen = 1
        else:
            touch_screen = 0
        query = np.array([brand, display_size, os, call_fun, bluetooth, wifi, GPS, display_type, display_resol, touch_screen, battery])

        query = query.reshape(1, 11)
        st.title("The predicted price of this configuration is " + str(int(np.exp(pipe_s.predict(query)[0]))))