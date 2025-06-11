# Sistema de Monitoramento Pessoal 2.0 - Documentação / Personal Monitoring System 2.0 - Documentation

## Descrição Geral / General Description

Este projeto consiste em um sistema para monitoramento pessoal de sustentabilidade. O sistema permite ao usuário registrar e acompanhar dados relacionados ao consumo de água, energia elétrica, geração de resíduos e gastos pessoais. Além disso, ele oferece funcionalidades para inserção, listagem, atualização e exclusão desses dados, assim como o cálculo de médias para análise do consumo.

This project consists of a personal sustainability monitoring system. The system allows users to record and track data related to water consumption, electricity usage, waste generation, and personal expenses. Additionally, it provides functionalities for inserting, listing, updating, and deleting these records, as well as calculating averages for consumption analysis.

O sistema foi desenvolvido em Python e utiliza um banco de dados MySQL para armazenamento persistente dos dados. Ele é voltado para usuários que desejam monitorar seus hábitos e impactos ambientais com o objetivo de melhorar sua sustentabilidade pessoal.

The system is developed in Python and uses a MySQL database for persistent data storage. It is aimed at users who want to monitor their habits and environmental impacts to improve their personal sustainability.

## Estrutura do Código / Code Structure

- `main.py` (ou arquivo principal): arquivo que contém o ponto de entrada do sistema. / `main.py` (or main file): contains the system entry point.
- Módulos para cada área monitorada (água, energia, resíduos, gastos), que incluem funções para: / Modules for each monitored area (water, energy, waste, expenses), including functions for:
  - Inserção de novos registros; / Insert new records;
  - Listagem dos registros existentes; / List existing records;
  - Alteração e exclusão de registros; / Update and delete records;
  - Cálculo da média dos consumos; / Calculate consumption averages;
- Arquivo de configuração para conexão com o banco de dados MySQL; / Configuration file for MySQL database connection;
- Scripts SQL para criação das tabelas e inserção inicial de dados (caso estejam presentes no repositório); / SQL scripts to create tables and initial data inserts (if included in the repository);
- Utilização de bibliotecas para conexão com MySQL e manipulação dos dados. / Use of libraries for MySQL connection and data handling.

## Dependências / Dependencies

Para executar o sistema em sua máquina, é necessário instalar as seguintes dependências: / To run the system on your machine, you need to install the following dependencies:

- Python 3.7 ou superior; / Python 3.7 or higher;
- Biblioteca `mysql-connector-python` para conexão com o banco de dados MySQL; / `mysql-connector-python` library to connect with MySQL database;
- Outras bibliotecas padrão do Python, como `os`, `sys` (geralmente já inclusas na instalação padrão). / Other standard Python libraries like `os`, `sys` (usually included by default).

### Instalando as dependências / Installing dependencies

Use o gerenciador de pacotes `pip` para instalar as dependências: / Use the `pip` package manager to install dependencies:

```bash
pip install mysql-connector-python
```

## Configuração do Banco de Dados / Database Configuration

1. Instale e configure um servidor MySQL (exemplo: MySQL Community Server). / Install and configure a MySQL server (e.g., MySQL Community Server).
2. Crie um banco de dados para o sistema, por exemplo `monitoramento_pessoal`. / Create a database for the system, e.g., `monitoramento_pessoal`.
3. Execute os scripts SQL fornecidos no repositório para criar as tabelas necessárias (se existirem). / Run the provided SQL scripts to create the necessary tables (if available).
4. Configure as credenciais de acesso ao banco no arquivo de configuração do projeto (exemplo: host, usuário, senha e nome do banco). / Configure the database access credentials in the project configuration file (host, user, password, and database name).

## Como Rodar o Sistema / How to Run the System

1. Certifique-se de que o banco de dados está configurado e rodando. / Make sure the database is configured and running.
2. Atualize as configurações de conexão no código-fonte para refletir seus dados do banco. / Update the connection settings in the source code with your database credentials.
3. Execute o arquivo principal do sistema com Python: / Run the main system file using Python:

```bash
python main.py
```

4. Utilize as opções do menu para inserir, listar, alterar ou excluir dados, bem como calcular médias. / Use the menu options to insert, list, update or delete data, as well as calculate averages.

## Observações Finais / Final Remarks

- Recomenda-se o uso de um ambiente virtual Python para evitar conflitos de dependências. / It is recommended to use a Python virtual environment to avoid dependency conflicts.
- Caso haja necessidade, instale o `virtualenv` e crie um ambiente virtual: / If needed, install `virtualenv` and create a virtual environment:

```bash
pip install virtualenv
virtualenv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```

- Para desativar o ambiente virtual, use o comando `deactivate`. / To deactivate the virtual environment, use the command `deactivate`.

---

Qualquer dúvida ou problema, verifique as mensagens de erro para identificar possíveis ajustes nas configurações do banco de dados ou nas dependências Python. /

If you encounter any issues, check error messages to identify necessary adjustments in database configuration or Python dependencies.

---

# Autor e Contato / Author and Contact

- Desenvolvedor: **Rnchx** / Developer: **Rnchx**
- Repositório original: https://github.com/Rnchx/Sistema-de-Monitoramento-Pessoal-2.0.git

---
