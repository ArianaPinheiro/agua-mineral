# Previsão de Vendas de Água Mineral com Machine Learning 💧📊

## 📌 Visão Geral
Este projeto tem como objetivo prever a quantidade de **água mineral vendida por dia** com base na **temperatura ambiente**, utilizando técnicas de **Machine Learning**.  
A solução ajuda comerciantes a planejarem melhor sua produção e estoque, reduzindo desperdícios e maximizando resultados.

---

## 🧠 Problema de Negócio
Em dias mais quentes, a demanda por água mineral aumenta significativamente.  
Sem previsão adequada, o comerciante pode:
- produzir menos e perder vendas
- produzir mais e gerar desperdício

A proposta é usar **regressão preditiva** para antecipar essa demanda.

---

## ⚙️ Tecnologias Utilizadas
- **Python 3**
- **Pandas** – manipulação de dados
- **Scikit-learn** – modelo de regressão linear
- **MLflow** – rastreamento de experimentos e métricas
- **VS Code** – desenvolvimento
- **Git/GitHub** – versionamento

---

## 📊 Dataset
Dataset sintético contendo:
- `temperature` → temperatura do dia (°C)
- `vendas` → unidades de água mineral vendidas

Arquivo:  
data/water_sales.csv

---

## 🤖 Modelo de Machine Learning
- Tipo: **Regressão Linear**
- Variável independente: Temperatura
- Variável dependente: Vendas

O modelo foi treinado e avaliado utilizando divisão de dados em treino e teste.

---

## 📈 Resultado
- **Métrica utilizada:** Mean Squared Error (MSE)
- **Resultado obtido:**  

MSE ≈ 76.59

Todos os experimentos e métricas foram registrados no **MLflow**.

---

## 🧪 MLflow
O MLflow foi utilizado para:
- registrar métricas
- versionar o modelo treinado
- acompanhar execuções do experimento

Interface acessada via:
mlflow ui

---

## 📁 Estrutura do Projeto

agua-mineral-ml/
│
├─ data/
│ └─ water_sales.csv
├─ src/
│ └─ train.py
├─ inputs/
│ └─ exemplo.txt
├─ requirements.txt
├─ README.md
└─ venv/


---

## 🚀 Possíveis Evoluções
- Criar uma **API de previsão** (FastAPI)
- Utilizar **dados reais**
- Deploy em **cloud (Azure / AWS)**
- Pipeline automatizado de ML

---

## 👩‍💻 Autora
Projeto desenvolvido para fins de **aprendizado e portfólio em Machine Learning**.
