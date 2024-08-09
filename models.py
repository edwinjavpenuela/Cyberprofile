from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre_empresa = db.Column(db.String(100))
    usuario = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    correo = db.Column(db.String(100), unique=True, nullable=False)
    tipo_usuario = db.Column(db.String(20), nullable=False)  # 'superadmin', 'empresa', 'general'

class Group(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    usuario_empresa_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    usuario_empresa = db.relationship('User', backref='grupos')

class Survey(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(200), nullable=False)
    usuario_superadmin_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    usuario_superadmin = db.relationship('User', backref='encuestas')

class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    texto = db.Column(db.String(500), nullable=False)
    encuesta_id = db.Column(db.Integer, db.ForeignKey('survey.id'), nullable=False)
    encuesta = db.relationship('Survey', backref='preguntas')

class Answer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    texto = db.Column(db.String(500), nullable=False)
    pregunta_id = db.Column(db.Integer, db.ForeignKey('question.id'), nullable=False)
    pregunta = db.relationship('Question', backref='respuestas')

class ActivityLog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    actividad = db.Column(db.String(500), nullable=False)
    fecha_hora = db.Column(db.DateTime, nullable=False)
