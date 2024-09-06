# app.py
from flask import Flask, jsonify, request
from flask_cors import CORS
import RPi.GPIO as GPIO

app = Flask(__name__)
CORS(app)

# Set up GPIO
LED_PIN = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)
GPIO.output(LED_PIN, GPIO.LOW)  # Start with the LED off

@app.route('/led', methods=['GET'])
def get_led_status():
    status = GPIO.input(LED_PIN) == GPIO.HIGH
    return jsonify({"status": status})

@app.route('/led/on', methods=['POST'])
def turn_on_led():
    GPIO.output(LED_PIN, GPIO.HIGH)
    return jsonify({"status": True})

@app.route('/led/off', methods=['POST'])
def turn_off_led():
    GPIO.output(LED_PIN, GPIO.LOW)
    return jsonify({"status": False})

@app.route('/led/toggle', methods=['POST'])
def toggle_led():
    current_status = GPIO.input(LED_PIN)
    GPIO.output(LED_PIN, not current_status)
    return jsonify({"status": GPIO.input(LED_PIN) == GPIO.HIGH})

if __name__ == '__main__':
    try:
        app.run(host='0.0.0.0', port=5000)
    finally:
        GPIO.cleanup()  # Cleanup GPIO on exit

