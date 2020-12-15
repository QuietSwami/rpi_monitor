#!/usr/bin/python3

"""
RPi Monitor API/Webserver
"""

from flask import Flask, render_template, jsonify
from utilities import cpu_clock, cpu_temp, mem_usage, storage

app = Flask(__name__)


header = {
    "Access-Control-Allow-Origin": "http://localhost:8080"
}

@app.route('/cpu-clock')
def cpu_clock_endpoint():
    """
    Returns current CPU Clock Speed
    """
    return jsonify(cpu_clock())

@app.route('/cpu-temp')
def cpu_temp_endpoint():
    """
    Returns current CPU temp
    """
    return jsonify(cpu_temp())

# Memory Information

@app.route('/mem-usage')
def mem_usage_endpoint():
    """
    Returns current memory usage
    """
    return jsonify(mem_usage())

# Storage Information

@app.route('/storage-information')
def storage_information_endpoint():
    """
    Returns current storage information
    """
    return jsonify(storage())

@app.route("/")
def serve_web_interface():
    """
    Serves RPi Monitor's web interface
    """
    return render_template("index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port='8080')
