from openai import OpenAI
from utils.rag import scrape_article, chunk_text, vectorize_text, find_most_similar, ask_question


def get_chatgpt_response(api_key, model, temperature, system_content, user_message):
    OPENAI_API_KEY = api_key
    client = OpenAI(
        api_key=OPENAI_API_KEY,
    )

    response = client.chat.completions.create(
        model=model,
        temperature=temperature,
        messages=[
            {"role": "system", "content": system_content},
            {"role": "user", "content": user_message},
        ],
    )
    return response.choices[0].message.content


def get_chatgpt_response_rag(user_message,urls):
    chunk_size = 400
    overlap = 50
    article_text = scrape_article(urls)
    text_chunks = chunk_text(article_text, chunk_size, overlap)
    vectors = [vectorize_text(doc) for doc in text_chunks]
    question = user_message
    question_vector = vectorize_text(question)
    similar_document = find_most_similar(question_vector, vectors, text_chunks)
    answer = ask_question(question, similar_document)
    return answer

