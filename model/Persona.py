class Persona:
    def __init__(self, dni, nombre, apellido, tel, mail ):
        self.dni = dni
        self.nombre = nombre
        self.apellido = apellido
        self.tel = tel
        self.mail = mail


class Cliente(Persona):
    def __init__(self, dni, nombre, apellido, tel, mail ):
        super().__init__(dni,nombre,apellido,tel,mail)

    def get_ventas(self):
        pass

class Proveedor(Persona):
    def __init__(self, dni, nombre, apellido, tel, mail ):
        super().__init__(dni,nombre,apellido,tel,mail)

    def get_compras(self):
        pass