from flask import Flask, render_template, request, session, redirect, url_for
import mysql.connector
from flask_bcrypt import Bcrypt, check_password_hash
import secrets
import os
from datetime import timedelta
from werkzeug.utils import secure_filename

app = Flask(__name__)

app.config['SECRET_KEY'] = secrets.token_hex(16)
app.config['UPLOAD_FOLDER'] =  "static\images"
# app.config['UPLOAD_FOLDER'] = 'path/to/upload/folder'
app.permanent_session_lifetime = timedelta(minutes=30)

bcrypt = Bcrypt(app)

# Configuration de la base de données
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="vente_vehicules"
)
#route principale page d'accceuil
@app.route('/')
def main_index():
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM vehicule LIMIT 6")
    vehicules = cursor.fetchall()
    cursor.execute("SELECT * FROM vehicule WHERE categorie='Voiture electrique' ")
    electriques = cursor.fetchall()
    cursor.execute("SELECT * FROM vehicule WHERE categorie='Voitures de sport' ")
    sports = cursor.fetchall()
    cursor.close()
    return render_template("main_index.html",vehicules=vehicules,electriques=electriques)

#route pour la page acceuil de l'admin
@app.route('/index')
def index():
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM vehicule LIMIT 6")
    vehicules = cursor.fetchall()
    cursor.execute("SELECT * FROM vehicule WHERE categorie='Voiture electrique' ")
    electriques = cursor.fetchall()
    cursor.execute("SELECT * FROM vehicule WHERE categorie='Voitures de sport' ")
    sports = cursor.fetchall()
    cursor.close()
    
    return render_template('index.html', vehicules=vehicules,electriques=electriques,sports=sports)
#route pour la page d'acceuil pour le client
@app.route('/user_index')
def user_index():
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM vehicule LIMIT 6")
    vehicules = cursor.fetchall()
    cursor.execute("SELECT * FROM vehicule WHERE categorie='Voiture electrique' ")
    electriques = cursor.fetchall()
    cursor.execute("SELECT * FROM vehicule WHERE categorie='Voitures de sport' ")
    sports = cursor.fetchall()
    cursor.close()
    
    return render_template("user_index.html",vehicules=vehicules,electriques=electriques,sports=sports)
#route pour la page liste de vehicule admin
@app.route('/liste_vehicule')
def liste_vehicule():
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM vehicule")
    vehicules = cursor.fetchall()
    return render_template("liste_vehicule.html", vehicules=vehicules)
#route pour la page liste de vehicule pour client
@app.route('/liste_vehicule_client')
def liste_vehicule_client():
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM vehicule")
    vehicules = cursor.fetchall()
    return render_template("liste_vehicule_client.html",vehicules=vehicules)
#route pour la page utilisateur
@app.route('/utilisateur')
def utilisateur():
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM utilisateur")
    users = cursor.fetchall()
    
    return render_template("utilisateur.html",users=users)

@app.route('/ajouter', methods=['GET', 'POST'])
def ajouter():
    if request.method == 'POST':
        couleur = request.form['couleur']
        modele = request.form['modele']
        marque = request.form['marque']
        prix = request.form['prix']
        age = request.form['age']
        categorie = request.form['categorie']
        kilometrage = request.form['kilometrage']
        description = request.form['description']
        photo = request.files['photo']
        
        if not all([couleur, modele, marque, prix, age, categorie, kilometrage, description, photo]):
            return "Tous les champs sont obligatoires", 400
        
        if photo:
            filename = secure_filename(photo.filename)
            # if not os.path.exists(app.config['UPLOAD_FOLDER']):
            #     os.makedirs(app.config['UPLOAD_FOLDER'])
            
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            try:
                photo.save(filepath)
                cursor = db.cursor()
                cursor.execute(
                    "INSERT INTO vehicule (couleur, modele, marque, prix, age, categorie, kilometrage, photo, description) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)",
                    (couleur, modele, marque, prix, age, categorie, kilometrage, filename, description)
                )
                db.commit()
            except Exception as e:
                db.rollback()
                return str(e), 500

        return redirect(url_for('index'))
    return render_template('ajouter.html')


#route pour l'enregistrement d'un utiisateur
@app.route('/ajouter_user',methods=['GET','POST'])
def ajouter_user():
    if request.method == 'POST':
        name = request.form['nom']
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        role = request.form['role']
        hashPwd = bcrypt.generate_password_hash(password).decode('utf-8')
        
        cursor = db.cursor()
        rows = cursor.execute("INSERT INTO utilisateur (name, username, password, email, role ) VALUES (%s, %s, %s, %s, %s)", (name, username, hashPwd, email, role))
        db.commit()
        message = ''
        if rows == 1:
            message = "Echec d'enregistrement!!!"
            return render_template("form_utilisateur.html",message=message)
        else:
            message = "Enregistrement avec succees!!!"
            return redirect(url_for("utilisateur",message=message))
    return render_template("form_utilisateur.html")

#route pour la creation d'un compte client
@app.route('/ajouter_client',methods=['GET','POST'])
def ajouter_client():
    if request.method == 'POST':
        name = request.form['nom']
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        hashPwd = bcrypt.generate_password_hash(password).decode('utf-8')
        
        cursor = db.cursor()
        rows = cursor.execute("INSERT INTO utilisateur (name, username, password, email, role ) VALUES (%s, %s, %s, %s, %s)", (name, username, hashPwd, email, 'client'))
        db.commit()
        message = ''
        if rows == 1:
            message = "Echec d'enregistrement!!!"
            return render_template("form_client.html",message=message)
        else:
            message = "Enregistrement avec succees!!!Complez ce formulaire pour vous connectez!"
            return redirect(url_for("login",message=message))
    return render_template("form_client.html")

@app.route('/modifier/<int:id>', methods=['GET', 'POST'])
def modifier(id):
    cursor = db.cursor(dictionary=True)
    if request.method == 'POST':
        couleur = request.form['couleur']
        modele = request.form['modele']
        marque = request.form['marque']
        prix = request.form['prix']
        age = request.form['age']
        categorie = request.form['categorie']
        kilometrage = request.form['kilometrage']
        description = request.form['description']
        photo = request.files['photo']
        if photo:
            filename = photo.filename
            filepath = os.path.abspath(app.config['UPLOAD_FOLDER'], filename)
            photo.save(filepath)
            cursor.execute("""
            UPDATE vehicule
            SET couleur=%s, modele=%s, marque=%s, prix=%s, age=%s, categorie=%s, kilometrage=%s, photo=%s, description=%s
            WHERE id=%s
        """, (couleur, modele, marque, prix, age, categorie, kilometrage, filename, description, id))
            db.commit()
        return redirect(url_for('index'))
    else:
        cursor.execute("SELECT * FROM vehicule WHERE id=%s", (id,))
        vehicule = cursor.fetchone()
        return render_template('modifier.html', vehicule=vehicule)

#route pour la modification de l'utilisateur
@app.route('/modifier_user/<int:id>',methods=['GET','POST'])
def modifier_user(id):
    cursor = db.cursor(dictionary=True)
    if request.method == 'POST':
        name = request.form['nom']
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        role = request.form['role']
        cursor.execute("""
            UPDATE utilisateur
            SET name=%s, username=%s, password=%s, email=%s, role=%s 
            WHERE id=%s
        """, (name, username, password, email, role, id))
        db.commit()
        return redirect(url_for('utilisateur'))
    else :
        cursor.execute("SELECT * FROM utilisateur WHERE id=%s",(id,))
        users = cursor.fetchone()
        return render_template("form_modif_utilisateur.html",users=users)

#route pour acheter les vehicules
@app.route('/acheter/<int:id>', methods=['POST', 'GET'])
def acheter(id):
    cursor = db.cursor(dictionary=True)
    if request.method == 'POST':
        id = request.form['id_vehicule']
        
        date = request.form['date']
        quantite = request.form['quantite']
        mode_paiement = request.form['mode_paiement']
        cursor.execute("INSERT INTO commande (id_panier, quantite, dates, mode_paiement) VALUES (%s, %s, %s, %s)", (id, quantite, date, mode_paiement))
        db.commit()
        
        return redirect(url_for('liste_achat',id=id,message="Achat effectué"))
    else:
        cursor.execute("""
        SELECT panier.id as id, vehicule.couleur as couleur, vehicule.modele as modele, vehicule.marque as marque, vehicule.prix, vehicule.categorie as categorie, vehicule.photo as photo, vehicule.description as description, vehicule.age as age, vehicule.kilometrage as kilometrage, utilisateur.id as id_user, utilisateur.name as name, vehicule.id as id_vehicule 
        FROM vehicule 
        JOIN panier ON vehicule.id = panier.id_vehicule 
        JOIN utilisateur ON panier.id_utilisateur = utilisateur.id 
        WHERE panier.id = %s
        """, (id,))
        commandes = cursor.fetchone()
        return render_template("form_acheter.html", vehicule=commandes, message="Echec d'acheter")

    
@app.route('/form_acheter/<int:id>')
def form_acheter(id):
    cursor = db.cursor(dictionary=True)
    cursor.execute("""
        SELECT panier.id as id, vehicule.couleur as couleur,vehicule.modele as modele,vehicule.marque as marque,vehicule.prix,vehicule.categorie as categorie,vehicule.photo as photo,vehicule.description as description,vehicule.age as age,vehicule.kilometrage as kilometrage,utilisateur.id as id_user,utilisateur.name as name,vehicule.id as id_vehicule FROM vehicule JOIN panier ON vehicule.id = panier.id_vehicule JOIN utilisateur ON panier.id_utilisateur=utilisateur.id WHERE panier.id=%s
    """,(id,))
    vehicule =cursor.fetchone()
    return render_template("form_acheter.html",vehicule=vehicule,id=id)
@app.route('/liste_achat')
def liste_achat():
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT p.id, c.quantite, c.mode_paiement, c.dates, v.couleur, v.modele, v.marque, v.prix, v.categorie, v.photo, v.description, v.age, v.kilometrage FROM panier p JOIN vehicule v ON p.id_vehicule = v.id JOIN commande c ON c.id_panier = p.id")
    commandes = cursor.fetchall()
    # prix_total = (commande['prix'] * commande['quantite'] for commande in commandes)
    return render_template("liste_achat.html",commandes=commandes)
@app.route('/supprimer_achat/<int:id>',methods=['POST'])
def supprimer_achat(id):
    cursor = db.cursor()
    cursor.execute("DELETE FROM commande WHERE id = %s",(id,))
    db.commit()
    return redirect(url_for('liste_achat'))

@app.route('/supprimer/<int:id>', methods=['POST'])
def supprimer(id):
    cursor = db.cursor()
    cursor.execute("DELETE FROM vehicule WHERE id=%s", (id,))
    db.commit()
    return redirect(url_for('index'))

#route pour la suppression utilisateur
@app.route('/supprimer_user/<int:id>',methods=['POST'])
def supprimer_user(id):
    cursor = db.cursor()
    rows=cursor.execute("DELETE FROM utilisateur WHERE id = %s",(id,))
    db.commit()
    message = ''
    if rows == 1:
        message = 'Suppression avec succes!!!'
        return redirect(url_for('utilisateur',message=message))
    else :
        message='Echec de suppression!!!'
        return redirect(url_for('utilisateur',message=message))

@app.route('/ajouter_au_panier/<int:id>', methods=['POST'])
def ajouter_au_panier(id):
    id_user = session.get('id')
    role = session.get('role')
    if id_user is None or role is None:
        return redirect(url_for('login'))  # Redirige vers la page de connexion si l'utilisateur n'est pas connecté
    
    
    cursor = db.cursor()
    cursor.execute("INSERT INTO panier (id_vehicule,id_utilisateur) VALUES (%s,%s)", (id,id_user))
    db.commit()
    if role == 'client':
        return redirect(url_for('panier_client'))
    else:
        return redirect(url_for('panier'))

@app.route('/panier')
def panier():
    cursor = db.cursor(dictionary=True)
    cursor.execute("""
        SELECT panier.id as id, vehicule.couleur as couleur,vehicule.modele as modele,vehicule.marque as marque,vehicule.prix,vehicule.categorie as categorie,vehicule.photo as photo,vehicule.description as description,vehicule.age as age,vehicule.kilometrage as kilometrage,utilisateur.id as id_user,utilisateur.name as name,vehicule.id as id_vehicule FROM vehicule JOIN panier ON vehicule.id = panier.id_vehicule JOIN utilisateur ON panier.id_utilisateur=utilisateur.id
    """)
    vehicules = cursor.fetchall()
    return render_template('panier.html', vehicules=vehicules)
#route pour la page panier du client
@app.route('/panier_client')
def panier_client():
    id = session.get("id")
    cursor = db.cursor(dictionary=True)
    cursor.execute("""
        SELECT panier.id as id, vehicule.couleur as couleur,vehicule.modele as modele,vehicule.marque as marque,vehicule.prix,vehicule.categorie as categorie,vehicule.photo as photo,vehicule.description as description,vehicule.age as age,vehicule.kilometrage as kilometrage,utilisateur.id as id_user,utilisateur.name as name,vehicule.id as id_vehicule FROM vehicule JOIN panier ON vehicule.id = panier.id_vehicule JOIN utilisateur ON panier.id_utilisateur=utilisateur.id
    WHERE utilisateur.id = %s""",(id,))
    vehicules = cursor.fetchall()
    #return [id]
    return render_template("panier_client.html", vehicules=vehicules)

@app.route('/supprimer_panier/<int:id>',methods=['POST','GET'])
def supprimer_panier(id):
    role=session.get('role')
    cursor=db.cursor()
    rows=cursor.execute("DELETE FROM panier WHERE id=%s",(id,))
    db.commit()
    
    if role == 'admin':
        message = 'Supprimer du panier avec succes'
        return redirect(url_for('panier',message=message))
    else:
        message = 'Supprimer du panier avec succes'
        return redirect(url_for('panier_client',message=message))
    
    
    



#route pour notre login
from flask import flash

from flask import flash

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        cursor = db.cursor(buffered=True)
        cursor.execute("SELECT * FROM utilisateur WHERE username=%s", (username,))
        user = cursor.fetchone()
        if user:
            try:
                pwdVerif = bcrypt.check_password_hash(user[2], password)
            except ValueError:
                flash('Erreur de hachage de mot de passe')
                return redirect(url_for('login'))
            if pwdVerif:
                if user[5] == 'admin':
                    session.permanent = True
                    session['logedin'] = True
                    session['id'] = user[0]
                    session['role'] = user[5]
                    id = session.get('id')
                    role = session.get('role')
                    flash('Bienvenu cher Admin')
                    return redirect(url_for('index',id=id,role=role))
                else:
                    session['id'] = user[0]
                    session['role'] = user[5]
                    session['logedin'] = True
                    id = session.get('id')
                    role = session.get('role')
                    flash('Bienvenu cher Client')
                    return redirect(url_for('user_index',id=id,role=role))
            else:
                flash('Echec de connexion')
                return redirect(url_for('login'))
        else:
            flash('Utilisateur non trouvé')
            return redirect(url_for('login'))
    return render_template("login.html")



#route pour le logout 
@app.route('/logout')
def logout():
    session.clear()
    return render_template("login.html")


@app.route('/recherche', methods=['GET'])
def recherche():
    query = request.args.get('query')
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM vehicules WHERE marque LIKE %s OR modele LIKE %s", (f'%{query}%', f'%{query}%'))
    vehicules = cursor.fetchall()
    return render_template('index.html', vehicules=vehicules)


if __name__ == '__main__':
    app.run(debug=True)
