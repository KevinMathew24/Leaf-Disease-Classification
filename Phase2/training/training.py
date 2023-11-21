import tensorflow as tf
# from tensorflow.keras import models , layers
# import matplotlib.pyplot as plt

#this is how you input into the dataset--------------------
images_ds = tf.data.Dataset.list_files('D:/Uni Crap/Leaf-Disease-Classification/Phase2/training/dataset/PlantVillage/*/*', shuffle=True)


# for file in images_ds.take(3):
#     print(file.numpy())

image_count= len(images_ds)
print("Image Count: ", image_count)

train_size = int(image_count*0.8)

train_ds = images_ds.take(train_size)
test_ds = images_ds.skip(train_size)