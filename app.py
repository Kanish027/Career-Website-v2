from flask import Flask, render_template
from database import load_jobs_from_db

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('Home.html')

@app.route('/careers')
def careers():
    job_list = load_jobs_from_db()
    return render_template('Careers.html', jobs=job_list)

@app.route('/contact')
def contact():
    return render_template('Contact.html')

@app.route('/about')
def about():
    return render_template('About.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

