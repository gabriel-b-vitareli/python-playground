import string

senha = input("Digite uma senha: ")

tamanho = len(senha)

tem_minuscula = any(c.islower() for c in senha)
tem_maiuscula = any(c.isupper() for c in senha)
tem_numero = any(c.isdigit() for c in senha)
tem_simbolo = any(not c.isalnum() for c in senha)
pontos = sum([tem_minuscula, tem_maiuscula, tem_numero, tem_simbolo])

if tamanho < 6:
    classificacao = "Muito fraca"
elif pontos <= 2:
    classificacao = "Fraca"
elif pontos == 3:
    classificacao = "Média"
else:
    classificacao = "Forte"

possibilidades = 0

if tem_minuscula: possibilidades += 26
if tem_maiuscula: possibilidades += 26
if tem_numero: possibilidades += 10
if tem_simbolo: possibilidades += 10

if possibilidades == 0:
    possibilidades = 1

total_combinacoes = possibilidades ** tamanho
tempo = total_combinacoes / 1_000_000_000

senhas_comuns = [
    "123", "1234", "123456", "12345678",
    "senha", "password", "qwerty", "abc123"
]

if senha.lower() in senhas_comuns:
    tempo = 0.000001
    classificacao = "Muito fraca"

elif senha.isdigit() and tamanho <= 4:
    tempo /= 100000

elif senha.islower() and tamanho <= 5:
    tempo /= 10000

elif senha in string.ascii_lowercase or senha in "0123456789":
    tempo /= 100000

def formatar_tempo(segundos):
    if segundos < 1:
        return f"{segundos:.8f} segundos"
    elif segundos < 60:
        return f"{segundos:.2f} segundos"
    elif segundos < 3600:
        return f"{segundos/60:.2f} minutos"
    elif segundos < 86400:
        return f"{segundos/3600:.2f} horas"
    elif segundos < 31536000:
        return f"{segundos/86400:.2f} dias"
    else:
        return f"{segundos/31536000:.2f} anos"

tempo_formatado = formatar_tempo(tempo)
faltando = []

if not tem_minuscula:
    faltando.append("letras minúsculas")
if not tem_maiuscula:
    faltando.append("letras maiúsculas")
if not tem_numero:
    faltando.append("números")
if not tem_simbolo:
    faltando.append("símbolos")
if tamanho < 8:
    faltando.append("maior comprimento (mínimo 8)")
print("\n--- RESULTADO ---")
print(f"Classificação: {classificacao}")
print(f"Tempo estimado para quebrar: {tempo_formatado}")

if faltando:
    print("Melhorias sugeridas:", ", ".join(faltando))
else:
    print("Sua senha já atende a todos os critérios básicos.")