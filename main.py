from imageai.Detection import ObjectDetection
import os

execution_path = os.getcwd()

detector = ObjectDetection()
# detector.setModelTypeAsTinyYOLOv3()
detector.setModelTypeAsYOLOv3()
detector.setModelPath("./models/yolo.h5")
print(detector.modelPath)
detector.loadModel()
detections = detector.detectObjectsFromImage(
  input_image="frame.jpg",
  output_image_path=os.path.join(execution_path , "result.jpg"),
  minimum_percentage_probability=30
)

for eachObject in detections:
  print(eachObject["name"] , " : ", eachObject["percentage_probability"], " : ", eachObject["box_points"] )