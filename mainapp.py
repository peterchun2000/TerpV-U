from flask import Flask, request, render_template, redirect, url_for, session, send_file
		
app = Flask(__name__)
		
@app.route('/')
def index():
    return 'Hello Flask!'

@app.route('/Website_src')
def main_page():
    return render_template('Test.html')
		
if __name__ == '__main__':
    app.run(debug=True)

