from cv2 import cv2 
import numpy as np
import glob
import random

class ImageCheck:

    def checkPool(self):
        return_set=set()
        # Load Yolo
        net = cv2.dnn.readNet("yolov3_training_last.weights", "yolov3_testing.cfg")
        net2 = cv2.dnn.readNet("yolov3.weights", "yolov3.cfg")

        # Name custom object
        classes = ["pool"]

        classes2 = []
        with open("coco.names", "r") as f:
            classes2 = [line.strip() for line in f.readlines()]

        # Images path
        images_path = glob.glob(r"C:\Users\nabaj\Pictures\swimming_pool\*.jpg")


        count=0
        layer_names = net.getLayerNames()
        output_layers = [layer_names[i[0] - 1] for i in net.getUnconnectedOutLayers()]
        colors = np.random.uniform(0, 255, size=(len(classes), 3))

        layer_names2 = net2.getLayerNames()
        output_layers2 = [layer_names2[i[0] - 1] for i in net2.getUnconnectedOutLayers()]
        colors2 = np.random.uniform(0, 255, size=(len(classes2), 3))

        # Insert here the path of your images
        #random.shuffle(images_path)
        # loop through all the images
        for img_path in images_path:
            print("ok")
            # Loading image
            img = cv2.imread(img_path)
            #img = cv2.resize(img, None, fx=0.4, fy=0.4)
            height, width, channels = img.shape

            # Detecting objects
            blob = cv2.dnn.blobFromImage(img, 0.00392, (416, 416), (0, 0, 0), True, crop=False)

            net.setInput(blob)
            outs = net.forward(output_layers)

            # Showing informations on the screen
            class_ids = []
            confidences = []
            boxes = []
            for out in outs:
                for detection in out:
                    scores = detection[5:]
                    class_id = np.argmax(scores)
                    confidence = scores[class_id]
                    if confidence > 0.3:
                        # Object detected
                        # print(class_id)
                        center_x = int(detection[0] * width)
                        center_y = int(detection[1] * height)
                        w = int(detection[2] * width)
                        h = int(detection[3] * height)

                        # Rectangle coordinates
                        x = int(center_x - w / 2)
                        y = int(center_y - h / 2)

                        boxes.append([x, y, w, h])
                        confidences.append(float(confidence))
                        class_ids.append(class_id)

            indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)
            #print(indexes)
            font = cv2.FONT_HERSHEY_PLAIN
            
            for i in range(len(boxes)):
                if i in indexes:
                    x, y, w, h = boxes[i]
                    label = str(classes[class_ids[i]])
                    return_set.add(label)
                    color = colors[class_ids[i]]
                    cv2.rectangle(img, (x, y), (x + w, y + h), color, 2)
                    cv2.putText(img, label, (x, y + 30), font, 3, color, 2)
                    count=count+1
                    # print(count)
                    # print("yes")

        #######

            net2.setInput(blob)
            outs2 = net2.forward(output_layers2)

            # Showing informations on the screen
            class_ids2 = []
            confidences2 = []
            boxes2 = []
            for out in outs2:
                for detection in out:
                    scores = detection[5:]
                    class_id = np.argmax(scores)
                    confidence = scores[class_id]
                    if confidence > 0.5:
                        # Object detected
                        center_x = int(detection[0] * width)
                        center_y = int(detection[1] * height)
                        w = int(detection[2] * width)
                        h = int(detection[3] * height)

                        # Rectangle coordinates
                        x = int(center_x - w / 2)
                        y = int(center_y - h / 2)

                        boxes2.append([x, y, w, h])
                        confidences2.append(float(confidence))
                        class_ids2.append(class_id)

            indexes2 = cv2.dnn.NMSBoxes(boxes2, confidences2, 0.5, 0.4)
            # print(indexes2)
            font2 = cv2.FONT_HERSHEY_SIMPLEX
            for i in range(len(boxes2)):
                if i in indexes2:
                    x, y, w, h = boxes2[i]
                    label = str(classes2[class_ids2[i]])
                    return_set.add(label)
                    color = colors2[i]
                    cv2.rectangle(img, (x, y), (x + w, y + h), color, 2)
                    cv2.putText(img, label, (x, y), font2, 1, color, 2)

        #     cv2.imshow("Image", img)
        #     key = cv2.waitKey(0)

        # cv2.destroyAllWindows()
        print(count)
        # for s in return_set:
        #     print(s)
        return return_set