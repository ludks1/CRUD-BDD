from Cafe import db


class Pedido(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_producto = db.Column(db.Integer, db.ForeignKey(
        'producto.id'), nullable=False)
    id_cliente = db.Column(db.Integer, db.ForeignKey(
        'cliente.id'), nullable=False)
    cantidad = db.Column(db.Integer, default=0)
    fecha = db.Column(db.DateTime, nullable=False)
    total = db.Column(db.Float, nullable=False)
    estado = db.Column(db.String(1), default='0')  # 0: Pendiente, 1: Entregado

    producto = db.relationship('Producto', backref='pedidos')
    cliente = db.relationship('Cliente', backref='pedidos')

    def __repr__(self):
        return f"<Pedido: {self.id} - {self.producto.nombre} - {self.cliente.nombre}>"
