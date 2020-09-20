from imageai.Detection import ObjectDetection
import os

execution_path = os.getcwd()

detector = ObjectDetection()
detector.setModelTypeAsYOLOv3()
detector.setModelPath("./models/yolo.h5")
print(detector.modelPath)
detector.loadModel()

custom = detector.CustomObjects(car=True, bus=True, motorcycle=True, truck=True)
detections = detector.detectCustomObjectsFromImage(
  custom_objects=custom,
  input_image="frame.jpg",
  output_image_path=os.path.join(execution_path , "result.jpg"),
  minimum_percentage_probability=30
)

for eachObject in detections:
  print(eachObject["name"] , " : ", eachObject["percentage_probability"], " : ", eachObject["box_points"] )