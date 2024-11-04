import requests
from bs4 import BeautifulSoup
from openai import OpenAI
import os
import boto3
import zipfile
import sys
import numpy as np
import scipy


OPENAI_API_KEY = os.environ["OPENAI_API_KEY"]
client = OpenAI(
    api_key=OPENAI_API_KEY,
)

def scrape_article(urls):
    joined_text = ""
    for url in urls:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        text_nodes = soup.find_all("div")
        joined_text += "".join(t.text.replace("\t", "").replace("\n", "") for t in text_nodes)

    return joined_text


def chunk_text(text, chunk_size, overlap):
    chunks = []
    start = 0
    while start + chunk_size <= len(text):
        chunks.append(text[start:start + chunk_size])
        start += (chunk_size - overlap)
    if start < len(text):
        chunks.append(text[-chunk_size:])
    return chunks


def vectorize_text(text):
    response = client.embeddings.create(
        input = text,
        model = "text-embedding-3-small"
    )
    return response.data[0].embedding


def cosine_similarity_manual(vector_a, vector_b):
    dot_product = np.dot(vector_a, vector_b)
    norm_a = np.linalg.norm(vector_a)
    norm_b = np.linalg.norm(vector_b)
    return dot_product / (norm_a * norm_b)

def find_most_similar(question_vector, vectors, documents):
    similarities = []
    for index, vector in enumerate(vectors):
        similarity = cosine_similarity_manual(question_vector, vector)
        similarities.append([similarity, index])
    similarities.sort(reverse=True, key=lambda x: x[0])
    top_documents = [documents[index] for similarity, index in similarities[:2]]
    return top_documents


def ask_question(question, context):
    prompt = f'''
    下記の参考情報をもとにユーザーの質問に回答してください。
    [ユーザーの質問]
    {question}
    [参考情報]
    {context}
    '''
    response = client.chat.completions.create(
        # model="ft:gpt-3.5-turbo-0125:personal:inn-faq-v1:AOL3qfFi",
        model="gpt-4o",
        temperature=0,
        messages=[
            {"role": "system", "content": prompt},
            {"role": "user", "content": question},
        ],
    )
    return response.choices[0].message.content



