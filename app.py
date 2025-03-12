from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)
DATABASE = 'tennis.db'

# Helper function to connect to the database
def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

# Route for the homepage
@app.route('/')
def index():
    return render_template('index.html')

# Route to display all matches
@app.route('/matches')
def matches():
    conn = get_db_connection()
    matches = conn.execute('SELECT * FROM matches').fetchall()
    conn.close()
    return render_template('matches.html', matches=matches)

# Route to add a new match
@app.route('/add_match', methods=['GET', 'POST'])
def add_match():
    if request.method == 'POST':
        team1 = request.form['team1']
        team2 = request.form['team2']
        date = request.form['date']

        conn = get_db_connection()
        conn.execute('INSERT INTO matches (team1, team2, date) VALUES (?, ?, ?)', (team1, team2, date))
        conn.commit()
        conn.close()

        return redirect(url_for('matches'))

    return render_template('add_match.html')

# Route to update match results
@app.route('/results', methods=['GET', 'POST'])
def results():
    if request.method == 'POST':
        match_id = request.form['match_id']
        winner = request.form['winner']

        conn = get_db_connection()
        conn.execute('UPDATE matches SET winner = ? WHERE id = ?', (winner, match_id))
        conn.commit()
        conn.close()

        return redirect(url_for('matches'))

    conn = get_db_connection()
    matches = conn.execute('SELECT * FROM matches WHERE winner IS NULL').fetchall()
    conn.close()

    return render_template('results.html', matches=matches)

if __name__ == '__main__':
    app.run(debug=True)
