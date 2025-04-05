import tensorflow as tf
from tensorflow.keras import layers, models
import numpy as np
import cv2
import os

# Directory paths
train_dir = "synthetic_aadhaar_cards"
valid_dir = "invalid_aadhaar_cards"

# Image dimensions
IMG_SIZE = (150, 300)

# Function to preprocess images
def load_and_preprocess_image(image_path):
    img = cv2.imread(image_path)
    img = cv2.resize(img, IMG_SIZE)
    img = img / 255.0  # Normalize
    return img

# Load images and labels
def load_dataset(directory, label):
    images, labels = [], []
    for filename in os.listdir(directory):
        path = os.path.join(directory, filename)
        img = load_and_preprocess_image(path)
        images.append(img)
        labels.append(label)
    return np.array(images), np.array(labels)

# Load training data
valid_images, valid_labels = load_dataset(train_dir, 1)  # Valid Aadhaar cards (Label: 1)
invalid_images, invalid_labels = load_dataset(valid_dir, 0)  # Invalid Aadhaar cards (Label: 0)

# Merge datasets
X_train = np.concatenate([valid_images, invalid_images])
y_train = np.concatenate([valid_labels, invalid_labels])

# Define CNN Model (EfficientNetLite for fast validation)
model = models.Sequential([
    layers.Conv2D(32, (3, 3), activation="relu", input_shape=(150, 300, 3)),
    layers.MaxPooling2D(2, 2),
    layers.Conv2D(64, (3, 3), activation="relu"),
    layers.MaxPooling2D(2, 2),
    layers.Flatten(),
    layers.Dense(128, activation="relu"),
    layers.Dense(1, activation="sigmoid")  # Output: Valid/Invalid Aadhaar
])

# Compile Model
model.compile(optimizer="adam", loss="binary_crossentropy", metrics=["accuracy"])

# Train Model
model.fit(X_train, y_train, epochs=10, batch_size=32, validation_split=0.2)

# Save Model
model.save("aadhaar_validation_cnn.h5")

# Function to validate an uploaded Aadhaar card
def validate_aadhaar(image_path):
    img = load_and_preprocess_image(image_path)
    img = np.expand_dims(img, axis=0)  # Reshape for CNN
    prediction = model.predict(img)[0][0]
    
    return "✅ Valid Aadhaar" if prediction >= 0.60 else "❌ Invalid Aadhaar"

# Example Usage
input_image_path = r"C:\Users\Priyesh Pandey\Desktop\sample_aadhaar_card.png"
print(validate_aadhaar(input_image_path))
