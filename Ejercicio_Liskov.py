class MetodoPagoBase: # Clase maestra
    def procesar_pago():
        pass

class MetodoPagoAutomatico(MetodoPagoBase): # Clase para todos los pagos automaticos
    def procesar_pago(self, cantidad):
        pass

class MetodoPagoManual(MetodoPagoBase): # Clase para todos los pagos manuales
    def procesar_pago():
        pass


"-----------------------------------------------------------------------------------------"
"-----------------------------------------------------------------------------------------"


# Metodos de pago automáticos
class PagoTarjeta(MetodoPagoAutomatico):
    def __init__(self, numero_tarjeta):
        self.numero_tarjeta = numero_tarjeta

    def procesar_pago(self, cantidad):
        print(f"Procesando pago automatico de {cantidad} usando tarjeta {self.numero_tarjeta}")

class PagoPaypal(MetodoPagoAutomatico):
    def __init__(self, cuenta_paypal):
        self.cuenta_paypal = cuenta_paypal
    
    def procesar_pago(self, cantidad):
        print(f"Procesando pago automatico de {cantidad} usando cuenta Paypal {self.cuenta_paypal}")

class PagoBitcoin(MetodoPagoAutomatico):
    def __init__(self, direccion_bitcoin):
        self.direccion_bitcoin = direccion_bitcoin
    
    def procesar_pago(self, cantidad):
        print(f"Procesando pago automatico de {cantidad} usando Bitcoin {self.direccion_bitcoin}")


# Metodo de pago manual
class PagoCheque(MetodoPagoManual):
    def __init__(self, numero_cheque):
        self.numero_cheque = numero_cheque

    def procesar_pago(self, cantidad):
        print(f"Procesando pago manual de {cantidad} usando cheque {self.numero_cheque}")


# Realizar pagos
def realizar_pago_automatico(metodo_pago: MetodoPagoAutomatico, cantidad):
    metodo_pago.procesar_pago(cantidad)

def realizar_pago_manual(metodo_pago: MetodoPagoManual, cantidad):
    metodo_pago.procesar_pago(cantidad)


"-----------------------------------------------------------------------------------------"
"-----------------------------------------------------------------------------------------"


# Instanciar las clases
pago_tarjeta = PagoTarjeta("123 456 789 123")
pago_paypal = PagoPaypal("mi_cuenta@pago.com")
pago_bitcoin = PagoBitcoin("8dfss87fh8a9f7g")
pago_cheque = PagoCheque(123456789)

# Realizar los pagos
realizar_pago_automatico(pago_tarjeta, 400)
realizar_pago_automatico(pago_paypal, 350)
realizar_pago_automatico(pago_bitcoin, 700)

realizar_pago_manual(pago_cheque, 1125)