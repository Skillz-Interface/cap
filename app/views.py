import os
from app import app
from flask import Flask,render_template

@app.route('/')
def home():
    """Render home page"""
    return render_template('index.html')
    
@app.route('/mission')
def mission():
    return render_template('mission.html')
@app.route('/team')
def team():
    return render_template(('team.html'))
    
if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port="8080")
