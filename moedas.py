from forex_python.converter import CurrencyRates

moedas = ['USD','EUR','GBP','JPY','CHF','CAD','AUD','CNY','INR','SGD']

simbolos = ['$', '€', '£', '¥', 'CHF', 'C$', 'A$', '¥', '₹', 'S$']

nomes = [
    'Dólar Americano',
    'Euro',
    'Libra Esterlina',
    'Iene Japonês',
    'Franco Suíço',
    'Dólar Canadense',
    'Dólar Australiano',
    'Yuan Chinês',
    'Rúpia Indiana',
    'Dólar de Singapura'
]

c = CurrencyRates()

try:
    reais = float(input('Digite quantos reais você tem: R$ '))

    print("\nBuscando taxas atuais...\n")
    taxas = c.get_rates('BRL')

    print("=" * 50)
    print(f"💰 Conversão de R$ {reais:.2f}")
    print("=" * 50)

    for i in range(len(moedas)):
        moeda = moedas[i]

        if moeda in taxas:
            convertido = reais * taxas[moeda]

            print(f"{nomes[i]:<22} ({moeda})")
            print(f"→ {simbolos[i]} {convertido:,.2f}")
            print("-" * 50)

except ValueError:
    print("Digite apenas números.")
except Exception as e:
    print("Erro ao acessar a API:", e)