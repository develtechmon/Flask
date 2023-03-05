from flask import Flask, render_template, request
import RPi.GPIO as GPIO

app = Flask(__name__)

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

led_pin = 21
GPIO.setup(led_pin, GPIO.OUT)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        led_status = request.form['led_status']
        if led_status == 'on':
            GPIO.output(led_pin, GPIO.HIGH)
        elif led_status == 'off':
            GPIO.output(led_pin, GPIO.LOW)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)