# import streamlit as st
# import tensorflow as tf
# from pathlib import Path
# import numpy as np
# import matplotlib.pyplot as plt
# from PIL import Image

# # Set up the page
# st.set_page_config(
#     page_title="Klasifikasi Citra Instrumen Musik",
#     page_icon="🎶",
#     layout="centered"
# )

# # Gaya halaman
# st.markdown(
#     """
#     <style>
#     .main {
#         background-color: #f4f4f4;
#         border-radius: 10px;
#         padding: 20px;
#         box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
#     }
#     h1 {
#         color: #333333;
#     }
#     .stButton button {
#         background-color: #007bff;
#         color: white;
#         border-radius: 5px;
#         padding: 10px 20px;
#     }
#     .stButton button:hover {
#         background-color: #0056b3;
#     }
#     </style>
#     """,
#     unsafe_allow_html=True
# )

# # Sidebar untuk navigasi
# st.sidebar.title("Navigasi")
# st.sidebar.info("""
# - Unggah citra melalui bagian utama.
# - Klik tombol Predict untuk melihat hasil.
# - Dapatkan probabilitas untuk setiap kelas.
# """)

# # Header utama
# st.markdown("<div class='main'>", unsafe_allow_html=True)
# st.title(":musical_note: Klasifikasi Citra Instrumen Musik")
# st.markdown("""
# Selamat datang di aplikasi klasifikasi citra instrumen musik! 
# Unggah citra instrumen Anda, dan model akan memprediksi jenis instrumen tersebut.
# """)

# # Menempatkan file uploader
# col1, col2, col3 = st.columns([1, 2, 1])
# with col2:
#     upload = st.file_uploader('Unggah citra (format: PNG, JPG)', type=['png', 'jpg', 'jpeg'])

# def predict(image):
#     class_names = [
#         "Didgeridoo", "Tambourine", "Xylophone", "Acordian", "Alphorn",
#         "Bagpipes", "Banjo", "Bongo Drum", "Casaba", "Castanets",
#         "Clarinet", "Clavichord", "Concertina", "Drums", "Dulcimer",
#         "Flute", "Guiro", "Guitar", "Harmonica", "Harp",
#         "Marakas", "Ocarina", "Piano", "Saxophone", "Sitar",
#         "Steel Drum", "Trombone", "Trumpet", "Tuba", "Violin"
#     ]

#     # Load and preprocess the image
#     img = tf.keras.utils.load_img(image, target_size=(224, 224))
#     img_array = tf.keras.utils.img_to_array(img)
#     img_array = tf.expand_dims(img_array, 0)

#     # Load the trained model
#     model = tf.keras.models.load_model(Path("src/uaprio/RestNet50_model.h5"))

#     # Make predictions
#     output = model.predict(img_array)
#     scores = tf.nn.softmax(output[0]).numpy()
#     return class_names, scores

# if upload is not None:
#     st.image(upload, caption="Citra yang diunggah", use_column_width=True)
#     st.subheader("Informasi Citra")
#     file_details = {"Filename": upload.name, "FileType": upload.type, "FileSize": upload.size}
#     st.json(file_details)

#     if st.button("Predict", type="primary"):
#         with st.spinner('Model sedang memproses citra...'):
#             class_names, scores = predict(upload)

#         # Display prediction result
#         st.success("Prediksi selesai!")
#         predicted_class = class_names[np.argmax(scores)]
#         st.subheader(f"Hasil prediksi: {predicted_class}")

#         # Visualize probabilities
#         st.subheader("Probabilitas untuk setiap kelas")
#         fig, ax = plt.subplots()
#         ax.bar(class_names, scores, color='skyblue')
#         ax.set_title("Probabilitas Klasifikasi")
#         ax.set_ylabel("Probabilitas")
#         ax.set_xlabel("Kelas")
#         plt.xticks(rotation=90)
#         st.pyplot(fig)
# else:
#     st.info("Silakan unggah citra untuk memulai klasifikasi.")
# st.markdown("</div>", unsafe_allow_html=True)

import streamlit as st
import tensorflow as tf
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
import io

# Set up the page
st.set_page_config(
    page_title="Klasifikasi Citra Instrumen Musik",
    page_icon="🎶",
    layout="wide"
)

# Display background image instead of title text
st.image("assets/background.png", use_container_width=True)

# File uploader
st.markdown("""
    <div style='text-align: center;'>
        <h3 style='color: #fbe4a5;'>Unggah citra instrumen Anda di sini:</h3>
    </div>
""", unsafe_allow_html=True)

upload = st.file_uploader('', type=['png', 'jpg', 'jpeg'])

def predict(image, model):
    class_names = [
        "Didgeridoo", "Tambourine", "Xylophone", "Acordian", "Alphorn",
        "Bagpipes", "Banjo", "Bongo Drum", "Casaba", "Castanets",
        "Clarinet", "Clavichord", "Concertina", "Drums", "Dulcimer",
        "Flute", "Guiro", "Guitar", "Harmonica", "Harp",
        "Marakas", "Ocarina", "Piano", "Saxophone", "Sitar",
        "Steel Drum", "Trombone", "Trumpet", "Tuba", "Violin"
    ]

    # Load and preprocess the image
    img = tf.keras.utils.load_img(image, target_size=(224, 224))
    img_array = tf.keras.utils.img_to_array(img)
    img_array = tf.expand_dims(img_array, 0)

    # Make predictions
    output = model.predict(img_array)
    scores = tf.nn.softmax(output[0]).numpy()
    return class_names, scores

if upload is not None:
    # Display the uploaded image with a specific width
    st.image(upload, caption="Citra yang diunggah", use_container_width=False, width=500)
    st.subheader("Informasi Citra")
    file_details = {"Filename": upload.name, "FileType": upload.type, "FileSize": upload.size}
    st.json(file_details)

    if st.button("Predict", type="primary"):
        with st.spinner('Model sedang memproses citra...'):
            # Load the models
            model_resnet = tf.keras.models.load_model(Path("src/uaprio/RestNet50_model.h5"))
            model_vgg = tf.keras.models.load_model(Path("src/uaprio/VGG16_model.h5"))

            # Predict using both models
            class_names_resnet, scores_resnet = predict(upload, model_resnet)
            class_names_vgg, scores_vgg = predict(upload, model_vgg)

        # Create two columns for side-by-side display
        col1, col2 = st.columns(2)

        # Display the ResNet50 results in the first column
        with col1:
            st.success("Prediksi selesai menggunakan ResNet50!")
            predicted_class_resnet = class_names_resnet[np.argmax(scores_resnet)]
            st.subheader(f"Hasil prediksi (ResNet50): {predicted_class_resnet}")

            # Visualize probabilities with a bar chart for ResNet
            st.subheader("Probabilitas untuk setiap kelas (ResNet50)")
            fig, ax = plt.subplots(figsize=(15, 10))
            ax.bar(class_names_resnet, scores_resnet, color='skyblue')
            ax.set_title("Probabilitas Klasifikasi (ResNet50)")
            ax.set_ylabel("Probabilitas")
            ax.set_xlabel("Kelas")
            plt.xticks(rotation=90)

            # Save the plot to a BytesIO object for ResNet
            buf_resnet = io.BytesIO()
            plt.savefig(buf_resnet, format="png")
            buf_resnet.seek(0)

            # Display the plot as an image with the specified width for ResNet
            st.image(buf_resnet, use_container_width=False, width=900)
            plt.close(fig)

        # Display the VGG16 results in the second column
        with col2:
            st.success("Prediksi selesai menggunakan VGG16!")
            predicted_class_vgg = class_names_vgg[np.argmax(scores_vgg)]
            st.subheader(f"Hasil prediksi (VGG16): {predicted_class_vgg}")

            # Visualize probabilities with a bar chart for VGG
            st.subheader("Probabilitas untuk setiap kelas (VGG16)")
            fig, ax = plt.subplots(figsize=(15, 10))
            ax.bar(class_names_vgg, scores_vgg, color='skyblue')
            ax.set_title("Probabilitas Klasifikasi (VGG16)")
            ax.set_ylabel("Probabilitas")
            ax.set_xlabel("Kelas")
            plt.xticks(rotation=90)

            # Save the plot to a BytesIO object for VGG
            buf_vgg = io.BytesIO()
            plt.savefig(buf_vgg, format="png")
            buf_vgg.seek(0)

            # Display the plot as an image with the specified width for VGG
            st.image(buf_vgg, use_container_width=False, width=900)
            plt.close(fig)

else:
    st.info("Silakan unggah citra untuk memulai klasifikasi.")
