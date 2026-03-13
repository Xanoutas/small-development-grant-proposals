# scripts/allocate_funds.py

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def expand_notes_with_nlp(notes_df):
    """
    Expands the given notes DataFrame by adding more detailed explanations
    using natural language processing (NLP) tools.
    
    Parameters:
    - notes_df: DataFrame containing the original notes.
    
    Returns:
    - DataFrame with expanded notes.
    """
    # Initialize TF-IDF Vectorizer
    vectorizer = TfidfVectorizer(stop_words='english')
    
    # Fit and transform the notes content
    tfidf_matrix = vectorizer.fit_transform(notes_df['content'])
    
    # Calculate cosine similarity between notes
    similarity_matrix = cosine_similarity(tfidf_matrix)
    
    # Expand notes by adding detailed explanations
    expanded_notes = []
    for i, row in notes_df.iterrows():
        # Find the most similar note
        similar_indices = similarity_matrix[i].argsort()[:-2:-1]
        similar_notes = [notes_df.iloc[idx]['content'] for idx in similar_indices]
        
        # Combine original content with similar notes to expand
        expanded_content = row['content'] + " " + " ".join(similar_notes)
        expanded_notes.append(expanded_content)
    
    # Create a new DataFrame with expanded notes
    expanded_notes_df = notes_df.copy()
    expanded_notes_df['expanded_content'] = expanded_notes
    
    return expanded_notes_df

# Example usage
if __name__ == "__main__":
    # Sample data
    data = {
        'content': [
            "NumPy is a library for the Python programming language, adding support for large, multi-dimensional arrays and matrices, along with a large collection of high-level mathematical functions to operate on these arrays.",
            "Pandas is a software library written for data manipulation and analysis. In particular, it offers data structures and operations for manipulating numerical tables and time series.",
            "Matplotlib is a plotting library for the Python programming language and its numerical mathematics extension NumPy. It provides an object-oriented API for embedding plots into applications."
        ]
    }
    notes_df = pd.DataFrame(data)
    
    # Expand notes
    expanded_notes_df = expand_notes_with_nlp(notes_df)
    print(expanded_notes_df)