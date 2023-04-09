from flask import Flask, render_template, request, url_for
import psycopg2

app = Flask('carlamaria')
# multiple route goes to the same page

image_file = 'image3.jpeg'

conn = psycopg2.connect(
        host='localhost',
        database='stiri',
        user='postgres',
        password='Alina1987')


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', image_file=image_file, message='Ce frumos este acest loc!')


@app.route('/newss')
def show_newss():
    """Afiseaza toate stirile"""

    with conn:
        query = "SELECT * FROM news"
        c = conn.cursor()
        c.execute(query)
        records = c.fetchall()

    return render_template('newss.html', title='Stirile sunt:', newss=records)


@app.route('/search', methods=['GET', 'POST'])
def search_newss():
    """Cauta stiri cu un anumit titlu"""

    if request.method == 'POST':
        search = request.form['search']
    else:
        search = request.args.get('search')

    with conn:
        query = "SELECT * FROM news WHERE title LIKE %s"
        c = conn.cursor()
        c.execute(query, ['%' + search + '%'])
        records = c.fetchall()

    return render_template('search.html', title='Rezultatele cautarii:', newss=records, search=search)


@app.route('/acasa')
def acasa():
    return render_template('home.html')


@app.route('/despre_mine')
def despre_mine():
    return render_template('despre_mine.html')


@app.route('/galerie')
def galerie():
    return render_template('galerie.html')


@app.route('/contact')
def show_contact():
    return render_template('contact.html')


@app.route('/tips_and_tricks')
def tips_and_tricks():
    return render_template('tips_and_tricks.html')


@app.route('/beauty')
def beauty():
    return render_template('beauty.html')


@app.route('/calatorii')
def calatorii():
    return render_template('calatorii.html')


if __name__ == '__main__':
    # run in debug mode; no need to restart on changes
    app.run(debug=True)