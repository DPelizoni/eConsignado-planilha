# Sistema de Processamento eConsignado 🚀

Este sistema automatiza o processamento de planilhas financeiras do eConsignado, realizando filtragem de CNPJ, transformações de dados e geração de arquivos formatados seguindo layouts específicos.

## 📋 Funcionalidades

- **Processamento em Lote (Bulk Processing)**: Selecione múltiplas planilhas de origem simultaneamente e receba todas processadas em um único arquivo ZIP.
- **Fidelidade de Layout**: Preserva cabeçalhos, cores, fórmulas e estilos das primeiras 6 linhas do modelo padrão (`Planilha finalizada.xlsx`).
- **Replicação Automática de Estilos**: Garante que todos os registros (independente da quantidade) herdem a formatação e fórmulas das linhas de referência.
- **Lógica Inteligente de Metadados**:
  - **B1 (Competência)**: Preenchimento automático no formato `dd/mm/aaaa`.
  - **B2 (Razão Social)**: Identificação automática da empresa.
  - **B3 (CNPJ/CPF)**: Prioriza o CNPJ da Matriz (`0001`). Caso não exista, insere um aviso para preenchimento manual.
- **Nomenclatura Dinâmica**: Arquivos gerados com o nome: `[Razão Social]_eConsignado - Planilha_[mm-aaaa].xlsx`.

## 🛠️ Tecnologias Utilizadas

- **Python 3.12+**
- **Streamlit**: Interface web moderna e intuitiva.
- **Pandas**: Motor de alta performance para manipulação de dados.
- **Openpyxl**: Manipulação cirúrgica de arquivos Excel (estilos, fórmulas e células).
- **Pytest**: Suíte de testes automatizados para garantir estabilidade.

## 🚀 Como Iniciar

### Pré-requisitos
- Python instalado no sistema.
- O arquivo `Planilha finalizada.xlsx` deve estar na raiz do projeto para servir como modelo.

### Instalação e Uso
1. Clone o repositório ou baixe a pasta do projeto.
2. Utilize o atalho **`Rodar_Aplicacao.bat`** para iniciar o sistema automaticamente (ele criará o ambiente virtual e instalará as dependências no primeiro uso, se necessário).
3. O navegador abrirá a interface na URL `http://localhost:8501`.

## 🧪 Testes Automatizados

Para garantir que a lógica de negócio (especialmente a regra do CNPJ 0001 e formatação de datas) permaneça íntegra, execute:
```powershell
.\venv\Scripts\pytest tests.py
```

## 📁 Estrutura do Projeto

- `app.py`: Interface do usuário (Streamlit).
- `processor.py`: Lógica central de processamento e persistência de dados.
- `validators.py`: Regras de validação e formatação (CNPJ/Datas).
- `tests.py`: Suite de testes automatizados.
- `.gitignore`: Configurado para proteger dados sensíveis e planilhas reais.

## 📄 Licença

Este projeto é de uso privado para automação de controle de empréstimos consignados (eConsignado).
