tentativas={}
with open("logs/auth.log", "r") as arquivo:
    for linha in arquivo:
     if "FAILED LOGIN" in linha:
        dados = linha.split()
        ips = dados[-1]
        if ips in tentativas:
           tentativas[ips] += 1
        else:
           tentativas[ips] = 1

print(f"{tentativas}")