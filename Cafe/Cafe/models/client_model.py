from Cafe import db


class Cliente(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(30), nullable=False)
    apellido = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(50), unique=True)
    telefono = db.Column(db.String(10))
    direccion = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return f"<Cliente {self.nombre} {self.apellido}>"
