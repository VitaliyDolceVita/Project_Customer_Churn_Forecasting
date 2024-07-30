import streamlit as st
import pandas as pd
import pickle

# Завантаження збереженої моделі та скалера
with open('rf_modelf1.pkl', 'rb') as file:
    rf_model = pickle.load(file)

with open('scalerf1.pkl', 'rb') as file:
    scaler = pickle.load(file)

st.markdown("# :rainbow[Прогнозування Відтоку Клієнтів]")

st.sidebar.header("Введіть дані нового клієнта:")

def user_input_features():
    is_tv_subscriber = st.sidebar.selectbox("Чи є абонентом телебачення?", [0, 1], key='is_tv_subscriber')
    is_movie_package_subscriber = st.sidebar.selectbox("Чи є абонентом пакету фільмів?", [0, 1], key='is_movie_package_subscriber')
    subscription_age = st.sidebar.number_input("Термін підписки", min_value=0.0, max_value=100.0, step=0.01, key='subscription_age')
    bill_avg = st.sidebar.number_input("Середній рахунок", min_value=0.0, max_value=1000.0, step=0.01, key='bill_avg')
    service_failure_count = st.sidebar.number_input("Кількість збоїв у сервісі", min_value=0, max_value=100, step=1, key='service_failure_count')
    download_avg = st.sidebar.number_input("Середня швидкість скачування", min_value=0.0, max_value=100.0, step=0.01, key='download_avg')
    upload_avg = st.sidebar.number_input("Середня швидкість завантаження", min_value=0.0, max_value=100.0, step=0.01, key='upload_avg')
    download_over_limit = st.sidebar.number_input("Кількість перевищень ліміту скачування", min_value=0, max_value=100, step=1, key='download_over_limit')

    data = {
        'is_tv_subscriber': is_tv_subscriber,
        'is_movie_package_subscriber': is_movie_package_subscriber,
        'subscription_age': subscription_age,
        'bill_avg': bill_avg,
        'service_failure_count': service_failure_count,
        'download_avg': download_avg,
        'upload_avg': upload_avg,
        'download_over_limit': download_over_limit
    }

    features = pd.DataFrame(data, index=[0])
    return features

input_df = user_input_features()

def preprocess_input(df):
    # Переконайтесь, що усі необхідні ознаки включені
    required_features = ['subscription_age', 'bill_avg', 'service_failure_count', 'download_avg',
                         'upload_avg', 'download_over_limit']
    
    for feature in required_features:
        if feature not in df.columns:
            df[feature] = 0  # Заповнюємо відсутні ознаки нулями або значеннями за замовчуванням

    # Переставте стовпці у правильному порядку
    df = df[required_features]
    
    try:
        df = scaler.transform(df)  # Масштабування введених даних
        return df
    except Exception as e:
        st.error(f"Помилка при попередній обробці даних: {e}")
        return None

if input_df is not None:
    preprocessed_input = preprocess_input(input_df)

    if preprocessed_input is not None:
        try:
            prediction_proba = rf_model.predict_proba(preprocessed_input)[:, 1]
            prediction = (prediction_proba >= 0.5).astype(int)

            # Вивід результатів
            st.subheader('Ймовірність відтоку клієнта')
            st.markdown(f"<h2 style='font-size:28px; color: magenta;'>{prediction_proba[0]:.2f}</h2>", unsafe_allow_html=True)

            st.subheader('Клієнт має високу/низьку ймовірність відтоку')

            if prediction[0] == 1:
                st.markdown("<h2 style='font-size:28px; color: red;'>Клієнт має високу ймовірність відтоку</h2>", unsafe_allow_html=True)
            else:
                st.markdown("<h2 style='font-size:28px; color: green;'>Клієнт має низьку ймовірність відтоку</h2>", unsafe_allow_html=True)
        except Exception as e:
            st.error(f"Помилка при прогнозуванні: {e}")
else:
    st.error("Не надано даних для обробки")



