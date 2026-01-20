# 📊 Linguistic Acquisition Analysis: Temporal Expressions in Child Speech

![Project Status](https://img.shields.io/badge/Status-Complete-green)
![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Plotly](https://img.shields.io/badge/Visualizations-Plotly-orange)
![Streamlit](https://img.shields.io/badge/Dashboard-Streamlit-red)

[🇬🇧 English Version](#-about-the-project) | [🇧🇷 Versão em Português](#-sobre-o-projeto)

---

## 🇬🇧 English: Project Overview

### 📖 About the Project
This project explores the acquisition of temporal expressions (words related to time like "now", "tomorrow", "yesterday") in young children. By analyzing longitudinal corpora of child-parent interactions, this analysis investigates the relationship between **Child Directed Speech (CDS)** (what parents say) and **Child Speech (CHI)** (what children say).

This repository serves as a **Data Analyst Portfolio** project, demonstrating skills in:
- **Data Processing**: Parsing and cleaning CHILDES chat format transcripts using RegEx and Python.
- **Statistical Analysis**: Implementing Correlation and Regression (OLS) models.
- **Data Visualization**: Creating interactive charts using **Plotly** and **Streamlit**.

### ❓ Key Research Questions
1.  **Input Frequency**: Is there a correlation between parent frequency and child frequency?
2.  **Age of Acquisition**: How does frequency change as the child grows?
3.  **Cross-Linguistic Comparison**: Do patterns hold across Brazilian Portuguese and English?

### 🛠️ Methodology
1.  **Extraction**: Python script parses `.cha` files.
2.  **Cleaning**: RegEx normalizes text and identifies temporal markers.
3.  **Modeling**: Pearson/Spearman correlations and Multiple Linear Regression (OLS).

### 🖥️ Interactive Dashboard
A **Streamlit** dashboard is included for dynamic exploration:
- **Live Filters**: Select by language (PT/EN), specific children, or age range.
- **Interactive Metrics**: Real-time frequency calculations.
- **Deep Dive Stats**: Visualizations of developmental trajectories.

### 🚀 How to Run
1.  **Install Dependencies**:
    ```bash
    pip install pandas numpy matplotlib seaborn plotly statsmodels streamlit
    ```
2.  **Generate Data**: Run all cells in `LL264.ipynb`.
3.  **Launch Dashboard**:
    ```bash
    streamlit run dashboard.py
    ```

---

## 🇧🇷 Português: Sobre o Projeto

### 📖 Descrição
Este projeto explora a aquisição de expressões temporais (palavras como "agora", "amanhã", "ontem") em crianças pequenas. Analisamos a relação entre a **Fala Dirigida à Criança (CDS)** e a **Fala da Criança (CHI)**.

Este repositório é um projeto de **Portfólio de Analista de Dados**, demonstrando:
- **Processamento de Dados**: Limpeza de transcrições CHILDES usando RegEx.
- **Análise Estatística**: Modelos de Correlação e Regressão Linear (OLS).
- **Visualização**: Gráficos interativos com **Plotly** e **Streamlit**.

### ❓ Questões de Pesquisa
1.  **Frequência do Input**: Existe correlação entre o que os pais dizem e o que a criança aprende?
2.  **Idade de Aquisição**: Como a frequência evolui com a idade da criança?
3.  **Comparação Translinguística**: Os padrões são similares em Português e Inglês?

### 🛠️ Metodologia
1.  **Extração**: Parsing de arquivos `.cha` via Python.
2.  **Limpeza**: Uso de RegEx para normalização e identificação de termos.
3.  **Modelagem**: Testes de Pearson, Spearman e Regressão OLS.

### 🖥️ Dashboard Interativo
O dashboard **Streamlit** permite uma exploração dinâmica:
- **Filtros Dinâmicos**: Por idioma, criança ou faixa etária.
- **Métricas em Tempo Real**: Frequências calculadas instantaneamente.
- **Análises Visuais**: Trajetórias de desenvolvimento interativas.

### 🚀 Como Executar
1.  **Instalar Dependências**:
    ```bash
    pip install pandas numpy matplotlib seaborn plotly statsmodels streamlit
    ```
2.  **Gerar Dados**: Execute todas as células do notebook `LL264.ipynb`.
3.  **Iniciar Dashboard**:
    ```bash
    streamlit run dashboard.py
    ```

---

### 📈 Sample Insights / Exemplos de Resultados
*   **Correlation**: Strong positive correlation (r > 0.5) found between parent and child usage.
*   **Lexical Growth**: Significant expansion of temporal vocabulary between 24-36 months.
*   **Deictics Phase**: Words like "now" (agora) appear significantly earlier than relative terms like "after" (depois).

### 💻 Tech Stack
- **Python**: Pandas, NumPy, Statsmodels, SciPy.
- **Visualization**: Plotly, Seaborn, Matplotlib.
- **App Framework**: Streamlit.

---
*Author: Antonio Morais*
