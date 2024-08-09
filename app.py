from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_mail import Mail, Message
import random
from models import User, Group, Survey, Question, Answer, ActivityLog

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://usuario:contraseña@localhost/nombre_base_datos'
app.config['SECRET_KEY'] = 'tu_clave_secreta'
app.config['MAIL_SERVER'] = 'smtp.tu_servidor_email.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = 'tu_correo@dominio.com'
app.config['MAIL_PASSWORD'] = 'tu_contraseña'
app.config['MAIL_USE_TLS'] = True

db = SQLAlchemy(app)
mail = Mail(app)

# Ruta para registrar usuarios
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        nombre_empresa = request.form['nombre_empresa']
        usuario = request.form['usuario']
        password = generate_password_hash(request.form['password'])
        correo = request.form['correo']
        tipo_usuario = 'empresa'  # Por defecto, registro de empresa
        nuevo_usuario = User(nombre_empresa=nombre_empresa, usuario=usuario, password=password, correo=correo, tipo_usuario=tipo_usuario)
        db.session.add(nuevo_usuario)
        db.session.commit()
        flash('Registro exitoso. Ahora puede iniciar sesión.', 'success')
        return redirect(url_for('login'))
    return render_template('register.html')

# Ruta para iniciar sesión
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        usuario = request.form['usuario']
        password = request.form['password']
        usuario_obj = User.query.filter_by(usuario=usuario).first()
        if usuario_obj and check_password_hash(usuario_obj.password, password):
            session['user_id'] = usuario_obj.id
            session['user_type'] = usuario_obj.tipo_usuario
            codigo_verificacion = random.randint(100000, 999999)
            session['codigo_verificacion'] = codigo_verificacion
            enviar_codigo_verificacion(usuario_obj.correo, codigo_verificacion)
            return redirect(url_for('verificar_codigo'))
        else:
            flash('Usuario o contraseña incorrectos.', 'danger')
    return render_template('login.html')

def enviar_codigo_verificacion(correo, codigo):
    msg = Message('Código de Verificación', sender='tu_correo@dominio.com', recipients=[correo])
    msg.body = f'Su código de verificación es: {codigo}'
    mail.send(msg)

# Ruta para verificar el código de autenticación
@app.route('/verificar_codigo', methods=['GET', 'POST'])
def verificar_codigo():
    if request.method == 'POST':
        codigo = request.form['codigo']
        if 'codigo_verificacion' in session and session['codigo_verificacion'] == int(codigo):
            session.pop('codigo_verificacion', None)
            return redirect(url_for('dashboard'))
        else:
            flash('Código de verificación incorrecto.', 'danger')
    return render_template('verify_code.html')

# Ruta del panel de control del usuario
@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    user_type = session.get('user_type')
    # Lógica para mostrar el panel correcto basado en el tipo de usuario
    if user_type == 'superadmin':
        return render_template('admin.html')  # Panel de superadmin
    elif user_type == 'empresa':
        return render_template('dashboard.html')  # Panel de empresa
    elif user_type == 'general':
        return render_template('encuesta.html')  # Panel de usuario general
    return redirect(url_for('login'))

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
