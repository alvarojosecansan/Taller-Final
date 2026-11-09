class Envio:

  def __init__(self, peso_kg, distancia_km):
    self.peso_kg = peso_kg
    self.distancia_km = distancia_km

  def calcular_costo(self, monto_base):
    pass


class EnvioEstandar(Envio):

  def calcular_costo(self, monto_base):
    return monto_base * 1.05


class EnvioExpress(Envio):

  def calcular_costo(self, monto_base):
    return monto_base * 1.15


paquetes = [
    EnvioEstandar(3.0, 45),
    EnvioExpress(1.2, 60),
    EnvioEstandar(6.5, 120),
    EnvioExpress(4.0, 90),
]

monto_base = 50.0

for paquete in paquetes:
  categoria = type(paquete).__name__
  total = paquete.calcular_costo(monto_base)
  print(f"{categoria} -> Total a pagar: ${total:.2f}")