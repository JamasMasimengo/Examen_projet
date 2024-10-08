from flask import Flask, render_template, request, redirect, session
import mysql.connector
from flask_bcrypt import  Bcrypt
import secrets

app = Flask(__name__)

# Configuration de la base de données
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="chat_app"
)
app.config['SECRET_KEY']= secrets.token_hex(16)
bcrypt=Bcrypt(app)


@app.route('/',methods=['GET','POST'])
def login():        
       
        
    return render_template('login.html')

@app.route('/signin')  
def signin():
    return render_template('signin.html')

@app.route('/enregistrer_user',methods=['POST','GET'])
def enregistrer_user():
    if request.method=='POST':
        firstname = request.form['firstName']
        lastname = request.form['lastName']
        username = request.form['username']
        password = request.form['password']
        hash=bcrypt.generate_password_hash(password).decode('utf-8')

        photo = 'image'

        req = 'INSERT INTO `users`( `username`, `password`, `firstname`, `lastname`, `profile_picture`) VALUES (%s,%s,%s,%s,%s)'

        valeur = (username,hash,firstname,lastname,photo)

        curseur = db.cursor() 
        rows=curseur.execute(req,valeur)
        db.commit()
        curseur.close()
        msg=""
        if rows==1:
            msg="Compte crée avec succes! Entrez vos identifiants pour vous connecter"
            return render_template("login.html",msg=msg)
        else:
            msg="Echec de creation.Reesayer Svp!"
            return render_template('signin.html',msg=msg)
    

    return redirect('signin')
@app.route('/index',methods=['POST','GET'])
def index():
    if request.method == "POST":
        pwdverif=None
        username = request.form['username']
        password = request.form['password']
        cursor=db.cursor(buffered=True)
        cursor.execute("SELECT * FROM users WHERE username=%s",(username,))
        user=cursor.fetchone()
        cursor.close()
        pwdverif=bcrypt.check_password_hash(user[2], password)
        if user and pwdverif:
            session['loggedin']=True
            session['id']=user[0]
            session['firstname']=user[3]
            session['lastname']=user[4]
            session['username']=user[1]
            message="Vous etes connecté"
            firstname=session.get('firstname')
            lastname=session.get('lastname')
            idsender=session.get('id')
            username=session.get('username')

            cursor=db.cursor(buffered=True)
            cursor.execute("SELECT * FROM users WHERE username!=%s",(username,))
            user=cursor.fetchall()
            cursor.close()
            return render_template('index.html',message=message,firstname=firstname,lastname=lastname,username=username,idsender=idsender,user=user)
    return render_template('login.html')

@app.route('/conversation',methods=['POST','GET'])
def conversation():
    sender = request.form['sender']
    receiver = request.form['receiver']
    firstname = request.form['firstname']
    lastname = request.form['lastname']
    idsender = request.form['idsender']
    idreceiver = request.form['idreceiver']

    cursor=db.cursor(buffered=True)
    cursor.execute("SELECT * FROM users WHERE username!=%s",(sender,))
    user=cursor.fetchall()

    cursor.execute("SELECT * FROM users WHERE username=%s",(receiver,))
    receive=cursor.fetchall()

    cursor.execute("SELECT * FROM messages WHERE (sender_id=%s AND receiver_id=%s) OR (sender_id=%s AND receiver_id=%s) ORDER BY sent_at DeSC",(idsender,idreceiver,idreceiver,idsender))
    message = cursor.fetchall()
    cursor.close()

    return render_template('conversation.html',user=user,receive=receive,username=sender,firstname=firstname,lastname=lastname,message=message,idreceiver=idreceiver,idsender=idsender)

    
@app.route('/envoyer_message',methods=['POST','GET'])
def envoyer_message():
    idreceiver = request.form['idreceiver']
    idsender = request.form['idsender']
    message = request.form['message']
    firstname = request.form['firstname']
    lastname = request.form['lastname']
    sender = request.form['sender']

    cursor=db.cursor(buffered=True)

    cursor.execute ('INSERT INTO messages (sender_id,receiver_id,message,sent_at) VALUES (%s,%s,%s,NOW())',(idreceiver,idsender,message))

    cursor.execute("SELECT * FROM users WHERE username!=%s",(sender,))
    user=cursor.fetchall()

    cursor.execute("SELECT * FROM users WHERE id=%s",(idreceiver,))
    receive=cursor.fetchall()

    cursor.execute("SELECT * FROM messages WHERE (sender_id=%s AND receiver_id=%s) OR (sender_id=%s AND receiver_id=%s) ORDER BY sent_at DeSC",(idsender,idreceiver,idreceiver,idsender))
    message = cursor.fetchall()
    cursor.close()

    return render_template('conversation.html',user=user,username=sender,firstname=firstname,lastname=lastname,message=message,idreceiver=idreceiver,idsender=idsender,receive=receive)

#@app.route('/message',methods=['GET','POST'])
#def message():
    #sender_id= request.form['sender_id'] 
    #receiver_id= request.form['receiver_id']
    #message= request.form['message']
    #sent_at= request.form['sent_at']    
    #req='INSERT INTO `messages` WHERE (`sender_id`,`receiver_id`,`message`,`sent_at`)  VALUES(%s,%s,%s,%s)'

    #valeur = (sender_id,receiver_id,message,sent_at)

    #curseur = db.cursor()
    #curseur.execute(req,valeur)
    #db.commit()
     
    #return redirect('/message')





if __name__ == '__main__':
    app.run(debug = True)

   