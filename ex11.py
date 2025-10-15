class NotaFiscal:
    def __init__(self, numero, tipo, serie, cnpj, razao_social, data_emissao, valor_produto, icms=0.0, frete=0.0, ipi=0.0):
        self.numero = numero
        self.tipo = tipo
        self.serie = serie
        self.cnpj = cnpj
        self.razao_social = razao_social
        self.data_emissao = data_emissao
        self.valor_produto = valor_produto
        self.icms = icms
        self.frete = frete
        self.ipi = ipi
        self.valor_total = 0.0

    def obter_numero(self):
        return self.numero

    def obter_data_emissao(self):
        return self.data_emissao

    def alterar_razao_social(self, nova_razao):
        self.razao_social = nova_razao

    def calcular_valor_total(self):
        self.valor_total = self.valor_produto + self.frete + self.icms + self.ipi
        return self.valor_total


numero = input("Digite o número da nota fiscal: ")
tipo = input("Digite o tipo: ")
serie = input("Digite a série: ")
cnpj = input("Digite o CNPJ: ")
razao_social = input("Digite a razão social: ")
data_emissao = input("Digite a data de emissão (DD/MM/AAAA): ")
valor_produto = float(input("Digite o valor do produto: "))
icms = float(input("Digite o ICMS: "))
frete = float(input("Digite o frete: "))
ipi = float(input("Digite o IPI: "))

nota = NotaFiscal(numero, tipo, serie, cnpj, razao_social, data_emissao, valor_produto, icms, frete, ipi)

print(f"\nNúmero: {nota.obter_numero()}")
print(f"Data de emissão: {nota.obter_data_emissao()}")
print(f"Razão social: {nota.razao_social}")
print(f"Valor total: R$ {nota.calcular_valor_total():.2f}")

nova_razao = input("\nDigite uma nova razão social (ou Enter para manter a atual): ")
if nova_razao.strip():
    nota.alterar_razao_social(nova_razao)
    print(f"Razão social atualizada: {nota.razao_social}")
