class Producto:
    def __init__(self, nombre, categoria, precio, disponibilidad, calificacion):
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio
        self.disponibilidad = disponibilidad
        self.calificacion = calificacion

class CarritoCompras:
    def __init__(self):
        self.items = []

    def agregar_producto(self, producto):
        self.items.append(producto)

    def total(self):
        return sum(p.precio for p in self.items)

class Pago:
    def __init__(self, metodo, estado="pendiente"):
        self.metodo = metodo
        self.estado = estado

    def validar_pago(self):
        self.estado = "aprobado"
        return True

class Inventario:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def actualizar_stock(self, nombre, cantidad):
        for producto in self.productos:
            if producto.nombre == nombre:
                producto.disponibilidad += cantidad

class Pedido:
    def __init__(self, usuario, carrito):
        self.usuario = usuario
        self.carrito = carrito
        self.estado = "pendiente"

    def procesar_pedido(self):
        self.estado = "completado"

class Reseña:
    def __init__(self, usuario, producto, calificacion, comentario):
        self.usuario = usuario
        self.producto = producto
        self.calificacion = calificacion
        self.comentario = comentario

class Usuario:
    def __init__(self, nombre, correo, contraseña):
        self.nombre = nombre
        self.correo = correo
        self.contraseña = contraseña
        self.autenticado = False

    def iniciar_sesion(self, contraseña):
        if self.contraseña == contraseña:
            self.autenticado = True
            return True
        return False

class Sistema:
    def __init__(self):
        self.usuarios = []
        self.inventario = Inventario()
        self.pedidos = []

    def registrar_usuario(self, usuario):
        self.usuarios.append(usuario)

    def realizar_pedido(self, usuario, carrito):
        if usuario.autenticado:
            pedido = Pedido(usuario, carrito)
            self.pedidos.append(pedido)
            return pedido
        return None
