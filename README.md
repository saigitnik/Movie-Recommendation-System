Movie Recommender System

This project is a movie recommender system built using Flask, Streamlit, and cosine similarity. It recommends similar movies based on user input and displays them using a web interface.

Overview
The recommender system uses a dataset of movies with their titles and features extracted from them, such as genres, keywords, and cast. These features are used to calculate the similarity between movies using cosine similarity.

Instructions:

To run the Flask version of the recommender system:
Clone this repository to your local machine.
Navigate to the project directory.
Install the required dependencies using pip install -r requirements.txt.
Run the Flask app using python app.py.
Open your web browser and go to http://localhost:5000 to access the recommender system.

To run the Streamlit version of the recommender system:
Install Streamlit using pip install streamlit.
Navigate to the project directory.
Run the Streamlit app using streamlit run streamlit_app.py.
Open your web browser and go to http://localhost:8501 to access the recommender system.

Note: Due to file size limitations on GitHub, the similarity.pkl file containing the cosine similarity matrix is larger than 25MB and cannot be uploaded to this repository. Please contact the project owner for access to this file.

Technologies Used:
Python
Flask
Streamlit
Cosine Similarity
