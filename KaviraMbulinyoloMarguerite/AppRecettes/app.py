from flask import Flask, render_template, request, session, redirect, url_for, flash
import mysql.connector
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin, current_user, login_user, logout_user, login_required
from datetime import datetime  
from flask_bcrypt import Bcrypt

import hashlib

app = Flask(__name__)
app.secret_key = 'votre_cle_secrete'
bcrypt = Bcrypt(app)

#Configuration de la base de données
db_config = {
    'user': 'root',
    'password': '',
    'host': 'localhost',
    'database': 'gestion_recette'
}
db = mysql.connector.connect(**db_config)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'connexion'

class User(UserMixin):
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

@login_manager.user_loader
def load_user(user_id):
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM user WHERE id=%s", (user_id,))
    user = cursor.fetchone()
    if user:
        return User(user['id'], user['username'], user['password'])
    return None

depenses=[]

@app.route('/')
def home():
    #if current_user.is_authenticated:
     #   return redirect(url_for('index'))
    return render_template('connexion.html')

@app.route('/index')
@login_required
def index():
    req = "SELECT * FROM transaction  WHERE user_id=%s"
    cursor = db.cursor()
    val=(current_user.id,)
    cursor.execute(req, val)
    transactions = cursor.fetchall()
    return render_template('index.html',transactions=transactions, utilisateur=current_user.username)

@app.route('/ajouter', methods=['GET', 'POST'])
@login_required
def ajouter():
    if request.method == 'POST':
        description = request.form['description']
        montant = request.form['montant']
        type_depense = request.form['type']
        date = datetime.now()
       
        # Récupérer l'id de la catégorie
        cursor = db.cursor(dictionary=True)
        cursor.execute("SELECT id FROM category WHERE name=%s", (description,))
        category = cursor.fetchone()
        category_id = category['id'] if category else None

        cursor = db.cursor(dictionary=True)
        
          # Insérer la transaction dans la base de données
        cursor.execute("INSERT INTO transaction (user_id, amount, type,description , date) VALUES (%s, %s, %s, %s, %s)", 
                       (current_user.id, montant, type_depense, description, date))
        db.commit()
        cursor.close()
        flash('Dépense ajoutée avec succès!')
        return redirect(url_for('index'))
    return render_template('ajouter.html', utilisateur=current_user.username)

@app.route('/rapport')
@login_required
def rapport():
    cursor = db.cursor(dictionary=True)
    cursor.execute("""
        SELECT category.name, SUM(transaction.amount) as total
        FROM transaction
        JOIN category ON transaction.description = description
        WHERE transaction.user_id = %s
        GROUP BY category.name
    """, (current_user.id,))
    rapport = cursor.fetchall()
    return render_template('rapport.html', rapport=rapport, utilisateur=current_user.username)

@app.route('/connexion', methods=['GET','POST'])
def connexion():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        cursor = db.cursor(dictionary=True)
        cursor.execute("SELECT * FROM user WHERE username=%s",(username,))
        user = cursor.fetchone()
        if user and bcrypt.check_password_hash(user['password'], password):
            user_obj = User(user['id'], user['username'], user['password'])
            login_user(user_obj)
            return redirect(url_for('index'))
        else:
            flash('Nom d\'utilisateur ou mot de passe incorrect')
    
    return render_template('connexion.html')

@app.route('/inscription', methods=['GET', 'POST'])
def inscription():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        confirmer_password = request.form['confirmer_password']
        
        if password == confirmer_password:
            hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
            cursor = db.cursor()
            cursor.execute("INSERT INTO user (username,  password) VALUES (%s, %s)", (username,  hashed_password))
            db.commit()
            cursor.close()
            flash('Inscription réussie! Vous pouvez maintenant vous connecter.')
            return redirect(url_for('connexion'))
        else:
            flash('Les mots de passe ne correspondent pas.')
    return render_template('inscription.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route('/transactions')
def transactions():
    return render_template('transactions.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        cursor = db.cursor(dictionary=True)
        cursor.execute("SELECT * FROM user WHERE username=%s", (username,))
        user = cursor.fetchone()
        
        if user and check_password_hash(user['password'], password):
            session['username_id'] = user['id']
            return redirect(url_for('index'))
        else:
            flash('Nom d\'utilisateur ou mot de passe incorrect')
    
    return render_template('connexion.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        confirmer_password = request.form['confirmer_password']

        if password == confirmer_password:
            hashed_password = generate_password_hash(password, method='sha256')
            conn = mysql.connector.connect(**db_config)
            cursor = conn.cursor()
            cursor.execute("INSERT INTO user (username, password) VALUES (%s, %s)", (username, hashed_password))
            conn.commit()
            cursor.close()
            conn.close()
            return redirect(url_for('connexion'))
        else:
            flash('Les mots de passe ne correspondent pas.')
    
    return render_template('inscription.html')
    
@app.route('/deconnexion')
def deconnexion():
    session.pop('user_id', None)
    return render_template('connexion.html')
    #return redirect(url_for('connexion'))

@app.route('/success')
def success():
    return "Connexion réussie !"

@app.route('/parametres')
def parametres():
    return render_template('parametres.html')


@app.route('/supprimer/<int:id>')
def supprimer(id):
    global depenses
    depenses = [depense for depense in depenses if depense['id'] != id]
    flash('Dépense supprimée avec succès!', 'success')
    return redirect(url_for('index'))

if __name__ == '__main__':
 app.run(debug=True)
