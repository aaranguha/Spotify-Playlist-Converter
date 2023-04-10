import tensorflow as tf
from tensorflow import keras

# Load the pre-trained MobileNet model
model = tf.keras.applications.MobileNet()

# Load an image
img = keras.preprocessing.image.load_img("./image.jpg", target_size=(224, 224))

# Preprocess the image for the model
x = keras.preprocessing.image.img_to_array(img)
x = tf.keras.applications.mobilenet.preprocess_input(x[tf.newaxis,...])

# Make a prediction
predictions = model.predict(x)

# Get the top predicted class
predicted_class = tf.argmax(predictions[0], axis=-1)

# Print the class label
print("This image is predicted to be:", tf.keras.applications.mobilenet.decode_predictions(predictions, top=1)[0][0][1])
