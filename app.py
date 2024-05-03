from flask import Flask, render_template, request
import pickle
import requests
import pandas as pd

app = Flask(__name__)

def fetch_poster(movie_id):
  """Fetches the movie poster URL from TMDB API."""
  url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id)
  response = requests.get(url)
  data = response.json()
  poster_path = data.get('poster_path')  

  if poster_path:
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path
  else:
    return None  # Return None for missing posters

def recommend(cinema, film, similarity):
  """Recommends movies based on a selected movie and similarity matrix."""
  index = film[film['title'] == cinema].index[0]
  distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
  recommended_movie_names = []
  recommended_movie_posters = []
  for i in distances[1:6]:
    movie_id = film.iloc[i[0]].movie_id
    recommended_movie_poster = fetch_poster(movie_id) 
    if recommended_movie_poster:  
      recommended_movie_names.append(film.iloc[i[0]].title)
      recommended_movie_posters.append(recommended_movie_poster)

  return recommended_movie_names, recommended_movie_posters

film_path = r'C:\Users\Acer\Desktop\innomatics\tmdb\film.pkl'
similarity_path = r'C:\Users\Acer\Desktop\innomatics\tmdb\similarity.pkl'

try:
  with open(film_path, 'rb') as f:
    film = pickle.load(f)
  with open(similarity_path, 'rb') as f:
    similarity = pickle.load(f)
except FileNotFoundError:
  print("Error: Movie data or similarity matrix not found!")
  exit(1)

@app.route('/')
def index():
  """Renders the movie selection page."""
  return render_template('index.html', movie_list=film['title'].values)

@app.route('/recommend', methods=['POST'])
def recommend_movies():
  """Recommends movies and renders the recommendation page."""
  selected_movie = request.form['selected_movie']
  recommended_movie_names, recommended_movie_posters = recommend(selected_movie, film, similarity)
  return render_template('recommend.html',
                         recommended_movie_names=recommended_movie_names,
                         recommended_movie_posters=recommended_movie_posters)

if __name__ == '__main__':
  app.run(debug=True)
