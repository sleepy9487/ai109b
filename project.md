## 期末專案:minist訓練模型  
# 前言  
* 參考資料來源  
  * [深度學習與Keras] (https://github.com/twtrubiks/face-recognition-notes)  
  * [Keras:Mnist](https://waternotetw.blogspot.com/2018/03/keras-mnist.html)  
  * [使用Keras進行深度學習](https://zhuanlan.zhihu.com/p/34822375)  
  * [DeepingLearningKeras手寫辨識Mnist] (https://medium.com/bryanyang0528/deep-learning-keras-%E6%89%8B%E5%AF%AB%E8%BE%A8%E8%AD%98-mnist-b41757567684)  
* 以mnist做練習  

# [Mnist資料集](https://en.wikipedia.org/wiki/MNIST_database)  
>圖片來源也在此
* MNIST數據庫是一個手寫數字的大型數據庫，通常用於訓練各種圖像處理系統。該數據庫還廣泛用於機器學習領域的培訓和測試，該數據庫還廣泛用於機器學習領域的培訓和測試。它是通過“重新混合”來自NIST原始數據集的樣本而創建的。

# 下載Mnist數據集
```
from keras.datasets import mnist  
(x_train_images, y_train_labels),(x_test_images, y_test_labels) = mnist.load_data()
```
>Kersa以預備好mnist數據集，從資料庫提取即可
>Mnist資料分有訓練圖像跟測試圖像
>image是用來訓練的資料,label則是資料對應的正確答案
# Mnist資料型態
```
x_train_images.shape  
len(y_train_labels)  
x_test_images.shape  
len(y_test_labels)  
```
>查看資料集的結構
>我們可以得出訓練圖像有60000筆、測試圖像是10000筆,image都是28x28
# 資料處理
```
fix_x_train_images = x_train_images.reshape((60000, 28 * 28)).astype('float32') / 255
fix_x_test_images = x_test_images.reshape((10000, 28 * 28)).astype('float32') / 255
```
>將資料正規劃  
# 建模  
```
network = models.Sequential()
network.add(layers.Dense(512, activation='relu', input_shape=(28 * 28,)))
network.add(layers.Dense(10, activation='softmax'))

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
```
>建模並訓練模型

* Result
```
469/469 [==============================] - 23s 11ms/step - loss: 0.4194 - accuracy: 0.8802 - val_loss: 0.1287 - val_accuracy: 0.9612
Epoch 2/20
469/469 [==============================] - 4s 9ms/step - loss: 0.1069 - accuracy: 0.9693 - val_loss: 0.0919 - val_accuracy: 0.9724
Epoch 3/20
469/469 [==============================] - 4s 8ms/step - loss: 0.0681 - accuracy: 0.9787 - val_loss: 0.0749 - val_accuracy: 0.9767
Epoch 4/20
469/469 [==============================] - 4s 8ms/step - loss: 0.0473 - accuracy: 0.9865 - val_loss: 0.0644 - val_accuracy: 0.9810
Epoch 5/20
469/469 [==============================] - 4s 9ms/step - loss: 0.0336 - accuracy: 0.9897 - val_loss: 0.0705 - val_accuracy: 0.9797
Epoch 6/20
469/469 [==============================] - 4s 7ms/step - loss: 0.0290 - accuracy: 0.9922 - val_loss: 0.0684 - val_accuracy: 0.9799
Epoch 7/20
469/469 [==============================] - 4s 8ms/step - loss: 0.0213 - accuracy: 0.9940 - val_loss: 0.0701 - val_accuracy: 0.9810
Epoch 8/20
469/469 [==============================] - 3s 7ms/step - loss: 0.0147 - accuracy: 0.9960 - val_loss: 0.0652 - val_accuracy: 0.9828
Epoch 9/20
469/469 [==============================] - 4s 8ms/step - loss: 0.0117 - accuracy: 0.9971 - val_loss: 0.0644 - val_accuracy: 0.9829
Epoch 10/20
469/469 [==============================] - 5s 10ms/step - loss: 0.0089 - accuracy: 0.9977 - 
val_loss: 0.0725 - val_accuracy: 0.9805
Epoch 11/20
469/469 [==============================] - 4s 9ms/step - loss: 0.0071 - accuracy: 0.9982 - val_loss: 0.0732 - val_accuracy: 0.9826
Epoch 12/20
469/469 [==============================] - 4s 9ms/step - loss: 0.0061 - accuracy: 0.9984 - val_loss: 0.0691 - val_accuracy: 0.9826
Epoch 13/20
469/469 [==============================] - 4s 7ms/step - loss: 0.0036 - accuracy: 0.9991 - val_loss: 0.0726 - val_accuracy: 0.9819
Epoch 14/20
469/469 [==============================] - 3s 7ms/step - loss: 0.0034 - accuracy: 0.9990 - val_loss: 0.0716 - val_accuracy: 0.9845
Epoch 15/20
469/469 [==============================] - 3s 7ms/step - loss: 0.0025 - accuracy: 0.9993 - val_loss: 0.0799 - val_accuracy: 0.9821
Epoch 16/20
469/469 [==============================] - 4s 8ms/step - loss: 0.0022 - accuracy: 0.9994 - vEpoch 17/20
469/469 [==============================] - 3s 7ms/step - loss: 0.0016 - accuracy: 0.9995 - val_loss: 0.0894 - val_accuracy: 0.9821
Epoch 18/20
469/469 [==============================] - 3s 7ms/step - loss: 0.0011 - accuracy: 0.9997 - val_loss: 0.0889 - val_accuracy: 0.9824
Epoch 19/20
469/469 [==============================] - 3s 7ms/step - loss: 7.5595e-04 - accuracy: 0.9998 - val_loss: 0.0958 - val_accuracy: 0.9813
Epoch 20/20
469/469 [==============================] - 3s 7ms/step - loss: 7.2355e-04 - accuracy: 0.9998 - val_loss: 0.0883 - val_accuracy: 0.9837
```
> 訓練的正確率落在0.98左右  
# 測試  
```  
loss, acc = network.evaluate(fix_x_test_images, fix_x_test_labels)
print('loss:', loss)
print('acc:', acc)
```  
>將訓練後的模型輸入測試進行評鑑
* Result
```
loss: 0.09333343058824539
acc: 0.9829000234603882
```
