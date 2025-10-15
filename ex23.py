class Transporte:
    def __init__(self, tipo, velocidade):
        self.tipo = tipo
        self.velocidade = velocidade

    def mover(self):
        print(f"{self.tipo} está se movendo a {self.velocidade} km/h.")


class Terrestre(Transporte):
    def __init__(self, tipo, velocidade, rodas):
        super().__init__(tipo, velocidade)
        self.rodas = rodas


class Automovel(Terrestre):
    def __init__(self, tipo, velocidade, rodas, modelo):
        super().__init__(tipo, velocidade, rodas)
        self.modelo = modelo


class Aquatico(Transporte):
    def __init__(self, tipo, velocidade, flutua):
        super().__init__(tipo, velocidade)
        self.flutua = flutua


class Aereo(Transporte):
    def __init__(self, tipo, velocidade, altitude_max):
        super().__init__(tipo, velocidade)
        self.altitude_max = altitude_max


class Lancha(Aquatico):
    def ligar_motor(self):
        print("Lancha ligada e pronta para navegar!")


class Navio(Aquatico):
    def carregar_carga(self):
        print("Navio está carregando contêineres.")


class AviaoMonomotor(Aereo):
    def decolar(self):
        print("Avião monomotor decolando!")


class AviaoComercial(Aereo):
    def embarcar_passageiros(self):
        print("Passageiros embarcando no avião comercial!")


tipo = input("Digite o tipo de transporte (automovel/lancha/navio/aviao_monomotor/aviao_comercial): ").strip().lower()
nome_tipo = input("Nome do transporte: ")
velocidade = float(input("Velocidade (km/h): "))

match tipo:
    case "automovel":
        rodas = int(input("Número de rodas: "))
        modelo = input("Modelo do automóvel: ")
        transporte = Automovel(nome_tipo, velocidade, rodas, modelo)
    case "lancha":
        flutua = input("Flutua? (s/n): ").strip().lower() == "s"
        transporte = Lancha(nome_tipo, velocidade, flutua)
        transporte.ligar_motor()
    case "navio":
        flutua = input("Flutua? (s/n): ").strip().lower() == "s"
        transporte = Navio(nome_tipo, velocidade, flutua)
        transporte.carregar_carga()
    case "aviao_monomotor":
        altitude_max = float(input("Altitude máxima (m): "))
        transporte = AviaoMonomotor(nome_tipo, velocidade, altitude_max)
        transporte.decolar()
    case "aviao_comercial":
        altitude_max = float(input("Altitude máxima (m): "))
        transporte = AviaoComercial(nome_tipo, velocidade, altitude_max)
        transporte.embarcar_passageiros()
    case _:
        transporte = Transporte(nome_tipo, velocidade)

transporte.mover()
