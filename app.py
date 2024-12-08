from flask import Flask, render_template

app = Flask(__name__)

JOBS = [
    {
        'id': 1,
        'title': 'Data Analyst',
        'location': 'Bengluru, India',
        'salary': '10,00,000',
        'currency': '₹'
    },
    {
        'id': 2,
        'title': 'Data Scientist',
        'location': 'Hyderabad, India',
        'salary': '12,00,000',
        'currency': '₹'
    },
    {
        'id': 3,
        'title': 'Frontend Engineer',
        'location': 'San Franscisco, USA',
        'salary': '120,000',
        'currency': '$'
    },
    {
        'id': 4,
        'title': 'AI Engineer',
        'location': 'Pune, India',
        'salary': '8,00,000',
        'currency': '₹'
    },
]

@app.route('/')
def home():
    return render_template('Home.html')

@app.route('/careers')
def careers():
    return render_template('Careers.html', jobs=JOBS)

@app.route('/contact')
def contact():
    return render_template('Contact.html')

@app.route('/about')
def about():
    return render_template('About.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

