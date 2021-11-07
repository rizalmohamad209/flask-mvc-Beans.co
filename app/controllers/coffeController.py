from app import app
from flask import render_template


@app.route('/coffe', methods=['GET'])
def coffe():
    return render_template('coffe.html')
