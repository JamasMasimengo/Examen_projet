from flask import Flask, render_template, request, redirect, url_for, session, flash
import MySQLdb
from flask_mail import Mail, Message
from werkzeug.security import generate_password_hash, check_password_hash
import secrets
from flask_bcrypt import Bcrypt

# Initialisation de l'application Flask
app = Flask(__name__)
bcrypt = Bcrypt(app)
app.config['SECRET_KEY'] = secrets.token_hex(16)

# Configuration de la base de données MySQL
def connect_db():
    return MySQLdb.connect(
        host="localhost",
        user="root",
        passwd="",
        db="vol_db"
    )

# Configuration de Flask-Mail pour l'envoi d'emails
app.config['MAIL_SERVER'] = 'smtp.example.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = 'your-email@example.com'
app.config['MAIL_PASSWORD'] = 'your-email-password'
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False

mail = Mail(app)

@app.route('/')
def lancerAcceuil():
     return render_template('acceuil.html')

# Route pour la page d'inscription
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

        conn = connect_db()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM users WHERE email = %s", (email,))
        user = cursor.fetchone()

        if user:
            flash('Cet email est déjà enregistré.')
        else:
            query = "INSERT INTO users (username, email, password) VALUES (%s, %s, %s)"
            cursor.execute(query, (username, email, hashed_password))
            conn.commit()

            flash('Inscription réussie. Veuillez vous connecter.')
            return redirect(url_for('Lancerlogin'))

        cursor.close()
        conn.close()

    return render_template('register.html')

@app.route('/logout')
def logout():
    session.clear()
    flash('Vous avez été déconnecté.')
    return redirect('/login')

# Route pour la page de connexion
@app.route('/login', methods=['GET', 'POST'])
def Lancerlogin():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        conn = connect_db()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM users WHERE email = %s", (email,))
        user = cursor.fetchone()

        cursor.close()
        conn.close()

        if user and bcrypt.check_password_hash(user[3], password):
            session['user_id'] = user[0]
            session['username'] = user[1]
            flash('Connexion réussie.')
            return redirect('/book')
        else:
            flash('Email ou mot de passe incorrect.')

    return render_template('login.html')




@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        flash('Veuillez vous connecter.')
        return redirect(url_for('Lancerlogin'))

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT r.id, u.username, f.route, r.reservation_date FROM reservations r JOIN users u ON r.user_id = u.id JOIN flights f ON r.flight_id = f.id")
    reservations = cursor.fetchall()

    cursor.execute("SELECT p.id, u.username, f.route, p.amount, p.payment_date FROM payments p JOIN reservations r ON p.reservation_id = r.id JOIN users u ON r.user_id = u.id JOIN flights f ON r.flight_id = f.id")
    payments = cursor.fetchall()

    cursor.close()
    conn.close()

    return render_template('admin.html', reservations=reservations, payments=payments)


@app.route('/book', methods=['GET', 'POST'])
def book():
    if 'user_id' not in session:
        flash('Veuillez vous connecter.')
        return redirect(url_for('Lancerlogin'))

    if request.method == 'POST':
        flight_id = request.form['flight_id']
        user_id = session['user_id']

        conn = connect_db()
        cursor = conn.cursor()

        query = "INSERT INTO reservations (user_id, flight_id) VALUES (%s, %s)"
        cursor.execute(query, (user_id, flight_id))
        conn.commit()

        cursor.close()
        conn.close()

        flash('Réservation réussie.')
        return redirect('/payments')

    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT id, route, price FROM flights")
    flights = cursor.fetchall()
    cursor.close()
    conn.close()

    return render_template('book.html', flights=flights)

@app.route('/reservations')
def reservations():
    if 'user_id' not in session:
        flash('Veuillez vous connecter.')
        return redirect(url_for('Lancerlogin'))

    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT r.id, f.route, r.reservation_date FROM reservations r JOIN flights f ON r.flight_id = f.id WHERE r.user_id = %s", (session['user_id'],))
    reservations = cursor.fetchall()
    cursor.close()
    conn.close()

    return render_template('reservations.html', reservations=reservations)

@app.route('/payments', methods=['GET', 'POST'])
def payments():
    if request.method == 'POST':
        reservation_id = request.form['reservation_id']
        amount = request.form['amount']

        conn = connect_db()
        cursor = conn.cursor()

        query = "INSERT INTO payments (reservation_id, amount) VALUES (%s, %s)"
        cursor.execute(query, (reservation_id, amount))
        conn.commit()

        cursor.close()
        conn.close()

        flash('Paiement réussi.')
        return redirect(url_for('payments'))

    if 'user_id' not in session:
        flash('Veuillez vous connecter.')
        return redirect(url_for('Lancerlogin'))

    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT p.id, r.id, p.amount, p.payment_date FROM payments p JOIN reservations r ON p.reservation_id = r.id WHERE r.user_id = %s", (session['user_id'],))
    payments = cursor.fetchall()
    cursor.close()
    conn.close()

    return render_template('payments.html', payments=payments)

@app.route('/manage_reservations')
def manage_reservations():
    if 'user_id' not in session:
        flash('Veuillez vous connecter.')
        return redirect(url_for('Lancerlogin'))

    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT r.id, u.username, f.route, r.reservation_date FROM reservations r JOIN users u ON r.user_id = u.id JOIN flights f ON r.flight_id = f.id")
    reservations = cursor.fetchall()
    cursor.close()
    conn.close()

    return render_template('manage_reservations.html', reservations=reservations)

@app.route('/manage_payments')
def manage_payments():
    if 'user_id' not in session:
        flash('Veuillez vous connecter.')
        return redirect(url_for('Lancerlogin'))

    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT p.id, u.username, f.route, p.amount, p.payment_date FROM payments p JOIN reservations r ON p.reservation_id = r.id JOIN users u ON r.user_id = u.id JOIN flights f ON r.flight_id = f.id")
    payments = cursor.fetchall()
    cursor.close()
    conn.close()

    return render_template('manage_payments.html', payments=payments)

if __name__ == '__main__':
    app.run(debug=True)
