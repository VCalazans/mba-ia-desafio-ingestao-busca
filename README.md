# Desafio MBA Engenharia de Software com IA - Full Cycle

## Como testar o projeto

1. **Instale as dependências**
   
	No diretório do projeto:
	```bash
	pip install -r requirements.txt
	```

2. **Configure as variáveis de ambiente**
   
	Crie um arquivo `.env` na raiz do projeto com as variáveis necessárias, por exemplo:
	```env
	OPENAI_API_KEY=token_openai
	PGVECTOR_URL=postgresql://usuario:senha@localhost:5432/seubanco
	PGVECTOR_COLLECTION=nome_da_colecao
	PDF_PATH=caminho\para\seu\documento.pdf 
	```

3. **Ingestão dos dados**
   
	Execute o script de ingestão para carregar o PDF no banco vetorial:
	```bash
	cd src
	py ingest.py
	```


4. **Interagir com o Chatbot**
   
	Execute o chat para fazer perguntas ao modelo:
	```bash
	cd src
	py chat.py
	```

	Digite sua pergunta no terminal. O chatbot utiliza internamente o search.py para buscar as respostas.


Pronto! O projeto estará pronto para testes.