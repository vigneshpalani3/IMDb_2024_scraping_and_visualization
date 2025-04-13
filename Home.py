import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from utils.shared import create_connection

engine=create_connection()

# page title
st.title("IMDB 2024 Data Scraping And Visualization")

selected_option = st.selectbox(
    "choose an option",
    ["Top 10 Movies By Rating And Voting Count",
     "Movie Distribution By Genre",
     "Average Duration By Genre",
     "Voting Trends by Genre",
     "Rating Distribution",
     "Top Movie per Genre",
     "Most Popular Genres by Voting",
     "Duration Extremes",
     "Genre Vs Rating",
     "Ratings Vs Voting Count"]
)

if selected_option=="Top 10 Movies By Rating And Voting Count":

    # first section
    st.subheader("Top 10 Movies By Rating And Voting Count")

    # get top 10 movies by rating and voting count
    top10_movies=pd.read_sql("SELECT * FROM MOVIES ORDER BY rating DESC,voting_count DESC LIMIT 10;",engine)
    top10_movies.index=range(1,len(top10_movies)+1)

    # display top 10 movies as a dataframe
    st.dataframe(top10_movies)

elif selected_option=="Movie Distribution By Genre":
    # second secition
    st.subheader("Movie Distribution By Genre")
    movie_count_by_genre=pd.read_sql("SELECT COUNT(*) AS Movies_Count,Genre FROM movies GROUP BY Genre;",engine)

    # display movie distribution by genre as bar chart
    fig,ax=plt.subplots()
    plt.style.use("default")
    sns.barplot(data=movie_count_by_genre,x="Genre",y="Movies_Count",palette="bright",ax=ax)

    st.pyplot(fig)

elif selected_option=="Average Duration By Genre":
    # third section
    st.subheader("Average Duration By Genre")

    average_duration_by_genre=pd.read_sql("SELECT ROUND(AVG(duration),2) AS Average_Duration ,Genre FROM movies GROUP BY Genre;",engine)

    fig,ax=plt.subplots()
    sns.barplot(data=average_duration_by_genre,y="Genre",x="Average_Duration",palette="bright",ax=ax)
    st.pyplot(fig)

elif selected_option=="Voting Trends by Genre":

    # fourth section
    st.subheader("Voting Trends by Genre")
    votings_by_genre=pd.read_sql("SELECT ROUND(AVG(voting_count),2) AS Average_Voting_Count,Genre FROM movies GROUP BY Genre;",engine)
    st.bar_chart(votings_by_genre.set_index("Genre"))

elif selected_option=="Rating Distribution":

    #fifth section
    st.subheader("Rating Distribution")
    rating_distribution=pd.read_sql("SELECT Movie_Name,Rating FROM movies",engine)
    fig,ax=plt.subplots()
    sns.histplot(data=rating_distribution,x="Rating",ax=ax,kde=True,color="purple",bins=10)
    st.pyplot(fig)

elif selected_option=="Top Movie per Genre":

    #sixth section
    st.subheader("Top Movie per Genre")
    top_movies_by_genre=pd.read_sql("SELECT m.* FROM movies m JOIN ( SELECT genre, MAX(rating) AS max_rating FROM movies GROUP BY genre ) AS max_ratings ON m.genre = max_ratings.genre AND m.rating = max_ratings.max_rating;",engine)
    st.dataframe(top_movies_by_genre)

elif selected_option=="Most Popular Genres by Voting":

    # seventh section
    st.subheader("Most Popular Genres by Voting")
    popular_genres=pd.read_sql("SELECT SUM(voting_count) AS Total_Votings,Genre FROM movies GROUP BY genre;",engine)
    fig,ax=plt.subplots()
    ax.pie(popular_genres["Total_Votings"],labels=popular_genres["Genre"],autopct="%1.1f%%")
    st.pyplot(fig)

elif selected_option=="Duration Extremes":

    # Eighth section
    st.subheader("Duration Extremes")
    max_duration=pd.read_sql("SELECT * FROM movies ORDER BY Duration desc LIMIT 1;",engine)
    min_duration=pd.read_sql("SELECT * FROM movies ORDER BY Duration asc LIMIT 1;",engine)
    st.write("Movie with Maximum Duration:")
    st.dataframe(max_duration)

    st.write("Movie with Minimum Duration:")
    st.dataframe(min_duration)

elif selected_option=="Genre Vs Rating":

    # ninth section
    st.subheader("Genre Vs Rating")
    genre_rating=pd.read_sql("SELECT Rating,Genre FROM movies;",engine)

    genre_rating["rating_bins"]=pd.cut(genre_rating["Rating"],bins=[0,6,7,8,9,10],labels=["<6","6-7","7-8","8-9","9-10"])

    heatmap_data=genre_rating.pivot_table(
        index="Genre",
        columns="rating_bins",
        values="Rating",
        aggfunc="count"
    ).fillna(0)

    fig,ax=plt.subplots()

    sns.heatmap(heatmap_data,cmap="coolwarm",fmt=".0f",annot=True,ax=ax)
    st.pyplot(fig)

elif selected_option=="Ratings Vs Voting Count":

    # Tenth section
    st.subheader("Ratings Vs Voting Count")
    rating_voting_count=pd.read_sql("SELECT Rating,Voting_Count FROM movies;",engine)
    st.scatter_chart(rating_voting_count,x="Rating",y="Voting_Count",use_container_width=True)