import streamlit as st
import pandas as pd
import pickle
import re
import nltk
from nltk.corpus import stopwords
from sklearn.metrics.pairwise import cosine_similarity

nltk.download("stopwords")
stop_words = set(stopwords.words("english"))

# Load pickle files
tfidf = pickle.load(open("tfidf_model.pkl", "rb"))
tfidf_matrix = pickle.load(open("tfidf_matrix.pkl", "rb"))
df = pd.read_csv("cleaned_movies_nlp.csv")


def clean_text(text):

    text = text.lower()
    text = re.sub(r"[^a-zA-Z ]", "", text)

    words = text.split()
    words = [w for w in words if w not in stop_words]

    return " ".join(words)


def recommend_movies(storyline):

    cleaned = clean_text(storyline)

    input_vector = tfidf.transform([cleaned])

    similarity_scores = cosine_similarity(input_vector, tfidf_matrix)

    scores = list(enumerate(similarity_scores[0]))

    sorted_scores = sorted(scores, key=lambda x: x[1], reverse=True)

    top_movies = sorted_scores[:5]

    results = []

    for i in top_movies:
        results.append(df.iloc[i[0]]["Movie Name"])

    return results


# Streamlit UI
st.title("🎬 Movie Recommendation System")

story = st.text_area("Enter Movie Storyline")

if st.button("Recommend Movies"):

    movies = recommend_movies(story)

    st.subheader("Recommended Movies")

    for m in movies:
        st.write("🎥", m)