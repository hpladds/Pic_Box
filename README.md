This project is comprised of three python 3 scripts (Neo_Fill.py, picamera_time.py and stepper_code.py) and one bash script (bash_sync.sh).

Neo_Fill.py controls the NeoPixel ring lights. Check Adafruit for configuration instuctions
picamera_time.py controls the Pi Camera module v2.
stepper_code.py controls the movement of the stepper motor.

The bash_sync.sh script calls all threeof the above python scripts. I believe this creates three simultaneously running processes. This allows me to klugily avoid the more difficult process of writing one python script with multi-processing/threading. 
