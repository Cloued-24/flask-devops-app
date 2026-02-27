from flask import current_app
import socket
import os

from __init__ import app

@app.route('/')
@app.route('/index')
def index():
    hostname = socket.gethostname()
    environment = os.getenv('FLASK_ENV', 'production')
    return f"""
    <html>
        <head>
            <title>DevOps Project 1</title>
            <style>
                body {{ font-family: Arial, sans-serif; margin: 40px; }}
                .container {{ max-width: 800px; margin: 0 auto; }}
                .info {{ background: #f0f0f0; padding: 20px; border-radius: 5px; }}
            </style>
        </head>
        <body>
            <div class="container">
                <h1>🚀 Hello DevOps!</h1>
                <div class="info">
                    <h2>Container Information:</h2>
                    <p><strong>Hostname:</strong> {hostname}</p>
                    <p><strong>Environment:</strong> {environment}</p>
                    <p><strong>Containerized:</strong> Yes! This app is running in Docker.</p>
                </div>
            </div>
        </body>
    </html>
    """
