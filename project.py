from keras import models
from keras import layers
from tensorflow.keras.utils import to_categorical
from keras.datasets import mnist
(x_train_images, y_train_labels),\
(x_test_images, y_test_labels) = mnist.load_data()
network = models.Sequential()
network.add(layers.Dense(512, activation='relu', input_shape=(28 * 28,)))
network.add(layers.Dense(10, activation='softmax'))

fix_x_train_images = x_train_images.reshape((60000, 28 * 28)).astype('float32') / 255
fix_x_test_images = x_test_images.reshape((10000, 28 * 28)).astype('float32') / 255

network.compile(optimizer='rmsprop',
        loss='categorical_crossentropy',
        metrics=['accuracy'])

 
fix_x_train_labels = to_categorical(y_train_labels)
fix_x_test_labels = to_categorical(y_test_labels)
result = network.fit(
    fix_x_train_images,
    fix_x_train_labels,
    epochs=20,
    batch_size=128,
    validation_data=(fix_x_test_images, fix_x_test_labels))