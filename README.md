# Health Insurance Cross-Sell

## This project aims to order a potential client list by propensity score

#### This project was made by {cookiecutter.author}}.

# 1. Business Problem.
A empresa fictícia Insurance All é uma seguradora de saúde. Esta empresa decidiu incorporar um segundo seguro em seus serviços. A empresa resolveu disponibilizar
um seguro automotivo, e para isso precisa analisar com seus clientes quem está disposto a adquirir este porduto. O objetivo deste projeto é dado uma lista de clientes
que responderam um questionário a cerca do desejo ou não de adquirir um seguro, encontrar aqueles com maiores probabilidades de adquirir o seguro automotivo. Retornando a mesma lista de clientes, dessa vez ordenada por propensão de compra, um ranking. Desta forma, em vez de fazer ligações aleatórias em busca de clientes, a empresa pode ranquear os clientes e procurá-los de forma mais eficiente, aumentando sua taxa de sucesso na venda de seguros, assim, aumentando receita.

# 2. Business Assumptions.

# 3. Solution Strategy

My strategy to solve this challenge was:

**Step 01. Data Description:** Descrever estatísticamente os dados dos clientes para tentar entender a forma dos dados.

**Step 02. Feature Engineering:** Criar novas features com base nas já existentes, a fim de melhorar o ranqueamento.

**Step 03. Data Filtering:** Filtrar dados indesejados, sujos, faltantes, que não agregam ao objetivo.

**Step 04. Exploratory Data Analysis:** Encontrar analisando os dados peculiaridades a cerca dos clientes, na finalidade de entender melhor os clientes e melhorar o resultado.

**Step 05. Data Preparation:** Preparar os dados convertendo a formas mais adequadas que os algoritmos de machine learning possam trabalhar.

**Step 06. Feature Selection:** Selecionar as melhores features, aquelas que irão agregar ao resultado esperado, diminuindo a dimensionalidade.

**Step 07. Machine Learning Modelling:** Criação e treinamento dos modelos que farão o ranqueamento dos clientes.

**Step 08. Hyperparameter Fine Tunning:** Após encontrar o melhor modelo, ajustar os parâmetros para melhorar um pouco a capacidade de ranqueamento do algoritmo.

**Step 09. Convert Model Performance to Business Values:** Analisar como os resultados obtidos impactam o negócio da empresa.

**Step 10. Deploy Modelo to Production:** Tornar o modelo público, online, para ser utilizado pela empresa.

# 4. Top 3 Data Insights *Devido se tratar do primeiro ciclo de criação do projeto esta etapa foi adiada.*

**Hypothesis 01:**

**True/False.**

**Hypothesis 02:**

**True/False.**

**Hypothesis 03:**

**True/False.**

# 5. Machine Learning Model Applied
 - Foram criados e comparados 4 modelos de machine learning:
    - K-Nearest Neighbor Classifier
    - Logistic Regression
    - XGBoost Classifier
    - Random Forest Classifier

# 6. Machine Learning Modelo Performance

            Model	           Precision_at_k	      Recall_at_k	       F1-Score_at_k	 ROC_AUC_Score
3	XGBoost Classifier CV	    0.4112 +/- 0.0059	0.122 +/- 0.0018	0.1884 +/- 0.0028	0.8520 +/- 0.0011
2	Random Forest Classifier CV	0.3564 +/- 0.0085	0.1056 +/- 0.0026	0.1628 +/- 0.0039	0.8310 +/- 0.0015
1	K Neighbors Classifier CV	0.3362 +/- 0.0072	0.0998 +/- 0.0021	0.1540 +/- 0.0033	0.7794 +/- 0.001
0	Logistic Regression CV	    0.2872 +/- 0.0133	0.085 +/- 0.0037	0.1312 +/- 0.0058	0.8168 +/- 0.0013

- Desta forma, destaca-se o desempenho do modelo XGBoost que teve metricas de ROC UAC Score, F1-Score, Precision e Recall maiores que todos os outros, por isso foi o escolhido para dar seguimento ao projeto.

# 7. Business Results
- Os resultados do modelo de machine learning aplicado a valores hipotéticos mostrou ser 3,36 vezes mais eficiente que um modelo de ligações aleatórias. Considerando-se 5 mil ligações.

# 8. Conclusions
- Desta forma, podemos averiguar que utilizar um modelo de machine lerning adequado pode aumentar o faturamento de uma empresa

# 9. Lessons Learned
- Existem métricas diferentes para tipos de classificações diferentes. Desta vez como o objetivo era ranquear, podemos aprender a utilizar precision at k e recall at k.
- Estudar o modelo de negócios de uma seguradora.

# 10. Next Steps to Improve
Como próximos passos podemos incluir e/ou mudar algumas coisas:
- Balancear os dados.
- Criar features.
- Fazer uma análise exploratória para ajudar a selecionar melhor as features.
- Estudar a aplicação de PCA.
- Fazer transformações de dados diferentes para testar.

# LICENSE

# All Rights Reserved - Comunidade DS 2021











