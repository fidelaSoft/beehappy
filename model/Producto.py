class Producto:
    def __init__(self,id, descripcion, cantidad, precio,presentacion):
        self.id = id
        self.descripcion = descripcion
        self.cantidad = cantidad
        self.precio = precio
        self.presentacion = presentacion


p1 = Producto(1,"Miel de abeja oscura x 500gr",150,250.00,)
p2 = Producto(2,"Miel de abeja oscura x 1kg",300,480.00,)
p1 = Producto(3,"Miel de abeja oscura x 12kg",15,5000.00)
p2 = Producto(4,"Miel de abeja oscura x 100kg",4,38500.00)