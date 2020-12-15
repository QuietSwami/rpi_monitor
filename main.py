#!/usr/bin/python3

"""
RPi Monitor API/Webserver
"""

from flask import Flask, render_template, Response
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
    resp = Response(cpu_clock)
    resp.headers = header
    return resp

@app.route('/cpu-temp')
def cpu_temp_endpoint():
    """
    Returns current CPU temp
    """
    resp = Response(cpu_temp())
    resp.headers = header
    return resp

# Memory Information

@app.route('/mem-usage')
def mem_usage_endpoint():
    """
    Returns current memory usage
    """
    resp = Response(mem_usage)
    resp.headers = header
    return resp

# Storage Information

@app.route('/storage-information')
def storage_information_endpoint():
    """
    Returns current storage information
    """
    resp = Response(storage)
    resp.headers = header
    return resp

@app.route("/")
def serve_web_interface():
    """
    Serves RPi Monitor's web interface
    """
    return render_template("index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port='8080')
