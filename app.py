import streamlit as st
import pickle
import pandas as pd
import requests

def fetch_poster(movie_id):
    response = requests.get(
        f'https://api.themoviedb.org/3/movie/{movie_id}?api_key=257026c15d46f5329bbf1bf3f42bf45b')
    data= response.json()
    return 'https://image.tmdb.org/t/p/w185/'+data['poster_path']

def recommend(movie):
    movie_index = movies[movies.title == movie].index[0]
    distances = similarity[movie_index]
    similar_movies = sorted(list(enumerate(distances)),
                            reverse=True, key=lambda x: x[1])[0:6]

    recommended_movies= []
    recommended_movies_posters= []
    for i in similar_movies:
        # print(i[0])
        # fetch poster from API
        movie_id = movies.iloc[i[0]].id
        recommended_movies_posters.append(fetch_poster(movie_id))
        recommended_movies.append(movies.iloc[i[0]].title)

    return recommended_movies, recommended_movies_posters

movies_dict= pickle.load(open('movie_dict.pkl', 'rb'))
similarity= pickle.load(open('similarity.pkl', 'rb'))
movies= pd.DataFrame(movies_dict)
movies_list= movies.title.values

st.title("Movie Recommender System")
st.header("- Deepankar Sharma")

selected_movie_name= st.selectbox(
    'Select a movie..',
    movies_list
)

if st.button('Recommend'):
    recommendations, posters= recommend(selected_movie_name)
    # for i in recommendations:
    #     st.write(i)
    col0, col1, col2, col3, col4, col5= st.columns(6)

    with col0:
        st.text(recommendations[0])
        st.image(posters[0])

    with col1:
        st.text(recommendations[1])
        st.image(posters[1])

    with col2:
        st.text(recommendations[2])
        st.image(posters[2])

    with col3:
        st.text(recommendations[3])
        st.image(posters[3])

    with col4:
        st.text(recommendations[4])
        st.image(posters[4])

    with col5:
        st.text(recommendations[5])
        st.image(posters[5])