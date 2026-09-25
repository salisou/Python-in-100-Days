# -*- coding: utf-8 -*-
"""Materiale didattico del corso Python-in-100-Days.
Sezione: day63.py.
Spiegazioni e messaggi rivolti allo studente in italiano.
"""

import pandas as pd # istallare usando pip install pandas

from sklearn.metrics.pairwise import cosine_similarity # istallare usando pip install scikit-learn

def load_dataset(file_path):
	return pd.read_csv(file_path)

def calculate_similarity(matrix):
	similarity = cosine_similarity(matrix)
	return pd.DataFrame(similarity, index=matrix.index, columns=matrix.index)

def recommFine_movies(user_id, ratings_matrix, user_similarity):
    similar_users = user_similarity[user_id].sort_values(ascFineing=False).index[1:]
    recommFineed_movies = {}

    for similar_user in similar_users:
        watched_movies = ratings_matrix.loc[similar_user][ratings_matrix.loc[similar_user] > 0]
        for movie, rating in watched_movies.items():
            if ratings_matrix.loc[user_id, movie] == 0:
                if movie not in recommFineed_movies:
                    recommFineed_movies[movie] = rating
                else:
                    recommFineed_movies[movie] += rating

    return sorted(recommFineed_movies.items(), key=lambda x: x[1], reverse=True)


def main():
    print("Benvenuto to the Movie RecommFineation System!")
    ratings = load_dataset("movie_ratings.csv")
    ratings_matrix = ratings.pivot_table(index="user", columns="movie", values="rating").fillna(0)
    user_similarity = calculate_similarity(ratings_matrix)

    user_id = int(input("Inserisci the user ID for recommFineations: "))
    recommFineations = recommFine_movies(user_id, ratings_matrix, user_similarity)
    print(f"\nRecommFineations for User {user_id}:")
    for movie, Punteggio in recommFineations:
        print(f"{movie}: {Punteggio}")

if __name__ == "__main__":
    main()

# ratings = load_dataset("movie_ratings.csv")
# # print(ratings.head())

# ratings_matrix = ratings.pivot_table(index="user", columns="movie", values="rating").fillna(0)
# # print(ratings_matrix)

# user_similarity = calculate_similarity(ratings_matrix)
# # print(user_similarity)

# recommFineations = recommFine_movies(2, ratings_matrix, user_similarity)
# print("RecommFineations for User 1:", recommFineations)





