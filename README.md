# Movie-Recommendation-System

![images](https://media-hosting.imagekit.io/d4bcad6b9b2b40d4/Screenshot_20250504_202239.png?Expires=1840978426&Key-Pair-Id=K2ZIVPTIP2VGHC&Signature=EJgg1RY4FaYAJkcNyw8wOif2C~X-f-cM~ATdMCuY3SV3hukICAVn4Irz7JjHKLD5Ir0kcVehoJ2PyqWleEcCIZ1rNCOcJQJw1MsW6mjxhY4KpqRbl186xcR9cPq80R23PWuceoTl1cg53RA1HwZ-pZMBvqXbvCFyEAoGnqQP2jAeDKwVfMLuilSDVTumQotitDgtgpuwMQMO7IPxO8y4oBocv0FsDpPK5loCute0GA~cH8u1OQlbFUv0gR2O3bXT70g1k-kGkcW37WgEkHbL~KRC5qfjMRAGogHRVpd4eelN~iqBu5~OcpZgPPDxDKxpDEbVjng23Fyae95IXplHkw) 


A machine learning-based movie recommendation system that suggests similar movies using text-based features and CountVectorizer.

---

##  Features

- Recommends similar movies using content-based filtering
- Utilizes CountVectorizer for feature extraction
- Calculates similarity using cosine similarity
- Clean and efficient text preprocessing
- Simple and interpretable machine learning pipeline

---

##  Dataset

This project uses the imdb 1000 dataset.

**Main columns used:**
- `Series_Title`
- `overview`
- `Star1			`
- `Star2`
- `Star3`

---

##  Tech Stack

- **Python**
- **Pandas**
- **Scikit-learn** (CountVectorizer, cosine similarity)
- **Numpy**
---

##  How It Works

1. **Data Cleaning** – Handles null values, formats text fields.
2. **Feature Engineering** – Merges fields like overview, genere, cast, etc.
3. **Vectorization** – Uses `CountVectorizer` to create a bag-of-words model.
4. **Similarity Calculation** – Computes cosine similarity across all movie vectors.
5. **Recommendation** – Returns top 5 most similar movies to a given title.

---


