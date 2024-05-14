import streamlit as st
from PIL import Image

# Set page config to customize layout and style
st.set_page_config(
    page_title='Forecasting System',
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS to improve aesthetics
st.markdown("""
<style>
.streamlit-container {
    margin-top: 50px;
}
h1, h2, h3, h4, h5 {
    color: White;
}
.sidebar .sidebar-content {
    background-color: lightgrey;
    color: black;
}
div.stButton > button:first-child {
    width: 100%;
}
div.row-widget.stRadio > div {
    flex-direction: row;
}
.metrics {
    text-align: center;
    color: #fff;
    background-color: #444;
    padding: 10px;
    border-radius: 10px;
    margin: 10px 0;
}
</style>
""", unsafe_allow_html=True)

# Initialize session state variables if not already present
if 'stage' not in st.session_state:
    st.session_state['stage'] = 'dataset_selection'

if 'dataset' not in st.session_state:
    st.session_state['dataset'] = None

if 'model_choice' not in st.session_state:
    st.session_state['model_choice'] = None

# Sidebar for navigation
with st.sidebar:
    st.title("Navigation")
    if st.button('Go to Dataset Selection'):
        st.session_state['stage'] = 'dataset_selection'
    if st.session_state['dataset'] and st.button('Go to Model Selection'):
        st.session_state['stage'] = 'model_selection'
    if st.session_state['model_choice'] and st.button('Show Results'):
        st.session_state['stage'] = 'results_display'

# Main area
if st.session_state['stage'] == 'dataset_selection':
    st.title("Welcome to the Forecasting System")
    dataset = st.selectbox("Select Dataset", ("S&P 500 Monthly Prices", "Hourly Energy Consumption", "Daily CO2 Concentrations"))
    if st.button('Select Dataset'):
        st.session_state['dataset'] = dataset
        st.session_state['stage'] = 'model_selection'

elif st.session_state['stage'] == 'model_selection':
    st.title(f"Model Selection for {st.session_state['dataset']}")
    model_choice = st.radio("Choose Model", ('ARIMA', 'ANN', 'Hybrid ARIMA-ANN', 'SARIMA', 'ETS', 'Prophet', 'SVR', 'LSTM'))
    if st.button('Select Model'):
        st.session_state['model_choice'] = model_choice
        st.session_state['stage'] = 'results_display'

elif st.session_state['stage'] == 'results_display':
    st.title(f"Results for {st.session_state['dataset']} using {st.session_state['model_choice']}")
    if st.session_state['dataset'] == "Hourly Energy Consumption":
        st.subheader("Model Performance Metrics")

        if st.session_state['model_choice'] == "ARIMA":
            col1, col2, col3 = st.columns(3)
            col1.metric("MAE", "0.182096")
            col2.metric("MSE", "0.052404")
            col3.metric("RMSE", "0.228921")

            st.subheader("Autocorrelation and ARIMA Forecast")
            col4, col5 = st.columns([1, 1])
            col4.image(Image.open('Energy/Arima/ACF.png'), caption='Autocorrelation', use_column_width=True)
            col5.image(Image.open('Energy/Arima/Arima.png'), caption='ARIMA Forecast', use_column_width=True)

        elif st.session_state['model_choice'] == "ANN":
            col1, col2, col3 = st.columns(3)
            col1.metric("MAE", "0.478458")
            col2.metric("MSE", "0.319195")
            col3.metric("RMSE", "0.564973")
            st.image(Image.open('Energy/Ann/ann.png'), caption='ANN Forecast', use_column_width=True)

        elif st.session_state['model_choice'] == "ETS":
            col1, col2 = st.columns(2)
            col1.metric("Mean Absolute Error", "0.092358")
            col2.metric("Mean Squared Error", "0.010632")
            st.image(Image.open('Energy/ETS/ets.png'), caption='ETS Forecast', use_column_width=True)

        elif st.session_state['model_choice'] == "Prophet":
            col1, col2 = st.columns(2)
            col1.metric("Mean Absolute Error", "0.218038")
            col2.metric("Mean Squared Error", "0.082359")
            st.image(Image.open('Energy/Prophet/prophet.png'), caption='Prophet Forecast', use_column_width=True)

        elif st.session_state['model_choice'] == "SVR":
            col1, col2 = st.columns(2)
            col1.metric("Mean Absolute Error", "0.819857")
            col2.metric("Mean Squared Error", "1.583158")
            st.image(Image.open('Energy/SVR/svr.png'), caption='SVR Forecast', use_column_width=True)

        elif st.session_state['model_choice'] == "LSTM":
            col1, col2 = st.columns(2)
            col1.metric("Mean Absolute Error", "0.111640")
            col2.metric("Mean Squared Error", "0.075964")
            st.image(Image.open('Energy/LSTM/lstm.png'), caption='LSTM Forecast', use_column_width=True)

        elif st.session_state['model_choice'] == "Hybrid ARIMA-ANN":
            col1, col2 = st.columns(2)
            col1.metric("Mean Absolute Error", "0.275526")
            col2.metric("Mean Squared Error", "0.150999")
            st.image(Image.open('Energy/Hybrid/hybrid.png'), caption='Hybrid ARIMA-ANN Forecast', use_column_width=True)

    elif st.session_state['dataset'] == "S&P 500 Monthly Prices":
        st.subheader("Model Performance Metrics")
        if st.session_state['model_choice'] == "ARIMA":
            col1, col2, col3 = st.columns(3)
            col1.metric("MAE (S&P 500)", "0.126876")
            col2.metric("MSE (S&P 500)", "0.021128")
            col3.metric("RMSE (S&P 500)", "0.145356")
            col4, col5 = st.columns([1, 1])
            col4.image(Image.open('S&P/Arima/acf.png'), caption='Autocorrelation', use_column_width=True)
            col5.image(Image.open('S&P/Arima/arima.png'), caption='ARIMA Forecast', use_column_width=True)

        elif st.session_state['model_choice'] == "ANN":
            col1, col2 = st.columns(2)
            col1.metric("MAE", "0.012780")
            col2.metric("MSE", "0.000312")
            st.image(Image.open('S&P/Ann/ann.png'), caption='ANN Forecast', use_column_width=True)

        elif st.session_state['model_choice'] == "Hybrid ARIMA-ANN":
            col1, col2 = st.columns(2)
            col1.metric("Mean Absolute Error", "0.033090")
            col2.metric("Mean Squared Error", "0.001910")
            st.image(Image.open('S&P/Hybrid/hybrid.png'), caption='Hybrid ARIMA-ANN Forecast', use_column_width=True)

        elif st.session_state['model_choice'] == "LSTM":
            col1, col2 = st.columns(2)
            col1.metric("Mean Absolute Error", "194.293")
            col2.metric("Mean Squared Error", "57554.099")
            st.image(Image.open('S&P/LSTM/lstm.png'), caption='LSTM Forecast', use_column_width=True)

        elif st.session_state['model_choice'] == "Prophet":
            col1, col2 = st.columns(2)
            col1.metric("Mean Absolute Error", "153.982")
            col2.metric("Mean Squared Error", "44179.517")
            st.image(Image.open('S&P/Prophet/prophet.png'), caption='Prophet Forecast', use_column_width=True)

        elif st.session_state['model_choice'] == "SVR":
            col1, col2 = st.columns(2)
            col1.metric("Mean Absolute Error", "407.331")
            col2.metric("Mean Squared Error", "346281.717")
            st.image(Image.open('S&P/SVR/svr.png'), caption='SVR Forecast', use_column_width=True)

    elif st.session_state['dataset'] == "Daily CO2 Concentrations":
        st.subheader("Model Performance Metrics")
        if st.session_state['model_choice'] == "ARIMA":
            col1, col2, col3 = st.columns(3)
            col1.metric("MAE (CO2)", "0.004827")
            col2.metric("MSE (CO2)", f"{3.5062367863404307e-05:.8f}")
            col3.metric("RMSE (CO2)", "0.005921")
            col4, col5 = st.columns([1, 1])
            col4.image(Image.open('CO2/Arima/acf.png'), caption='Autocorrelation', use_column_width=True)
            col5.image(Image.open('CO2/Arima/arima.png'), caption='ARIMA Forecast', use_column_width=True)

        elif st.session_state['model_choice'] == "ANN":
            col1, col2 = st.columns(2)
            col1.metric("MAE", "0.002323")
            col2.metric("MSE", f"{1.371504769410519e-05:.8f}")
            st.image(Image.open('CO2/Ann/ann.png'), caption='ANN Forecast', use_column_width=True)

        elif st.session_state['model_choice'] == "Hybrid ARIMA-ANN":
            col1, col2 = st.columns(2)
            col1.metric("Mean Absolute Error", "0.714566")
            col2.metric("Mean Squared Error", "1.009527")
            st.image(Image.open('CO2/Hybrid/hybrid.png'), caption='Hybrid ARIMA-LSTM Forecast', use_column_width=True)

        elif st.session_state['model_choice'] == "LSTM":
            col1, col2 = st.columns(2)
            col1.metric("Mean Absolute Error", "0.709639")
            col2.metric("Mean Squared Error", "1.005047")
            st.image(Image.open('CO2/LSTM/lstm.png'), caption='LSTM Forecast', use_column_width=True)

        elif st.session_state['model_choice'] == "Prophet":
            col1, col2 = st.columns(2)
            col1.metric("Mean Absolute Error", "0.495909")
            col2.metric("Mean Squared Error", "0.435974")
            st.image(Image.open('CO2/Prophet/prophet.png'), caption='Prophet Forecast', use_column_width=True)

        elif st.session_state['model_choice'] == "SVR":
            col1, col2 = st.columns(2)
            col1.metric("Mean Absolute Error", "2.529058")
            col2.metric("Mean Squared Error", "9.792074")
            st.image(Image.open('CO2/SVR/svr.png'), caption='SVR Forecast', use_column_width=True)


    # Reset to dataset selection
    if st.button('Start Over'):
        st.session_state['stage'] = 'dataset_selection'
        st.session_state['dataset'] = None
        st.session_state['model_choice'] = None

