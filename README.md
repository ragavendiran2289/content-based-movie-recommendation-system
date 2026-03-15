# Movie Recommendation System (NLP + TF-IDF)

This project is a **Content-Based Movie Recommendation System** built
using **Natural Language Processing (NLP)** and **TF-IDF
vectorization**.
It recommends movies based on a user-provided storyline.

The application is deployed using **Streamlit** to provide an
interactive web interface.

------------------------------------------------------------------------

## Features

-   NLP-based text preprocessing
-   TF-IDF vectorization for movie storyline analysis
-   Cosine similarity for recommendation
-   Streamlit web interface
-   Returns top 5 similar movies

------------------------------------------------------------------------

## How It Works

1.  Movie storylines are cleaned using NLP techniques:

    -   Lowercasing
    -   Removing special characters
    -   Removing stopwords

2.  Cleaned text is converted into vectors using **TF-IDF**.

3.  When a user enters a storyline:

    -   The text is cleaned
    -   Transformed using the saved TF-IDF model
    -   Compared with the dataset using **Cosine Similarity**

4.  The system returns the **Top 5 most similar movies**.

------------------------------------------------------------------------

## Project Structure

    project-folder/
    │
    ├── IMDB_UI.py                 # Streamlit application
    ├── recomendation.ipynb        # Model building notebook
    ├── webpage scrapping.ipynb    # Data scraping notebook
    ├── cleaned_movies_nlp.csv     # Cleaned movie dataset
    ├── tfidf_model.pkl            # Saved TF-IDF model
    ├── tfidf_matrix.pkl           # TF-IDF matrix
    ├── requirements.txt           # Python dependencies
    └── README.md                  # Project documentation

------------------------------------------------------------------------

## Installation

### 1. Clone the Repository

``` bash
git clone https://github.com/yourusername/movie-recommendation-system.git
cd movie-recommendation-system
```

### 2. Install Dependencies

``` bash
pip install -r requirements.txt
```

------------------------------------------------------------------------

## ▶️ Run the Application

``` bash
streamlit run IMDB_UI.py
```

Then open the URL shown in the terminal (usually):

    http://localhost:8501

------------------------------------------------------------------------

## Example Usage

Enter a movie storyline like:

    A group of astronauts travel through space to save humanity.

The system will recommend **5 similar movies**.

------------------------------------------------------------------------

## Technologies Used

-   Python
-   Streamlit
-   Pandas
-   Scikit-learn
-   NLTK
-   TF-IDF Vectorizer
-   Cosine Similarity

------------------------------------------------------------------------

## Machine Learning Technique

**Content-Based Filtering**

Uses: - TF-IDF vectorization - Cosine similarity between storyline
vectors

------------------------------------------------------------------------

## Future Improvements

-   Add movie posters
-   Add IMDB ratings
-   Improve UI design
-   Deploy on Streamlit Cloud
-   Add hybrid recommendation system

------------------------------------------------------------------------

## Author

Ragavendiran
