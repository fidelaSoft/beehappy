#Mock up de un database
from model.persona import Cliente
from model.producto import Producto
class DataBase:
    def get_clientes(self):
        return [Cliente("18447836","Luis","Navarro","2615460220","luis@gmail.com"),
                Cliente("36812603","Federico","Olguin","2615460220","fede@gmail.com"),
                Cliente("46326369","Matias","Sanchez","2615460220","mti@gmail.com"),
                Cliente("44139890","Julieta","Toledo","2615460220","juli@gmail.com")]
    def get_productos(self):
        return [Producto(1, "Miel de abeja oscura x 500gr", 150, 250.00,"Frasco 1/2" ),
                Producto(2, "Miel de abeja oscura x 1kg", 300, 480.00 , "Frasco 1 Kg"),
                Producto(3, "Miel de abeja oscura x 12kg", 15, 5000.00, "Balde"),
                Producto(4, "Miel de abeja oscura x 100kg", 4, 38500.00,"Tambor")]
