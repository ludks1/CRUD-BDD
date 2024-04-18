"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template, request, redirect, flash, url_for
from . import app
from .models.client_model import Cliente
from .models.order_model import Pedido
from .models.product_model import Producto
from Cafe import db

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )


@app.route('/clientes')
def clientes():
    clientes = Cliente.query.all()
    return render_template('clientes.html', clientes=clientes)


@app.route('/clientes/nuevo')
def nuevo_cliente():
    return render_template('nuevo_cliente.html')


@app.route('/clientes/crear', methods=['POST'])
def crear_cliente():
    nombre = request.form['nombre']
    apellido = request.form['apellido']
    email = request.form['email']
    telefono = request.form['telefono']
    direccion = request.form['direccion']
    nuevo_cliente = Cliente(nombre=nombre, apellido=apellido,
                            email=email, telefono=telefono, direccion=direccion)
    db.session.add(nuevo_cliente)
    db.session.commit()
    flash('Cliente creado exitosamente')
    return redirect(url_for('clientes.clientes'))


@app.route('/clientes/<int:id>/editar')
def editar_cliente(id):
    cliente = Cliente.query.get_or_404(id)
    return render_template('editar_cliente.html', cliente=cliente)


@app.route('/clientes/<int:id>/actualizar', methods=['POST'])
def actualizar_cliente(id):
    cliente = Cliente.query.get_or_404(id)
    cliente.nombre = request.form['nombre']
    cliente.apellido = request.form['apellido']
    cliente.email = request.form['email']
    cliente.telefono = request.form['telefono']
    cliente.direccion = request.form['direccion']
    db.session.commit()
    flash('Cliente actualizado exitosamente')
    return redirect(url_for('clientes.clientes'))


@app.route('/clientes/<int:id>/eliminar')
def eliminar_cliente(id):
    cliente = Cliente.query.get_or_404(id)
    db.session.delete(cliente)
    db.session.commit()
    flash('Cliente eliminado exitosamente')
    return redirect(url_for('clientes.clientes'))


@app.route('/pedidos')
def pedidos():
    pedidos = Pedido.query.all()
    return render_template('pedidos.html', pedidos=pedidos)


@app.route('/pedidos/nuevo')
def nuevo_pedido():
    clientes = Cliente.query.all()
    productos = Producto.query.all()
    return render_template('nuevo_pedido.html', clientes=clientes, productos=productos)


@app.route('/pedidos/crear', methods=['POST'])
def crear_pedido():
    cliente_id = request.form['cliente_id']
    producto_id = request.form['producto_id']
    cantidad = request.form['cantidad']
    fecha = datetime.datetime.now()  # Capturar la fecha actual
    # Validar si la cantidad solicitada no supera el stock del producto
    producto = Producto.query.get(producto_id)
    if cantidad > producto.stock:
        flash('La cantidad solicitada supera el stock disponible')
        return redirect(url_for('pedidos.nuevo_pedido'))
    total = cantidad * producto.precio  # Calcular el total del pedido
    nuevo_pedido = Pedido(
        cliente_id=cliente_id,
        producto_id=producto_id,
        cantidad=cantidad,
        fecha=fecha,
        total=total
    )
    db.session.add(nuevo_pedido)
    db.session.commit()
    flash('Pedido creado exitosamente')
    return redirect(url_for('pedidos.pedidos'))


@app.route('/pedidos/<int:id>/editar')
def editar_pedido(id):
    pedido = Pedido.query.get_or_404(id)
    clientes = Cliente.query.all()
    productos = Producto.query.all()
    return render_template('editar_pedido.html', pedido=pedido, clientes=clientes, productos=productos)


@app.route('/pedidos/<int:id>/actualizar', methods=['POST'])
def actualizar_pedido(id):
    pedido = Pedido.query.get_or_404(id)
    cliente_id = request.form['cliente_id']
    producto_id = request.form['producto_id']
    cantidad = request.form['cantidad']
    # Validar si la cantidad solicitada no supera el stock del producto (actualizar)
    producto = Producto.query.get(producto_id)
    nueva_cantidad = producto.stock + pedido.cantidad - \
        cantidad  # Considerar la cantidad original
    if nueva_cantidad < 0:
        flash('La cantidad solicitada supera el stock disponible')
        return redirect(url_for('pedidos.editar_pedido', id=id))
    pedido.cliente_id = cliente_id
    pedido.producto_id = producto_id
    pedido.cantidad = cantidad
    pedido.total = cantidad * producto.precio  # Recalcular el total
    db.session.commit()
    flash('Pedido actualizado exitosamente')
    return redirect(url_for('pedidos.pedidos'))


@app.route('/pedidos/<int:id>/eliminar')
def eliminar_pedido(id):
    pedido = Pedido.query.get_or_404(id)
    db.session.delete(pedido)
    db.session.commit()
    flash('Pedido eliminado exitosamente')
    return redirect(url_for('pedidos.pedidos'))

@app.route('/productos')
def productos():
    productos = Producto.query.all()
    return render_template('productos.html', productos=productos)


@app.route('/productos/nuevo')
def nuevo_producto():
    return render_template('nuevo_producto.html')


@app.route('/productos/crear', methods=['POST'])
def crear_producto():
    nombre = request.form['nombre']
    descripcion = request.form['descripcion']
    precio = request.form['precio']
    stock = request.form['stock']
    nuevo_producto = Producto(
        nombre=nombre, descripcion=descripcion, precio=precio, stock=stock)
    db.session.add(nuevo_producto)
    db.session.commit()
    flash('Producto creado exitosamente')
    return redirect(url_for('productos.productos'))


@app.route('/producto/<int:id>/editar')
def editar_producto(id):
    producto = Producto.query.get_or_404(id)
    return render_template('editar_producto.html', producto=producto)


@app.route('/producto/<int:id>/actualizar', methods=['POST'])
def actualizar_producto(id):
    producto = Producto.query.get_or_404(id)
    producto.nombre = request.form['nombre']
    producto.descripcion = request.form['descripcion']
    producto.precio = request.form['precio']
    producto.stock = request.form['stock']
    db.session.commit()
    flash('Producto actualizado exitosamente')
    return redirect(url_for('productos.productos'))


@app.route('/productos/<int:id>/eliminar')
def eliminar_producto(id):
    producto = Producto.query.get_or_404(id)
    db.session.delete(producto)
    db.session.commit()
    flash('Producto eliminado exitosamente')
    return redirect(url_for('productos.productos'))


@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404

