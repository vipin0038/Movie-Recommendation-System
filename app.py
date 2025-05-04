import pickle
import streamlit as st
import requests
from PIL import Image
import requests
from io import BytesIO


movies = pickle.load(open('movie_list.pkl','rb'))
similarity = pickle.load(open('similarity.pkl','rb'))



def recommend(movie):
    index = movies[movies['Series_Title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    for i in distances[1:6]:
        recommended_movie_names.append(movies.iloc[i[0]].Series_Title)

    return recommended_movie_names 


st.header('Movie Recommender System')


movie_list = movies['Series_Title'].values
selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    movie_list
)

if st.button('Show Recommendation'):
    recommended_movie_name= recommend(selected_movie)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommended_movie_name[0])
        try :
            index = movies[movies['Series_Title'] == recommended_movie_name[0]].index
            url = movies['Poster_Link'][index].values[0]
            response = requests.get(url)
            response.raise_for_status()
            img = Image.open(BytesIO(response.content))
            st.image(img)
        except requests.exceptions.RequestException as e:
             print(f"Failed to retrieve image: {e}")
        except IOError as e:
             print(f"Failed to process image: {e}")
        
    with col2:
        st.text(recommended_movie_name[1]) 
        try :
            index = movies[movies['Series_Title'] == recommended_movie_name[1]].index
            url = movies['Poster_Link'][index].values[0]
            response = requests.get(url)
            response.raise_for_status()
            img = Image.open(BytesIO(response.content))
            st.image(img)
        except requests.exceptions.RequestException as e:
             print(f"Failed to retrieve image: {e}")
        except IOError as e:
             print(f"Failed to process image: {e}")
    with col3:
        st.text(recommended_movie_name[2])
        try :
            index = movies[movies['Series_Title'] == recommended_movie_name[2]].index
            url = movies['Poster_Link'][index].values[0]
            response = requests.get(url)
            response.raise_for_status()
            img = Image.open(BytesIO(response.content))
            st.image(img)
        except requests.exceptions.RequestException as e:
             print(f"Failed to retrieve image: {e}")
        except IOError as e:
             print(f"Failed to process image: {e}")
        
    with col4:
        st.text(recommended_movie_name[3])
        try :
            index = movies[movies['Series_Title'] == recommended_movie_name[3]].index
            url = movies['Poster_Link'][index].values[0]
            response = requests.get(url)
            response.raise_for_status()
            img = Image.open(BytesIO(response.content))
            st.image(img)
        except requests.exceptions.RequestException as e:
             print(f"Failed to retrieve image: {e}")
        except IOError as e:
             print(f"Failed to process image: {e}")
        
    with col5:
        st.text(recommended_movie_name[4])
        try :
            index = movies[movies['Series_Title'] == recommended_movie_name[4]].index
            url = movies['Poster_Link'][index].values[0]
            response = requests.get(url)
            response.raise_for_status()
            img = Image.open(BytesIO(response.content))
            st.image(img)
        except requests.exceptions.RequestException as e:
             print(f"Failed to retrieve image: {e}")
        except IOError as e:
             print(f"Failed to process image: {e}")


