from django.db import models

class Marca(models.Model):
    nombre = models.CharField(max_length=50)
    pais_origen = models.CharField(max_length=50, blank=True)
    def __str__(self): return self.nombre

class Vendedor(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    telefono = models.CharField(max_length=20)
    def __str__(self): return self.nombre

class Sucursal(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    def __str__(self): return self.nombre

class Accesorio(models.Model):
    nombre = models.CharField(max_length=100) 
    def __str__(self): return self.nombre

class Auto(models.Model):
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE) 
    modelo = models.CharField(max_length=100)
    anio = models.IntegerField()
    precio = models.DecimalField(max_digits=12, decimal_places=2)
    imagen = models.ImageField(upload_to='autos/', null=True, blank=True)
    vendedor = models.ForeignKey(Vendedor, on_delete=models.SET_NULL, null=True)
    sucursal = models.ForeignKey(Sucursal, on_delete=models.SET_NULL, null=True)
    
    accesorios = models.ManyToManyField(Accesorio, blank=True)
    
    def __str__(self): return f"{self.marca} {self.modelo} ({self.anio})"

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    telefono = models.CharField(max_length=20)
    direccion = models.CharField(max_length=200, blank=True)
    def __str__(self): return self.nombre

class Venta(models.Model):
    auto = models.ForeignKey(Auto, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    vendedor = models.ForeignKey(Vendedor, on_delete=models.SET_NULL, null=True)
    fecha_venta = models.DateField(auto_now_add=True) 
    precio_final = models.DecimalField(max_digits=12, decimal_places=2)
    def __str__(self): return f"Venta: {self.auto.modelo} a {self.cliente.nombre}"