with open("logs/auth.log", "r") as arquivo:
    for linha in arquivo:
     if "FAILED LOGIN" in linha:
        print(linha )