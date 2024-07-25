import streamlit as st
from PIL import Image
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing.image import img_to_array

# Load the trained model
model_path = 'models/trained_model.h5'
model = tf.keras.models.load_model(model_path)

# Define the class names
class_names = ['AnnualCrop', 'Forest', 'HerbaceousVegetation', 'Highway', 'Industrial',
               'Pasture', 'PermanentCrop', 'Residential', 'River', 'SeaLake']

# Function to preprocess the uploaded image
def preprocess_image(image, target_size):
    image = image.resize(target_size)
    image_array = img_to_array(image)
    image_array = np.expand_dims(image_array, axis=0)
    image_array = image_array / 255.0
    return image_array

# Main function to run the app
def main():
    st.title("Satellite Image Classification")

    uploaded_files = st.file_uploader("Choose satellite images...", type=["jpg", "jpeg", "png"],
                                      accept_multiple_files=True)

    if uploaded_files:
        st.write(f"Number of images uploaded: {len(uploaded_files)}")

        # Display images in a grid
        cols = st.columns(3)  # Adjust the number of columns as needed
        for i, uploaded_file in enumerate(uploaded_files):
            with cols[i % 3]:
                image = Image.open(uploaded_file)
                st.image(image, caption='Uploaded Image', use_column_width=True)

                preprocessed_image = preprocess_image(image, target_size=(64, 64))
                predictions = model.predict(preprocessed_image)
                predicted_class = np.argmax(predictions[0])
                confidence = np.max(predictions[0])

                st.write(f"Prediction: {class_names[predicted_class]}")
                st.write(f"Confidence: {confidence:.2f}")

    # Add a footer with some basic HTML/CSS styling
    st.markdown(
        """
        <style>
        .reportview-container .main footer {visibility: hidden;}
        .reportview-container .main:after {
            content:'Created by [Your Name]'; 
            visibility: visible;
            display: block;
            position: relative;
            text-align: center;
            color: gray;
            padding: 10px;
            top: 2px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    main()
