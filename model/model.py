import tensorflow as tf
import time

# Create a dummy dataset
data = tf.constant([[1, 1], [0, 0], [2, 0], [2, 1], [3, 0], [0, 4], [5, 6], [0, 10]])
label = tf.constant([1, 0, 0, 1, 0, 0, 1, 0])

# Define model
model = tf.keras.Sequential(
    [
        tf.keras.Input(shape=(2,)),
        tf.keras.layers.Dense(20, activation="relu"),
        tf.keras.layers.Dense(2, activation="softmax")
    ]
)

print(model.summary())

# Compile model
model.compile(optimizer='adam',
              loss=tf.keras.losses.BinaryCrossentropy(),
              metrics=['accuracy'])

# Train model
model.fit(data, label, batch_size=2, epochs=25)

# Save trained model
save_time = int(time.time())
path = f"./saved_models/{save_time}"
model.save(path, save_format='tf')
