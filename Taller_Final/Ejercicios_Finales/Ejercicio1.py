class ProductoInventario:

  def __init__(self, nombre_articulo, costo_inicial):
    self.__nombre_articulo = nombre_articulo
    self.__historial_costos = []
    self.precio = costo_inicial

  @property
  def nombre_articulo(self):
    return self.__nombre_articulo

  @property
  def precio(self):
    if self.__historial_costos:
      return self.__historial_costos[-1]
    return 0

  @precio.setter
  def precio(self, nuevo_monto):
    if 0 <= nuevo_monto <= 10000:
      self.__historial_costos.append(nuevo_monto)
      print(f"Precio registrado correctamente: ${nuevo_monto}")
    else:
      print(
          f"Rechazado: El valor ${nuevo_monto} excede el rango permitido"
          " (0-10000)."
      )

  @property
  def precio_promedio(self):
    if not self.__historial_costos:
      return 0
    return sum(self.__historial_costos) / len(self.__historial_costos)


articulo = ProductoInventario("Pantalón Jeans", 2000)
articulo.precio = 2150
articulo.precio = -50
articulo.precio = 11000

print("Precio actual en sistema:", articulo.precio)
print("Promedio histórico:", articulo.precio_promedio)