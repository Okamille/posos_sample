# Librairies import
import tensorflow as tf
from tensorflow import keras
from sklearn.model_selection import train_test_split
import numpy as np
import pandas as pd
from keras.preprocessing.text import Tokenizer, text_to_word_sequence
from keras.utils import np_utils
import os


# Dataset loading
input_train = pd.read_csv('../data/input_train.csv')
X_text = input_train['question'].values

tokenizer = Tokenizer()
tokenizer.fit_on_texts(X_text)

voc_size = max(list(tokenizer.word_index.values())) + 1

X = []
for document in X_text:
    seq = text_to_word_sequence(document)
    X.append([tokenizer.word_index[word] for word in seq])

output_train = pd.read_csv('../data/output_train.csv')
y = output_train['intention'].values

num_classes = len(np.unique(y))

y = np_utils.to_categorical(y)

X_train, X_test, y_train, y_test = train_test_split(X, y)

print(len(X_train), 'train sequences')
print(len(X_test), 'test sequences')

X_train = keras.preprocessing.sequence.pad_sequences(X_train, maxlen=400)
X_test = keras.preprocessing.sequence.pad_sequences(X_test, maxlen=400)

batch_size = 32
epochs = 4

model = keras.models.Sequential([
    keras.layers.Embedding(voc_size,
                           50,
                           input_length=400), # Embedding learned
    keras.layers.Dropout(0.2),
    keras.layers.Conv1D(250,
                        3,
                        padding='valid',
                        activation='relu',
                        strides=1),
    keras.layers.GlobalMaxPooling1D(),
    keras.layers.Dense(num_classes),
    keras.layers.Activation('softmax')
])

model.compile(loss='categorical_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])

model.fit(X_train, y_train,
          batch_size=batch_size,
          epochs=epochs,
          validation_data=(X_test, y_test))

model_name = '1'

MODEL_DIR = '../models/%s' % model_name
if os.path.isdir(MODEL_DIR):
  print('\nAlready saved a model, cleaning up\n')
  !rm -r {export_path}

tf.saved_model.simple_save(
    keras.backend.get_session(),
    MODEL_DIR,
    inputs={'input_image': model.input},
    outputs={t.name:t for t in model.outputs})

print('\nSaved model:')
!ls -l {MODEL_DIR}

!saved_model_cli show --dir {MODEL_DIR} --all