import streamlit as st
import pandas as pd
import pickle

# Завантаження збереженої моделі та скалера
with open('rf_model.pkl', 'rb') as file:
    rf_model = pickle.load(file)

with open('scaler.pkl', 'rb') as file:
    scaler = pickle.load(file)

st.markdown("# :rainbow[Прогнозування Відтоку Клієнтів]")

st.sidebar.header("Введіть дані нового клієнта:")


# Функція для введення даних клієнта через інтерфейс Streamlit
def user_input_features():
    is_tv_subscriber = st.sidebar.selectbox("Чи є абонентом телебачення?/is_tv_subscriber", [0, 1],
                                            key='is_tv_subscriber')
    is_movie_package_subscriber = st.sidebar.selectbox("Чи є абонентом пакету фільмів?/is_movie_package_subscriber",
                                                       [0, 1], key='is_movie_package_subscriber')
    subscription_age = st.sidebar.number_input("Термін підписки/subscription_age", min_value=0.0, max_value=100.0,
                                               step=0.01, key='subscription_age')
    bill_avg = st.sidebar.number_input("Середній рахунок/bill_avg", min_value=0.0, max_value=1000.0, step=0.01,
                                       key='bill_avg')
    service_failure_count = st.sidebar.number_input("Кількість збоїв у сервісі/service_failure_count", min_value=0,
                                                    max_value=100, step=1, key='service_failure_count')
    download_avg = st.sidebar.number_input("Середня швидкість скачування/download_avg", min_value=0.0, max_value=100.0,
                                           step=0.01, key='download_avg')
    upload_avg = st.sidebar.number_input("Середня швидкість завантаження/upload_avg", min_value=0.0, max_value=100.0,
                                         step=0.01, key='upload_avg')
    download_over_limit = st.sidebar.number_input("Кількість перевищень ліміту скачування?/download_over_limit",
                                                  min_value=0, max_value=100, step=1, key='download_over_limit')

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

if st.sidebar.button('Прогнозувати'):
    if input_df is not None:  # гарантує, що дані для обробки були введені користувачем
        def preprocess_input(df):  # Попередня обробка даних
            # Масштабуємо лише ті колонки, які були використані при навчанні скалера
            df_scaled = df[['subscription_age', 'bill_avg', 'service_failure_count', 'download_avg', 'upload_avg',
                            'download_over_limit']]
            df_scaled = scaler.transform(df_scaled)

            # Перетворюємо назад в DataFrame
            df_scaled = pd.DataFrame(df_scaled,
                                     columns=['subscription_age', 'bill_avg', 'service_failure_count', 'download_avg',
                                              'upload_avg', 'download_over_limit'])

            # Додаємо немасштабовані колонки
            df_scaled['is_tv_subscriber'] = df['is_tv_subscriber'].values
            df_scaled['is_movie_package_subscriber'] = df['is_movie_package_subscriber'].values

            # Переставляємо колонки в правильному порядку
            df_scaled = df_scaled[['is_tv_subscriber', 'is_movie_package_subscriber', 'subscription_age', 'bill_avg',
                                   'service_failure_count', 'download_avg', 'upload_avg', 'download_over_limit']]
            return df_scaled


        preprocessed_input = preprocess_input(input_df)

        # Прогнозування
        prediction_proba = rf_model.predict_proba(preprocessed_input)[:, 1]
        prediction = (prediction_proba >= 0.5).astype(int)

        # Вивід результатів
        st.subheader('Ймовірність відтоку клієнта')
        st.markdown(f"<h2 style='font-size:28px; color: magenta;'>{prediction_proba[0]:.2f}</h2>",
                    unsafe_allow_html=True)

        st.subheader('Клієнт має високу/низьку ймовірність відтоку')

        if prediction[0] == 1:
            st.markdown("<h2 style='font-size:28px; color: red;'>Клієнт має високу ймовірність відтоку</h2>",
                        unsafe_allow_html=True)
        else:
            st.markdown("<h2 style='font-size:28px; color: green;'>Клієнт має низьку ймовірність відтоку</h2>",
                        unsafe_allow_html=True)






