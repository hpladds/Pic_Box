This software controls a "Picture_Box" that uses a Pi Camera Module V2, a stepper motor and a NeoPixel ring light to take pictures of a single piece of lego from several different angles. It is useful in creating a database of images, perhaps for an AI project that classifies lego.

This project is comprised of three python 3 scripts (Neo_Fill.py, picamera_time.py and stepper_code.py) and one bash script (bash_sync.sh).

"Neo_Fill.py" controls the NeoPixel ring lights; check Adafruit for configuration instuctions.
"picamera_time.py" controls the Pi Camera module v2.
"stepper_code.py" controls the movement of the stepper motor.

The "bash_sync.sh" script calls all three python scripts. I believe this creates three simultaneously running processes with each process running one of the scripts. This allows me to klugily avoid the more difficult process of writing one python script with multi-processing/threading. 
