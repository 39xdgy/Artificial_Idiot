from sklearn.neural_network import MLPClassifier
from sklearn.externals import joblib
import face_recognition as face
##from call_cam import *
from pathlib import Path
from PIL import ImageFile
from PIL import Image
import os


clf = joblib.load("gender_MLP_model.pkl")
file_path = Path("/")

ImageFile.LOAD_TRUNCATED_IMAGES = True


while os.path.isfile("test.jpg"):
    img = face.load_image_file("test.jpg")

    encode = face.face_encodings(img)
    if(len(encode) != 0):
        for i in range(0, len(encode)):
            print(clf.predict(encode))

    else:
        print("No one is there!!")
