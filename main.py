tentativas={}
with open("logs/auth.log", "r") as arquivo:
    for linha in arquivo:
     if "FAILED LOGIN" in linha:
        dados = linha.split()
        ips = dados[-1]
        temp = dados[1]
        data = dados[0]
        if ips in tentativas:
           tentativas[ips] += 1
        else:
           tentativas[ips] = 1
for ip, quantidade in tentativas.items():
   if quantidade >= 3:
      status = "SUSPEITO"
   else:
      status = "NORMAL"
   print(f" |Data: {data} |IP:{ip}| Tentativas:{quantidade} |Tempo: {temp} | Status: {status}")