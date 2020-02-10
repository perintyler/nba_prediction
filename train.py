from generate_training_set import generate, get_game_data
import numpy as np
from time import sleep
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten
from tensorflow.keras.models import model_from_yaml


# generate training set
x_train, y_train = generate()

x_train = np.array(x_train)
y_train = np.array(y_train)

MODEL_SAVED = True




model = None
if(MODEL_SAVED):
    # load YAML and create model
    yaml_file = open('model.yaml', 'r')
    loaded_model_yaml = yaml_file.read()
    yaml_file.close()
    model = model_from_yaml(loaded_model_yaml)
    # load weights into new model
    model.load_weights("model.h5")
    print("Loaded model from disk")
else:
    model = Sequential()
    model.add(Flatten())
    model.add(Dense(256, activation='relu'))
    model.add(Dense(256, activation='relu'))
    model.add(Dense(2, activation='softmax'))

    # set training parameters
    model.compile(optimizer='adam',
                loss='binary_crossentropy',
                metrics=['accuracy'])


    # fit model with the training set
    model.fit(x_train, y_train, epochs=10)


games = get_game_data()
size = len(games)
predictions = model.predict(np.array(games), batch_size=size)

print(predictions)

if(MODEL_SAVED == False):
    if(np.argmax(result) == 0):
        # save ghe model
        # serialize model to JSON
        model_yaml = model.to_yaml()
        with open("model.yaml", "w") as yaml_file:
            yaml_file.write(model_yaml)
        # serialize weights to HDF5
        model.save_weights("model.h5")
        print("Saved model to disk")
