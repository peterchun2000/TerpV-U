from flask import Flask, request, render_template, redirect, url_for, session, send_file
from flask_bootstrap import Bootstrap
from multiTracker import begin_tracking
		
app = Flask(__name__)
		
bootstrap  = Bootstrap(app)

'''
@app.route('/')
def index():
    return 'Hello Flask!'
'''

@app.route('/')
def main_page():
    return render_template('Test.html')

@app.route('/', methods=["POST"])
def record():
    if request.form.get('record') == "Record":
        html_table = begin_tracking()
        return render_template('Test.html', table = html_table)

if __name__ == '__main__':
    app.run(debug=True)
