clientes = [
    {"nome": "Cliente A", "saldo": 12000, "investimento": False},
    {"nome": "Cliente B", "saldo": 85000, "investimento": True},
    {"nome": "Cliente C", "saldo": 60000, "investimento": False},
    {"nome": "Cliente D", "saldo": 3000, "investimento": False},
    {"nome": "Cliente E", "saldo": 150000, "investimento": False},
]

total = sum(c["saldo"] for c in clientes)
print(f"Clientes: {len(clientes)}")
print(f"Saldo total: R$ {total:.2f}")
print(f"Saldo médio: R$ {total / len(clientes):.2f}")

print("Oportunidades (saldo acima de R$ 50.000 e sem investimento):")
for c in clientes:
    if c["saldo"] > 50000 and not c["investimento"]:
        print("-", c["nome"])
