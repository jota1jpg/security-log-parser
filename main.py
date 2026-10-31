with open("logs/auth.log", "r") as arquivo:
    for linha in arquivo:
     if "FAILED LOGIN" in linha:
        dados = linha.split()
        ips = dados[-1]
        print(ips)