import streamlit as st   # імпортуємо потрібні бібліотеки
import pandas as pd
import pickle # модуль в Python, який дозволяє серіалізувати та десеріалізувати об'єкти Python


model_path = 'rf_modelf1.pkl' # завантаження збереженої моделі та масштабувальника
scaler_path = 'scalerf1.pkl'

try:
    with open(model_path, 'rb') as file:
        rf_model = pickle.load(file)
except FileNotFoundError:   # обробляєм помилки
    st.error(f"Файл моделі '{model_path}' не знайдено.")
except pickle.UnpicklingError:
    st.error(f"Помилка при розпаковці файлу моделі '{model_path}'.")

try:
    with open(scaler_path, 'rb') as file:
        scaler = pickle.load(file)
except FileNotFoundError:
    st.error(f"Файл скалера '{scaler_path}' не знайдено.")
except pickle.UnpicklingError:
    st.error(f"Помилка при розпаковці файлу скалера '{scaler_path}'.")

st.markdown("# :rainbow[Прогнозування Відтоку Клієнтів]") # функція використовується для виведення HTML/Markdown-коду на сторінку Streamlit

st.sidebar.header("Введіть дані нового клієнта:") # вивід інформації для користувача на бічній панелі


# функція для введення даних клієнта через інтерфейс Streamlit
def user_input_features():
    is_tv_subscriber = st.sidebar.selectbox("Чи є абонентом телебачення?/is_tv_subscriber", [0, 1], key='is_tv_subscriber') # для кожного віджета призначаємо унікальний ключ
    is_movie_package_subscriber = st.sidebar.selectbox("Чи є абонентом пакету фільмів?/is_movie_package_subscriber", [0, 1], key='is_movie_package_subscriber') 
    subscription_age = st.sidebar.number_input("Термін підписки/subscription_age", min_value=0.0, max_value=100.0, step=0.01, key='subscription_age')
    bill_avg = st.sidebar.number_input("Середній рахунок/bill_avg", min_value=0.0, max_value=1000.0, step=0.01, key='bill_avg')
    service_failure_count = st.sidebar.number_input("Кількість збоїв у сервісі/service_failure_count", min_value=0, max_value=100, step=1, key='service_failure_count')
    download_avg = st.sidebar.number_input("Середня швидкість скачування/download_avg", min_value=0.0, max_value=100.0, step=0.01, key='download_avg')
    upload_avg = st.sidebar.number_input("Середня швидкість завантаження/upload_avg", min_value=0.0, max_value=100.0, step=0.01, key='upload_avg')
    download_over_limit = st.sidebar.number_input("Кількість перевищень ліміту скачування/download_over_limit", min_value=0, max_value=100, step=1, key='download_over_limit')

    data = { # дані зберігаєм в словник
        'is_tv_subscriber': is_tv_subscriber,
        'is_movie_package_subscriber': is_movie_package_subscriber,
        'subscription_age': subscription_age,
        'bill_avg': bill_avg,
        'service_failure_count': service_failure_count,
        'download_avg': download_avg,
        'upload_avg': upload_avg,
        'download_over_limit': download_over_limit
    }

    features = pd.DataFrame(data, index=[0]) # збережені дані поміщаєм в датафрейм який матиме лише один рядок, і індекс цього рядка буде дорівнювати 0
    return features # функція повертає датафрейм збережений з введеними даними


input_df = user_input_features() # зберігаєм в змінну датафрейм після обробки функцією

if st.sidebar.button('Прогнозувати'): # якщо користувач нажав кнопку
    if input_df is not None:  # гарантує, що дані для обробки були введені користувачем
        def preprocess_input(df):  # Попередня обробка датафрейму даних
            # масштабуємо лише ті колонки, які були використані при нормалізації
            df_scaled = df[['subscription_age', 'bill_avg', 'service_failure_count', 'download_avg', 'upload_avg', 'download_over_limit']]# створюємо новий датафрейм під назвою df_scaled, вибираючи лише певні стовпці з існуючого  df
            df_scaled = scaler.transform(df_scaled) # цей метод застосовує перетворення, яке було визначене під час навчання скалера, до нових даних

            # перетворюємо назад в DataFrame
            df_scaled = pd.DataFrame(df_scaled, columns=['subscription_age', 'bill_avg', 'service_failure_count', 'download_avg','upload_avg', 'download_over_limit'])

            # додаємо немасштабовані колонки
            df_scaled['is_tv_subscriber'] = df['is_tv_subscriber'].values
            df_scaled['is_movie_package_subscriber'] = df['is_movie_package_subscriber'].values

            # переставляємо колонки в правильному порядку
            df_scaled = df_scaled[['is_tv_subscriber', 'is_movie_package_subscriber', 'subscription_age', 'bill_avg', 'service_failure_count', 'download_avg', 'upload_avg', 'download_over_limit']]
            return df_scaled


        preprocessed_input = preprocess_input(input_df) #  зберігаєм в змінну

        # прогнозування
        try:
            prediction_proba = rf_model.predict_proba(preprocessed_input)[:, 1] # за допомогою моделі випадкового лісу (rf_model)  вибираєм ймовірності позитивного класу.
            prediction = (prediction_proba >= 0.5).astype(int) # перетворює масив булевих значень (True/False) в масив цілих чисел. True перетворюється в 1, а False - в 0.

            # вивід результатів
            st.subheader('Ймовірність відтоку клієнта:')
            prediction_percentage = prediction_proba[0] * 100 # отриману ймовірність множимо на 100, щоб перетворити її у відсоток
            st.markdown(f"<h2 style='font-size:28px; color: magenta;'>{prediction_percentage:.0f}%</h2>", unsafe_allow_html=True) # вставка значення змінної prediction_percentage, округленого до цілого числа (форматування .0f), з додаванням знака %.

            st.subheader('Клієнт має високу/низьку ймовірність відтоку:') # вивід інформації для користувача

            if prediction[0] == 1:
                st.markdown("<h2 style='font-size:28px; color: red;'>Клієнт має високу ймовірність відтоку</h2>", unsafe_allow_html=True) # якщо unsafe_allow_html встановлений на True, Streamlit інтерпретує HTML-код і відображає його
            else:
                st.markdown("<h2 style='font-size:28px; color: green;'>Клієнт має низьку ймовірність відтоку</h2>", unsafe_allow_html=True)
        except ValueError as e:
            st.error(f"Помилка при прогнозуванні: {e}")  # обробляєм помилки






