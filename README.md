# 📊 Linguistic Acquisition Analysis: Temporal Expressions in Child Speech

![Project Status](https://img.shields.io/badge/Status-Complete-green)
![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Plotly](https://img.shields.io/badge/Visualizations-Plotly-orange)

[🇬🇧 English Version](#-about-the-project) | [🇧🇷 Versão em Português](#-sobre-o-projeto)

---

## 📖 About the Project

This project explores the acquisition of temporal expressions (words related to time like "now", "tomorrow", "yesterday") in young children. By analyzing longitudinal corpora of child-parent interactions, this analysis investigates the relationship between **Child Directed Speech (CDS)** (what parents say) and **Child Speech (CHI)** (what children say).

This repository serves as a **Data Analyst Portfolio** project, demonstrating skills in:
- **Data Processing**: Parsing and cleaning CHILDES chat format transcripts using RegEx and Python.
- **Statistical Analysis**: Implementing Correlation and Regression (OLS) models to test linguistic hypotheses.
- **Data Visualization**: Creating interactive, publication-quality charts using **Plotly** and **Seaborn**.
- **Automated Reporting**: Generates statistical summaries and visual artifacts automatically.

### ❓ Key Research Questions

1.  **Input Frequency**: Is there a correlation between how often parents use time words and how often children use them?
2.  **Age of Acquisition**: How does the frequency of temporal expressions change as the child grows (measured in months)?
3.  **Cross-Linguistic Comparison**: Do these patterns hold true across different languages (e.g., Brazilian Portuguese vs. English)?

### 📂 Data Sources

The analysis uses data from the **CHILDES (Child Language Data Exchange System)** database.
Two specific corpora are analyzed:
*   **AlegreLong Corpus**: Longitudinal data for **Brazilian Portuguese**.
*   **Weist Corpus**: Longitudinal data for **English**.

Required directory structure:
```
/corpus
    /AlegreLong
        /Alexandra
        /Camila
        ...
    /Weist
        /Matt
        /Emily
        ...
```

### 🛠️ Methodology

1.  **Extraction**: Python script iterates through `.cha` files, extracting dialogue lines for Target Child (CHI) and Caretakers (CDS).
2.  **Tokenization & Cleaning**: 
    - Text is normalized (removing interruptions, special codes).
    - **Regular Expressions (Regex)** are used to identify and count specific temporal markers (e.g., *'ontem'*, *'amanhã'*, *'now'*, *'later'*).
3.  **Metrics**:
    - **Frequency per 1000 words**: Normalized frequency to account for varying session lengths.
4.  **Statistical Modeling**:
    - **Pearson/Spearman Correlations**: To assess linear relationships.
    - **Multiple Linear Regression (OLS)**: To model Child Frequency as a function of CDS Frequency and Age.

### 📊 Visualizations

The project generates interactive HTML plots to allow deep exploration of the data:

*   **Scatter Plots (Interactive)**: 
    *   *Input vs. Output*: Visualizing the strong correlation between parent and child usage.
    *   *Developmental Trajectory*: Tracking usage frequency over age (months).
*   **Bar Charts**: Top 10 most frequent temporal expressions for each child and aggregate groups.
*   **Comparison Charts**: Side-by-side analysis of Portuguese and English and data.

### 🚀 How to Run

#### Prerequisites
Ensure you have the following Python libraries installed:
```bash
pip install pandas numpy matplotlib seaborn plotly statsmodels
```

#### Execution
1.  Clone this repository.
2.  Ensure your `corpus` folder is placed in the root directory (or modify the path in the notebook).
3.  Open the Jupyter Notebook:
    ```bash
    jupyter notebook LL264.ipynb
    ```
4.  Run all cells. The script will:
    - Process all `.cha` files.
    - Generate CSV summaries in `corpus/{CorpusName}Stats`.
    - Save interactive HTML plots in the output directories.

### 📈 Sample Insights

*   **Correlation**: There is typically a significant positive correlation (r > 0.5) between CDS frequency and Children's frequency of temporal words.
*   **Lexical Growth**: The variety of temporal expressions expands rapidly between 24 and 36 months.
*   **Common Words**: Deictic terms (e.g., "now/agora", "today/hoje") appear earlier than sequential terms (e.g., "after/depois").

### 💻 Tech Stack

*   **Language**: Python
*   **Libraries**: 
    *   **Pandas**: Data manipulation and aggregation.
    *   **Plotly Express**: Interactive data visualization.
    *   **Statsmodels**: Regression and statistical testing.
    *   **Seaborn/Matplotlib**: Static plotting components.
    *   **Re**: Regular expression pattern matching.

---

## 📖 Sobre o Projeto

Este projeto explora a aquisição de expressões temporais (palavras relacionadas ao tempo como "agora", "amanhã", "ontem") em crianças pequenas. Ao analisar corpora longitudinais de interações criança-pais, esta análise investiga a relação entre a **Fala Dirigida à Criança (CDS)** (o que os pais dizem) e a **Fala da Criança (CHI)**.

Este repositório serve como um projeto de **Portfólio de Analista de Dados**, demonstrando habilidades em:
- **Processamento de Dados**: Parsing e limpeza de transcrições no formato CHILDES chat usando RegEx e Python.
- **Análise Estatística**: Implementação de modelos de Correlação e Regressão (OLS) para testar hipóteses linguísticas.
- **Visualização de Dados**: Criação de gráficos interativos com qualidade de publicação usando **Plotly** e **Seaborn**.
- **Relatórios Automatizados**: Geração automática de resumos estatísticos e artefatos visuais.

### ❓ Questões de Pesquisa

1.  **Frequência do Input**: Existe uma correlação entre a frequência com que os pais usam palavras temporais e a frequência com que as crianças as usam?
2.  **Idade de Aquisição**: Como a frequência de expressões temporais muda à medida que a criança cresce (medida em meses)?
3.  **Comparação Translinguística**: Esses padrões se mantêm em diferentes idiomas (ex: Português Brasileiro vs. Inglês)?

### 📂 Fontes de Dados

A análise utiliza dados do banco de dados **CHILDES (Child Language Data Exchange System)**.
Dois corpora específicos são analisados:
*   **Corpus AlegreLong**: Dados longitudinais para **Português Brasileiro**.
*   **Corpus Weist**: Dados longitudinais para **Inglês**.

Estrutura de diretório necessária:
```
/corpus
    /AlegreLong
        /Alexandra
        /Camila
        ...
    /Weist
        /Matt
        /Emily
        ...
```

### 🛠️ Metodologia

1.  **Extração**: Script Python itera por arquivos `.cha`, extraindo linhas de diálogo para a Criança Alvo (CHI) e Cuidadores (CDS).
2.  **Tokenização & Limpeza**: 
    - O texto é normalizado (removendo interrupções, códigos especiais).
    - **Expressões Regulares (Regex)** são usadas para identificar e contar marcadores temporais específicos.
3.  **Métricas**:
    - **Frequência por 1000 palavras**: Frequência normalizada para considerar tempos de sessão variados.
4.  **Modelagem Estatística**:
    - **Correlações de Pearson/Spearman**: Para avaliar relações lineares.
    - **Regressão Linear Múltipla (OLS)**: Para modelar a Frequência da Criança em função da Frequência do CDS e da Idade.

### 📊 Visualizações

O projeto gera gráficos HTML interativos para permitir uma exploração profunda dos dados:

*   **Gráficos de Dispersão (Interativos)**: 
    *   *Input vs. Output*: Visualizando a forte correlação entre o uso dos pais e da criança.
    *   *Trajetória de Desenvolvimento*: Acompanhando a frequência de uso ao longo da idade (meses).
*   **Gráficos de Barras**: Top 10 expressões temporais mais frequentes para cada criança e grupos agregados.
*   **Gráficos de Comparação**: Análise lado a lado de dados em Português e Inglês.

### 🚀 Como Executar

#### Pré-requisitos
Certifique-se de ter as seguintes bibliotecas Python instaladas:
```bash
pip install pandas numpy matplotlib seaborn plotly statsmodels
```

#### Execução
1.  Clone este repositório.
2.  Certifique-se de que sua pasta `corpus` esteja na raiz do diretório.
3.  Abra o Jupyter Notebook:
    ```bash
    jupyter notebook LL264.ipynb
    ```
4.  Execute todas as células. O script irá:
    - Processar todos os arquivos `.cha`.
    - Gerar resumos CSV em `corpus/{CorpusName}Stats`.
    - Salvar gráficos HTML interativos nos diretórios de saída.

### 📈 Insights de Exemplo

*   **Correlação**: Normalmente existe uma correlação positiva significativa (r > 0.5) entre a frequência do CDS e a frequência de palavras temporais das crianças.
*   **Crescimento Lexical**: A variedade de expressões temporais expande rapidamente entre 24 e 36 meses.
*   **Palavras Comuns**: Termos dêiticos (ex: "agora", "hoje") aparecem mais cedo do que termos sequenciais (ex: "depois").

### 💻 Stack Tecnológico

*   **Linguagem**: Python
*   **Bibliotecas**: 
    *   **Pandas**: Manipulação e agregação de dados.
    *   **Plotly Express**: Visualização de dados interativa.
    *   **Statsmodels**: Regressão e testes estatísticos.
    *   **Seaborn/Matplotlib**: Componentes de plotagem estática.
    *   **Re**: Correspondência de padrões com expressões regulares.

---

*Autor: Antonio Morais*
