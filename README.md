# Analisador de Logs de Autenticação

## Sobre o projeto

Este projeto consiste em um analisador de logs desenvolvido em Python, com o objetivo de identificar possíveis atividades suspeitas em tentativas de autenticação.

O programa analisa um arquivo de logs, identifica tentativas de login malsucedidas e contabiliza quantas vezes cada endereço IP aparece.

IPs com 3 ou mais tentativas de login malsucedidas são classificados como **SUSPEITOS**. Os demais são classificados como **NORMAIS**.

## Funcionalidades

- Leitura de arquivos de logs.
- Identificação de tentativas de login malsucedidas (`FAILED LOGIN`).
- Contagem de tentativas por endereço IP.
- Classificação de IPs como NORMAL ou SUSPEITO.
- Geração de relatório no terminal.
- Contagem total de IPs suspeitos.

## Tecnologias utilizadas

- Python 3
- Dicionários
- Estruturas condicionais (`if/else`)
- Estruturas de repetição (`for`)
- Manipulação de arquivos (`open`)

## Estrutura do projeto

```text
analisador-de-logs/
│
├── logs/
│   └── auth.log
│
├── main.py
├── README.md
└── .gitignore
```

## Como executar

1. Clone este repositório:

```bash
git clone URL_DO_SEU_REPOSITORIO
```

2. Entre na pasta do projeto:

```bash
cd analisador-de-logs
```

3. Execute o programa:

```bash
python main.py
```

## Regra de classificação

O programa utiliza a seguinte regra:

| Quantidade de tentativas | Classificação |
|---|---|
| Menos de 3 | NORMAL |
| 3 ou mais | SUSPEITO |

## Exemplo de resultado

```text
====== RELATÓRIO DE SEGURANÇA ======

IP: 192.168.0.10 | Tentativas: 3 | Status: SUSPEITO
IP: 192.168.0.15 | Tentativas: 1 | Status: NORMAL

Total de IPs suspeitos: 1
```

*Resultado ilustrativo.*

## Objetivo de aprendizado

O projeto foi desenvolvido com o objetivo de praticar conceitos fundamentais de Python aplicados à cibersegurança, especialmente análise de logs, manipulação de arquivos, estruturas de dados e identificação de possíveis atividades suspeitas.

## Limitações

A classificação é baseada apenas na quantidade de tentativas malsucedidas por IP. Portanto, um IP classificado como suspeito representa uma possível atividade suspeita, não uma confirmação de invasão.

---

**Projeto desenvolvido para fins educacionais.**

<img width="456" height="85" alt="image" src="https://github.com/user-attachments/assets/83e5fe9d-df9d-4795-965d-3e133633f19f" />

