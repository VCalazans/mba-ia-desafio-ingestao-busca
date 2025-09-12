import os
from dotenv import load_dotenv

from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_postgres import PGVector
from langchain.prompts import PromptTemplate

load_dotenv()


question_template = PromptTemplate(
    input_variables=["contexto", "pergunta"],
    template="""
CONTEXTO:
{contexto}

REGRAS:
- Responda somente com base no CONTEXTO.
- Se a informação não estiver explicitamente no CONTEXTO, responda:
  "Não tenho informações necessárias para responder sua pergunta."
- Nunca invente ou use conhecimento externo.
- Nunca produza opiniões ou interpretações além do que está escrito.

EXEMPLOS DE PERGUNTAS FORA DO CONTEXTO:
Pergunta: "Qual é a capital da França?"
Resposta: "Não tenho informações necessárias para responder sua pergunta."

Pergunta: "Quantos clientes temos em 2024?"
Resposta: "Não tenho informações necessárias para responder sua pergunta."

Pergunta: Qual o faturamento da Empresa SuperTechIABrazil?
Resposta: O faturamento foi de 10 milhões de reais.

Pergunta: Faturamento da SuperTechIABrazil?
Resposta: O faturamento foi de 10 milhões de reais.

Pergunta: "Você acha isso bom ou ruim?"
Resposta: "Não tenho informações necessárias para responder sua pergunta."

PERGUNTA DO USUÁRIO:
{pergunta}

RESPONDA A "PERGUNTA DO USUÁRIO"
""")


model = ChatOpenAI(model="gpt-5-nano", temperature=0.5)
chainQuestion = question_template | model

embeddings = OpenAIEmbeddings(model=os.getenv("OPENAI_MODEL","text-embedding-3-small"))

store = PGVector(
        embeddings=embeddings,
        collection_name=os.getenv("PG_VECTOR_COLLECTION_NAME"),
        connection=os.getenv("DATABASE_URL"),
        use_jsonb=True,
)


def search_prompt(question=None):
    if not question:
        raise ValueError("A pergunta não pode ser vazia.")

    try:
        results = store.similarity_search(question, k=10)
    except Exception as e:
        return f"Erro ao buscar contexto: {str(e)}"

    contexto = "\n\n".join([f"- {doc.page_content.strip()}" for doc in results])

    try:
        resposta = chainQuestion.invoke({"contexto": contexto, "pergunta": question})
        return resposta.content
    except Exception as e:
        return f"Erro ao gerar resposta: {str(e)}"


