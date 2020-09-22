# car-space
### Project structure:
1. *create_coordinates.py* - User clicks 4 corners for each spot they want tracked. Presses 'q' when all desired spots are marked, after that new .yml file with coordinates will be created.
- *--image* - path to the image, on which you will be able to set spots.
- *--data* - path to .yml file, that will be created after script execution.
```bash
python create_coordinates.py --image images/another_one.png --data data/chornovola.yml
```

2. *main.py* - start park spots recognition.
- *--data* - path to .yml, that contains coordinates of park spots.
- *--start-frame* - the frame from which the video should start. (not mandatory)
```bash
python main.py --data data/chornovola.yml --start-frame 400
```

3. *colors.py*, *motion_detector.py*, *drawing_utils.py*, *coordinates_generator.py* - auxiliary files.