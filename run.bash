python3 recognition/camera_recognition.py --name "Chornovola st 93" --camera http://vs7.videoprobki.com.ua/streams/cam673stream_ &
P1=$!
python3 bot/main.py &
P2=$!

wait $P1 $P2