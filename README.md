
# Finansys💰 - Controle suas finanças, conquiste seus sonhos.

O **Finansys** é um sistema de gestão financeira criado para auxiliar usuários a gerenciar suas finanças de maneira prática e organizada. Os recursos principais incluem:

- **Registro de Gastos**: Permite inserir e categorizar despesas e receitas.
- **Definição de Metas**: Ajuda a estabelecer objetivos financeiros e monitorar o progresso.
- **Relatórios Detalhados**: Exibe relatórios de despesas, receitas e saldo.
- **Dashboards**: Painéis gráficos para mostrar a situação financeira atual e indicadores de progresso nas metas.

### Tecnologias Utilizadas

- **Frontend**: Desenvolvido com Vue.js (ou Vite) para uma interface interativa e responsiva.
- **Backend**: FastAPI, proporcionando uma API robusta e fácil de escalar.
- **Banco de Dados**: SQLite (banco de dados leve e de fácil configuração).
- **Autenticação**: JWT para autenticação segura de usuários.

---

### Instalação de Dependências e Execução do Projeto

Aqui está o guia para instalar e rodar o projeto localmente, sem necessidade de Docker.

#### Pré-requisitos

- **Node.js e npm**: Necessário para o frontend. Baixe em [https://nodejs.org](https://nodejs.org).
- **Python 3.8+ e pip**: Necessário para o backend.

#### Passo 1: Clonar o Repositório

Clone o repositório do projeto e entre no diretório do projeto:
```bash
git clone https://github.com/usuario/finansys.git
cd finansys
```

#### Passo 2: Backend - Instalação e Configuração

1. **Configurar Ambiente Virtual**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # No Windows: venv\Scripts\activate
   ```

2. **Instalar Dependências do Backend**:
   ```bash
   pip install -r backend/requirements.txt
   ```

3. **Configurar o Banco de Dados**:
   - O projeto utiliza SQLite, então ele criará automaticamente o banco de dados ao rodar as migrações. Apenas verifique se o arquivo `.env` em `backend` está configurado corretamente para o ambiente SQLite.


4. **Iniciar o Servidor Backend**:
   ```bash
   uvicorn src.main:app --reload
   ```

   O backend estará disponível em `http://127.0.0.1:8000`.

#### Passo 3: Frontend - Instalação e Configuração

1. **Instalar Dependências do Frontend**:
   ```bash
   cd ../frontend
   npm install
   ```

2. **Iniciar o Servidor de Desenvolvimento**:
   ```bash
   npm run dev
   ```

   O frontend estará acessível em `http://localhost:3000` (ou na porta configurada).

#### Passo 4: Testar o Projeto

- **API Documentation**: Acesse `http://127.0.0.1:8000/docs` para visualizar a documentação automática da API gerada pelo Swagger.
- **Interface Web**: Acesse `http://localhost:3000` para testar o frontend e interagir com o sistema.

---