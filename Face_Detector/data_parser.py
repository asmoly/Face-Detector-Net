import numpy as np
import pickle

dataset = []

endOfDataSet = False
counter = 0

with open("Data/wider_face_split/wider_face_val_bbx_gt.txt", "r") as f:
    while endOfDataSet == False:
        path = f.readline().replace("\n", "")

        if path == "":
            endOfDataSet = True
            break

        amountOfFaces = int(f.readline().replace("\n", ""))

        boundingBoxes = np.empty(20)
        for i in range (0, amountOfFaces):
            target = f.readline().replace("\n", "").split()
            
            try:
                boundingBoxes[0 + i*4] = int(target[0])
                boundingBoxes[1 + i*4] = int(target[1])
                boundingBoxes[2 + i*4] = int(target[2])
                boundingBoxes[3 + i*4] = int(target[3])
            except:
                pass

        if amountOfFaces == 0:
            f.readline()

        if amountOfFaces <= 5:
            for i in range (amountOfFaces, 5):
                boundingBoxes[0 + i*4] = 0
                boundingBoxes[1 + i*4] = 0
                boundingBoxes[2 + i*4] = 0
                boundingBoxes[3 + i*4] = 0

            dataset.append((path, boundingBoxes))


        counter += 1
        print(counter)

dataset = np.array(dataset, dtype=object)
pickle.dump(dataset, open("Training_Data/dataset_val", "wb"))