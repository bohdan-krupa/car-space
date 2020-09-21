from imageai.Detection import ObjectDetection
import os

execution_path = os.getcwd()

detector = ObjectDetection()
detector.setModelTypeAsYOLOv3()
detector.setModelPath('./models/yolo.h5')
detector.loadModel()

custom = detector.CustomObjects(car=True, bus=True, motorcycle=True, truck=True)

def recognite_cars(parking_id):
  detections = detector.detectCustomObjectsFromImage(
    custom_objects=custom,
    input_image=f'input{parking_id}.jpg',
    output_image_path=os.path.join(execution_path , f'result{parking_id}.jpg'),
    minimum_percentage_probability=30
  )

  for eachObject in detections:
    print(f"{eachObject['name']} {round(eachObject['percentage_probability'])}% {eachObject['box_points']}")