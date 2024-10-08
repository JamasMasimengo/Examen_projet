from flask import Flask,render_template,request,redirect,request, session, redirect,flash, url_for, jsonify

import mysql.connector
from datetime import datetime



#nous creeons l'instance de la classe Flask a executer pour chaque route
app=Flask(__name__)
app.secret_key = 'votre_cle_secrete'


bd=mysql.connector.connect(
    host='localhost',
    database='transfert_fonds',
    username='root',
    
    
    password=''
)

@app.route("/index")
def index():
    
    return render_template('index.html')

@app.route("/index1")
def index1():
    
    return render_template('index1.html')

#  differentes routes pour les devises 
@app.route('/devise')
def devise():
    req = "SELECT * FROM devise"
    curseur = bd.cursor(buffered=True)
    curseur.execute(req)
    devise = curseur.fetchall()
    curseur.close()
    return render_template('devise.html',devise=devise)

@app.route('/add_devise',methods=['POST','GET'])
def add_devise():
    if request.method == 'POST':
        requete = 'INSERT INTO devise (description) VALUES (%s)'
        description = request.form['description']
        valeurs = (description,)
        curseur = bd.cursor()
        curseur.execute(requete, valeurs)
        bd.commit()
        return redirect('/devise')
    
@app.route("/ajoutDevise")
def Form_AjoutDevise():
    return render_template('ajoutDevise.html')

@app.route("/delete_Devise/<id>")
def delete_Devise(id):
    req = ('DELETE from devise WHERE id=%s')
    valeur = (id,)
    curseur = bd.cursor()
    curseur.execute(req,valeur)
    return redirect('/devise')

@app.route("/modifier_Devise/<id>",methods=['POST','GET'])
def modifier_Devise(id):
    if request.method == 'POST':
        
     req = ('UPDATE devise SET description=%s WHERE id=%s')
     description = request.form['description']
     valeur = (description,id)
     curseur = bd.cursor()
     curseur.execute(req,valeur)
     return redirect('/devise')
 
 
@app.route('/lancer_mod_dev/<id>')
def lancer_mod_dev(id):
     req = "SELECT * FROM devise WHERE id=%s"
     valeur = (id,)
     curseur = bd.cursor()
     curseur.execute(req,valeur)
     
     donnees = curseur.fetchall()
     return render_template('modifierDevise.html',donnees=donnees)
 
    
# differentes routes pour le gestionnaire 
@app.route('/gestionnaire')
def gestionnaire():
    req= 'SELECT * FROM transactions'
    req1 = "SELECT gestionnaires.id,gestionnaires.idTrans,gestionnaires.Nom,gestionnaires.Prenom,gestionnaires.telephone,gestionnaires.genre from gestionnaires JOIN transactions on transactions.id=gestionnaires.idTrans"
    curseur = bd.cursor(buffered=True)
    
    curseur.execute(req)
    transaction= curseur.fetchall()
    
    curseur.execute(req1)
    gestionnaire= curseur.fetchall()
    curseur.close()
    return render_template('gestionnaire.html',transaction=transaction,gestionnaire=gestionnaire)

@app.route('/add_gestionnaire',methods=['POST','GET'])
def add_gestionnaire():
    if request.method == 'POST':
        requete ='INSERT INTO gestionnaires (idTrans,Nom,Prenom,telephone,genre) VALUES (%s,%s,%s,%s,%s)'
        idTrans = request.form['idTrans']
        Nom = request.form['Nom']
        Prenom = request.form['Prenom']
        telephone = request.form['telephone']
        genre = request.form['genre']
        valeurs = (idTrans,Nom,Prenom,telephone,genre)
        curseur = bd.cursor()
        curseur.execute(requete, valeurs)
        bd.commit()
        return redirect('/gestionnaire')
    
@app.route("/ajoutGestionnaire")
def Form_AjoutGestionnaire():
    req1 = "SELECT * from transactions"
    curseur = bd.cursor(buffered=True)
    curseur.execute(req1)
    transaction= curseur.fetchall()
    curseur.close()
    return render_template('ajoutGestionnaire.html',transaction=transaction)

@app.route("/delete_Gestionnaire/<id>")
def delete_Gestionnaire(id):
    req = ('DELETE from gestionnaires WHERE id=%s')
    valeur = (id,)
    curseur = bd.cursor()
    curseur.execute(req,valeur)
    return redirect('/gestionnaire')


@app.route("/modifier_Gestionnaire/<id>",methods=['POST','GET'])
def modifier_Gestionnaire(id):
    if request.method == 'POST':  
     req = ('UPDATE gestionnaires SET idTrans=%s,Nom=%s,Prenom=%s,telephone=%s,genre=%s WHERE id=%s')
     idTrans = request.form['idTrans']
     Nom = request.form['Nom']
     Prenom = request.form['Prenom']
     telephone = request.form['telephone']
     genre = request.form['genre']
     valeurs = (idTrans,Nom,Prenom,telephone,genre,id)
     curseur = bd.cursor()
     curseur.execute(req,valeurs)
     return redirect('/gestionnaire')
 
@app.route('/lancer_mod_gest/<id>')
def lancer_mod_gest(id):
     req = "SELECT * FROM gestionnaires WHERE id=%s"
     valeur = (id,)
     curseur = bd.cursor()
     curseur.execute(req,valeur)
     
     donnees = curseur.fetchall()
     return render_template('modifierGestionnaire.html',donnees=donnees)


#differntes routes pour le client 
@app.route('/client')
def client():
    req= 'SELECT * FROM devise'
    req1 = "SELECT clients.id,clients.nom,clients.prenom,clients.adresse,clients.Telephone,clients.genre,clients.idDev,devise.description from clients JOIN devise on devise.id=clients.idDev"
    curseur = bd.cursor(buffered=True)
    
    curseur.execute(req)
    devise= curseur.fetchall()
    
    curseur.execute(req1)
    client= curseur.fetchall()
    
    curseur.close()
    return render_template('client.html',devise=devise,client=client)

@app.route('/add_client',methods=['POST','GET'])
def add_client():
    if request.method == 'POST':
        requete ='INSERT INTO clients (nom,prenom,adresse,Telephone,genre,idDev) VALUES (%s,%s,%s,%s,%s,%s)'
        nom = request.form['nom']
        prenom = request.form['prenom']
        adresse = request.form['adresse']
        Telephone = request.form['Telephone']
        genre = request.form['genre']
        idDev= request.form['idDev']
        valeurs = (nom,prenom,adresse,Telephone,genre,idDev)
        curseur = bd.cursor()
        curseur.execute(requete, valeurs)
        bd.commit()
        return redirect('/index')

@app.route("/ajoutClient")
def Form_AjoutClient():
    req1 = "SELECT * from devise"
    curseur = bd.cursor(buffered=True)
    curseur.execute(req1)
    devise= curseur.fetchall()
    curseur.close()
    return render_template('ajoutClient.html',devise=devise)

@app.route("/delete_Client/<id>")
def delete_Client(id):
    req = ('DELETE from clients WHERE id=%s')
    valeur = (id,)
    curseur = bd.cursor()
    curseur.execute(req,valeur)
    return redirect('/client')

@app.route("/modifier_Client/<id>",methods=['POST','GET'])
def modifier_Client(id):
    if request.method == 'POST':  
     req = ('UPDATE clients SET nom=%s,prenom=%s,adresse=%s,Telephone=%s,genre=%s,idDev=%s WHERE id=%s')
     nom = request.form['nom']
     prenom = request.form['prenom']
     adresse = request.form['adresse']
     Telephone = request.form['Telephone']
     genre = request.form['genre']
     idDev= request.form['idDev']
     valeurs = (nom,prenom,adresse,Telephone,genre,idDev,id)
     curseur = bd.cursor()
     curseur.execute(req,valeurs)
     return redirect('/client')  
 
@app.route('/lancer_mod_cli/<id>')
def lancer_mod_cli(id):
     req = "SELECT * FROM clients WHERE id=%s"
     valeur = (id,)
     curseur = bd.cursor()
     curseur.execute(req,valeur)
     donnees = curseur.fetchall()
     return render_template('modifierClient.html',donnees=donnees)
 
 
 
 #  differentes route pur la transaction 
@app.route('/transaction')
def transaction():
    req= 'SELECT * FROM clients'
    req1 = "SELECT transactions.id,transactions.idClient,transactions.Montant,transactions.DateTransaction,clients.nom,clients.prenom from transactions JOIN clients on clients.id=transactions.idClient"
    curseur = bd.cursor(buffered=True)
    
    curseur.execute(req)
    client= curseur.fetchall()
    
    curseur.execute(req1)
    transaction= curseur.fetchall()
    
    curseur.close()
    return render_template('transaction.html',client=client,transaction=transaction)

@app.route('/add_transaction',methods=['POST','GET'])
def add_transaction():
    if request.method == 'POST':
        requete ='INSERT INTO transactions (idClient,Montant,DateTransaction) VALUES (%s,%s,%s)'
        idClient = request.form['idClient']
        Montant = request.form['Montant']
        DateTransaction = request.form['DateTransaction']
        valeurs = (idClient,Montant,DateTransaction)
        curseur = bd.cursor()
        curseur.execute(requete, valeurs)
        bd.commit()
        with open('transactions.txt', 'a') as fichier:
            fichier.write(f'{idClient}, {Montant}, {DateTransaction}\n')
        return redirect('/transaction')
 
@app.route("/ajoutTransaction")
def Form_AjoutTransaction():
    req1 = "SELECT * from clients"
    curseur = bd.cursor(buffered=True)
    curseur.execute(req1)
    client= curseur.fetchall()
    curseur.close()
    return render_template('ajoutTransaction.html',client=client)

@app.route("/delete_Transaction/<id>")
def delete_Transaction(id):
    req = ('DELETE from transactions WHERE id=%s')
    valeur = (id,)
    curseur = bd.cursor()
    curseur.execute(req,valeur)
    return redirect('/transaction') 

@app.route("/modifier_Transaction/<id>",methods=['POST','GET'])
def modifier_Transaction(id):
    if request.method == 'POST':  
        req = ('UPDATE transactions SET idClient=%s,Montant=%s,DateTransaction=%s WHERE id=%s')
        idClient = request.form['idClient']
        Montant = request.form['Montant']
        DateTransaction = request.form['DateTransaction']
        valeurs = (idClient,Montant,DateTransaction,id)
        curseur = bd.cursor()
        curseur.execute(req,valeurs)
        return redirect('/transaction')  
  
@app.route('/lancer_mod_tra/<id>')
def lancer_mod_tra(id): 
     req = "SELECT * FROM transactions WHERE id=%s"
     valeur = (id,)
     curseur = bd.cursor()
     curseur.execute(req,valeur)
     donnees = curseur.fetchall()
     return render_template('modifierTransaction.html',donnees=donnees)

  
 
 
@app.route('/transactions_envoyer', methods=['GET'])
def transactions_mensuelles():
    requete = '''
    SELECT 
        g.Nom, 
        g.Prenom, 
        t.idClient, 
        t.Montant, 
        t.DateTransaction
    FROM 
        gestionnaires g
    JOIN 
        transactions t ON g.idTrans = t.idClient
    WHERE 
        t.DateTransaction BETWEEN %s AND %s
    '''
    debut_mois = '2024-09-01'
    fin_mois = '2024-09-30'
    curseur = bd.cursor()
    curseur.execute(requete, (debut_mois, fin_mois))
    resultats = curseur.fetchall()
    return render_template('transactions_envoyer.html', transactions=resultats) 
 
 
  
# differentes routes pour le rapport 
@app.route('/rapport')
def raport():
    req= 'SELECT * FROM gestionnaires'
    req1 = "SELECT rapports.id,rapports.idGestion,rapports.TypeRapport,rapports.DateDebut,rapports.DateFin,gestionnaires.Nom,gestionnaires.Prenom from rapports JOIN gestionnaires on gestionnaires.id = rapports.idGestion"
    curseur = bd.cursor(buffered=True)
    
    curseur.execute(req)
    gestionnaire= curseur.fetchall()
    
    curseur.execute(req1)
    rapport= curseur.fetchall()
    curseur.close()
    return render_template('rapport.html',gestionnaire=gestionnaire,rapport=rapport)
    

@app.route('/add_rapport',methods=['POST','GET'])
def add_rapport():
    if request.method == 'POST':
        requete ='INSERT INTO rapports (idGestion,TypeRapport,DateDebut,DateFin) VALUES (%s,%s,%s,%s)'
        idGestion = request.form['idGestion']
        TypeRapport = request.form['TypeRapport']
        DateDebut = request.form['DateDebut'] 
        DateFin = request.form['DateFin']
        valeurs = (idGestion,TypeRapport,DateDebut,DateFin)
        curseur = bd.cursor()
        curseur.execute(requete, valeurs)
        bd.commit()
        return redirect('/rapport')
    
@app.route("/ajoutRapport")
def Form_AjoutRapport():
    req1 = "SELECT * from gestionnaires"
    curseur = bd.cursor(buffered=True)
    curseur.execute(req1)
    gestionnaire= curseur.fetchall()
    curseur.close()
    return render_template('ajoutRapport.html',gestionnaire=gestionnaire)

@app.route("/delete_rapport/<id>")
def delete_Rapport(id):
    req = ('DELETE from rapports WHERE id=%s')
    valeur = (id,)
    curseur = bd.cursor()
    curseur.execute(req,valeur)
    return redirect('/rapport')

@app.route("/modifier_Rapport/<id>",methods=['POST','GET'])
def modifier_Rapport(id):
    if request.method == 'POST':  
     req = ('UPDATE rapports SET idGestion=%s,TypeRapport=%s,DateDebut=%s,DateFin=%s WHERE id=%s')
     idGestion = request.form['idGestion']
     TypeRapport = request.form['TypeRapport']
     DateDebut = request.form['DateDebut']
     DateFin = request.form['DateFin']
     valeurs = (idGestion,TypeRapport,DateDebut,DateFin,id)
     curseur = bd.cursor()
     curseur.execute(req,valeurs)
     return redirect('/rapport')  
 
@app.route('/lancer_mod_rap/<id>')
def lancer_mod_rap(id):
     req = "SELECT * FROM rapports WHERE id=%s"
     valeur = (id,)
     curseur = bd.cursor()
     curseur.execute(req,valeur)
     donnees = curseur.fetchall()
     return render_template('modifierRapport.html',donnees=donnees)
 
 
 
 
 #pour la connexion 
@app.route("/")
def login():
    
    return render_template('login.html')
 
@app.route('/login', methods=['GET', 'POST'])
def loginCG():
    if request.method == 'POST':
        nom = request.form['nom']
        prenom = request.form['prenom']
        
        # Vérifier si l'utilisateur est un client
        requete_client = "SELECT id, prenom FROM clients WHERE nom = %s AND prenom = %s"
        curseur = bd.cursor(buffered=True)
        curseur.execute(requete_client, (nom, prenom))
        client = curseur.fetchone()
        
        # Vérifier si l'utilisateur est un gestionnaire
        requete_gestionnaire = "SELECT id, prenom FROM gestionnaires WHERE Nom = %s AND Prenom = %s"
        curseur.execute(requete_gestionnaire, (nom, prenom))
        gestionnaire = curseur.fetchone()
        
        if client:
            session['id'] = client[0]
            session['prenom'] = client[1]
            flash('Connexion réussie en tant que client.')
            return redirect('/index1')
        elif gestionnaire:
            session['id'] = gestionnaire[0]
            session['prenom'] = gestionnaire[1]
            flash('Connexion réussie en tant que gestionnaire.')
            return redirect('/index')
        else:
            flash('Identifiants invalides.')
    
    return render_template('login.html')



@app.route('/logout')
def logout():
    # Supprimer les informations de session
    session.pop('id', None)
    session.pop('prenom', None)
    flash('Déconnexion réussie.')
    return redirect(url_for('loginCG'))



 
 
 
 
 
   
if __name__=='__main__':
     
#pour lancer le serveur a chaque enregistrement

    app.run(debug=True)