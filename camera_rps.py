import cv2
from keras.models import load_model
import numpy as np

model = load_model('keras_model.h5')
cap = cv2.VideoCapture(0)
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
class_names = open('labels.txt', 'r').readlines()

def get_prediction():

    ret, frame = cap.read()
    resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
    image_np = np.array(resized_frame)
    normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
    data[0] = normalized_image
    prediction = model.predict(data)
    cv2.imshow('frame', frame)
    cv2.waitKey(2000)

    # Release the cap object
    cap.release()
    # Destroy all the windows
    cv2.destroyAllWindows()

    # index = np.argmax(prediction)
    # class_name = class_names[index]
    # confidence_score = prediction[0][index]

    return prediction

print(get_prediction())