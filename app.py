from email.mime import application
from flask import Flask, render_template, jsonify, request
from database import add_application_to_db, load_job_from_db, load_jobs_from_db

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

@app.route('/job/<id>')
def job_details(id):
    job = load_job_from_db(id)
    if not job:
        return "<h1>Job Not Found</h1>", 404
    return render_template('Job_Details.html', job_detail = job)

@app.route('/job/<id>/apply', methods=['post'])
def apply_to_job(id):
    data = request.form
    job_detail = load_job_from_db(id)
    add_application_to_db(id, data)
    # Store this in DB
    # Send an email
    # display an acknowledgement
    return render_template('Application_submitted.html', application=data, job=job_detail)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

