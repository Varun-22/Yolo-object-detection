from imageai.Detection import ObjectDetection
import cv2

"""Create instance of Object Detection class"""

det = ObjectDetection()

"""Setting paths for input image, output image and pretrained model weights of tiny yolo"""

model_path = "yolo-tiny.h5"
input_path = "input.jpg"
output_path = "prediction_output.jpg"

"""Setting the model to tiny yolov3 and loading the weights from the specified path"""

det.setModelTypeAsTinyYOLOv3()
det.setModelPath(model_path)
det.loadModel()

"""Detecting objects from the image and displaying the label if the prediction has minimum 0.1 probability."""

detection = det.detectObjectsFromImage(input_image=input_path, output_image_path=output_path,minimum_percentage_probability=0.1)

"""Result: Input and output image"""

i1 = cv2.imread("input.jpg")
cv2.imshow(i1)
i2 = cv2.imread("prediction_output.jpg")
cv2.imshow(i2)

"""Total objects detected"""

print("Enter object name to get the box location")
print("Available options are:")
count = 1
for i in detection:
  print(count,') ', i['name'])
  count+=1

"""Display requested object box dimensions"""

z = input()
for i in detection:
  if(i['name']==z):
    boxpix = i['box_points']
print("Top-left corner: (X1, Y1) = ({}, {})".format(boxpix[0],boxpix[1]))
print("Bottom-right corner: (X2, Y2) = ({}, {})".format(boxpix[2],boxpix[3]))

"""Display requested object"""

selectedobj = cv2.imread("input.jpg")[boxpix[1]:boxpix[3],boxpix[0]:boxpix[2]]
cv2.imshow(selectedobj)
