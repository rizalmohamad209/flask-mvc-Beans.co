from app import app
from flask import render_template
# from app.models.user import User  # import kelas User dari model


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')
