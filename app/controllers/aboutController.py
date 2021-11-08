from app import app
from flask import render_template


@app.route('/aboutme', methods=['GET'])
def about():
    return render_template('aboutme.html')
