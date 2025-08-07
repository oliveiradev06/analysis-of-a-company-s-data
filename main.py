# -*- coding: utf-8 -*-
"""Análise de Dados com Pandas"""

import pandas as pd

# Leitura do dataset
df = pd.read_csv("https://raw.githubusercontent.com/guilhermeonrails/data-jobs/refs/heads/main/salaries.csv")

# Visualização básica
df.head(10)
df.info()
df.describe()

# Dimensões
linhas, colunas = df.shape
print("N° de Linhas:", linhas)
print("N° de Colunas:", colunas)

# Verificando nomes originais das colunas
print("Colunas antes da renomeação:")
print(df.columns)

# Renomeando colunas (nomes reais em inglês → traduzido para português)
df.rename(columns={
    'work_year': 'ano',
    'experience_level': 'senioridade',
    'employment_type': 'contrato',
    'job_title': 'cargo',
    'salary': 'salario',
    'salary_currency': 'moeda',
    'salary_in_usd': 'usd',
    'employee_residence': 'residencia',
    'remote_ratio': 'remoto',
    'company_location': 'localizacao',
    'company_size': 'tamanho_empresa'
}, inplace=True)

print("Colunas após renomeação:")
print(df.columns)

# Contagens de valores antes da substituição
print("\nContagem por senioridade (antes):")
print(df["senioridade"].value_counts())

print("\nContagem por contrato (antes):")
print(df['contrato'].value_counts())

print("\nContagem por modelo de trabalho (antes):")
print(df['remoto'].value_counts())

print("\nContagem por tamanho da empresa (antes):")
print(df['tamanho_empresa'].value_counts())

# Substituindo siglas por nomes descritivos
df['senioridade'] = df['senioridade'].replace({
    'SE': 'Sênior',
    'MI': 'Pleno',
    'EN': 'Júnior',
    'EX': 'Executivo'
})

df['contrato'] = df['contrato'].replace({
    'FT': 'Tempo Integral',
    'CT': 'Contrato',
    'PT': 'Tempo Parcial',
    'FL': 'Freelancer'
})

df['tamanho_empresa'] = df['tamanho_empresa'].replace({
    'M': 'Médio',
    'L': 'Grande',
    'S': 'Pequeno'
})

df['remoto'] = df['remoto'].replace({
    0: 'Presencial',
    50: 'Híbrido',
    100: 'Remoto'
})

# Contagens após a substituição
print("\nContagem por senioridade (depois):")
print(df['senioridade'].value_counts())

print("\nContagem por contrato (depois):")
print(df['contrato'].value_counts())

print("\nContagem por tamanho da empresa (depois):")
print(df['tamanho_empresa'].value_counts())

print("\nContagem por modelo de trabalho (depois):")
print(df['remoto'].value_counts())

# Visualização final
print("\nVisualização dos primeiros dados formatados:")
print(df.head())

# Descrição de colunas categóricas
print("\nDescrição de colunas categóricas:")
print(df.describe(include='object'))

# Estatísticas gerais
print("\nEstatísticas gerais:")
print(df.describe())
