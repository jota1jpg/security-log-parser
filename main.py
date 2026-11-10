tentativas={}
ips_suspeitos = 0

with open("logs/auth.log", "r") as arquivo:
    for linha in arquivo:
        if "FAILED LOGIN" in linha:
            dados = linha.split()
            ips = dados[-1]
            
            if ips in tentativas:
                tentativas[ips] += 1
            else:
                tentativas[ips] = 1

for ip, quantidade in tentativas.items():
    if quantidade >= 3:
       status = "SUSPEITO"
       ips_suspeitos += 1
    else:
       status = "NORMAL"
       print(f"====== RELATÓRIO DE SEGURANÇA ====== ")
       print(f"IP:{ips} | Tentativas:{quantidade} | Status:{status}")
       print(f"Total  de IPs suspeitos:{ips_suspeitos}")