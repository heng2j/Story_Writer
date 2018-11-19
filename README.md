![StoryY Writer Temp](Doc_Images/Story_writer_home_Screen_Temp.png?raw=true "StoryY Writer Temp Home Screen")

# Story Writer (Coming soon...)
-----------------
Story Writer is a web widget that create a space with the right tools for creative writers, urban poets and rhymed artists to compose their art pieces.  


# Table of Contents
1. [Creative Values](README.md#creative-values)
2. [Basic usage](README.md#basic-usage)
3. [Future Development](README.md#future-development)
4. [Author](README.md#author)
5. [References](README.md#references)


# Features that generate Creative Values

### "Give me a Synonym" 
  - Have you ever running out of words to use? In Story Writer, by highlighting two ore more words on the inline rich text editor, you will have a search option to get a random synonym for your inspiration. Currently the Synonyms are providing by [datamuse api](https://www.datamuse.com/api/) 
  
  - Details can be found in the [WikiPage]()
  
### "Give me a List of words that rhymed with this word" 
  - Running out of right word that rhyme? Instead of Googling around or even digging out your dictionary, in Story Writer, your rhyme is at your fingertips. Whenever you are typing a new word, a list of words that rhymed with the word that you are typing will show at bottom of the rich text editor. So you will never running out of rhyme. Currently, our database of Rhymed words are using the [CMU Pronouncing Dictionary](http://www.speech.cs.cmu.edu/cgi-bin/cmudict#about)
  
  - Details can be found in the [WikiPage]()
  
 ### "Whom said the same thing as well?" 
  - Have you ever wondering if your line is fresh enough? What if someone had already used it, can you figure it out without leaving your workspace? Here Story Writer can tell you right away. Currently, our database contained 24850 hip-hop songs by 1107 artists from 1982 to 2015. And the data are coming from the [380000 lyrics from Metrolyrics](https://www.kaggle.com/gyani95/380000-lyrics-from-metrolyrics) dataset from Kaggle. So when you highlighted and query certain words on the rich editor, you can get a list of songs that have lyrics contained the phase you are having in mind. Currently, we only support single word searching, and limited to 100 referenced songs for each query. The list of songs are randomly selected. More option will be provided in the future release. 
  - Details can be found in the [WikiPage]()
  - Here is an brief [Exploratory Data Analysis on MetroLyrics Data Set](https://github.com/heng2j/Story_Writer/blob/master/notebook/Exploratory%20Data%20Analysis%20on%20MetroLyrics%20Data%20Set.ipynb) 

  


# Basic usage

### Installation & Set up

#### Step 1. Install Dependencies 

    pip install -r requirements.txt

#### Step 2. Build the SQLite Database
    cd src
    python build_database.py 

#### Step 3. Start Flask Server
    # Assumed you are already in /src
    python server.py
    
### Check out the Swagger ReST Article  
  Once the flask server is up and running. By copy and paste the following url, you can access the Swagger ReST Article to see the full details of the API endpoints
  
    http://localhost:5000/api/ui/#/
 
 
 ![Swagger ReST Article](Doc_Images/Swagger%20ReST%20Article.png?raw=true "Swagger ReST Article ")
 
 
### All functions for the API endpoints were developed and tested in the Test Driven Development (TDD) manner
  All tests under the tests folder had been tested successfully in PyCharm
  
    /tests 
    
   ** I am still new to pytest to fully automate the test process, if the tests can be run in the command line, please try on Pycharm

### All API endpoints were also tested Postman

  ![PostMan Test Sample ](Doc_Images/song_search_Postman_test.png?raw=true "PostMan Test Sample for song seraching with song title and artist name")

 # Future Development
 
 This web widget is inspired by the iOS mobile app [Rhymer's Block](https://appsite.skygear.io/rhymer_s_block/)
 Currently, all the fundamental API endpoints are set up. And the next step will be front-end development to fully intergrade the features. And few Open Sourced Rich Editor will be used. For example [MediumEditor](https://github.com/yabwe/medium-editor)
 
 Here is the [Trello Broad](https://trello.com/b/yZ2EeRUG/storywriter) for this project. 
 
  ![Trello Board](Doc_Images/Trello_board.png?raw=true "Trello Board")
 
 
 
 # Author
 All code started with the following header are created by Zhongheng Li (Heng). And references of the code are included in the comment.
 
    #!/usr/bin/env python3
    # {script_name}
    # ---------------
    # Author: Zhongheng Li
    # Start Date: MM-DD_YY
    # Last Modified Date: MM-DD_YY
 
 ### The following files are also created by Zhongheng Li (Heng)
    - src/home.html
    - src/swagger.yml
    - notebook/Exploratory Data Analysis on MetroLyrics Data Set.ipynb

    
 # References
 
 The following are the references and resources I came across during this project. They gave me lights of how to solve some of the technically challenges.
 
 Reference for working with The CMU Pronouncing Dictionary:
- [Time to Rhyme: The CMU Pronouncing Dictionary and You](https://www.youtube.com/watch?v=W0pdPNh86H0)
- [Rhyme dictionary from CMU pronunciation database](https://stackoverflow.com/questions/15822832/rhyme-dictionary-from-cmu-pronunciation-database)

Reference For developing PythonRest_API: 
- [Flask Connexion Rest API](https://realpython.com/flask-connexion-rest-api/)
- [Flask Connexion Rest API Part 2](https://realpython.com/flask-connexion-rest-api-part-2/)
- [Meet Connexion: Our REST Framework for Python](https://jobs.zalando.com/tech/blog/meet-connexion-our-rest-framework-for-python/?gh_src=4n3gxh1)


Reference for Testing in Python:
- [Python Testing](https://realpython.com/python-testing/)
- [Testing a Flask Application Using Pytest](https://www.patricksoftwareblog.com/testing-a-flask-application-using-pytest/)

