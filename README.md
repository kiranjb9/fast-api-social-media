🚀 Social Media App Clone Backend Project

1) Post route
This route is reponsible for creating post, deleting post, updating post and Checkinh post

2) Users route
This route is about creating users and searching user by id

3) Auth route
This route is about login system

4) Vote route
This route is about likes or vote system and this route contain code for upvote or back vote

how to run locally
First clone this repo by using following command

git clone https://github.com/kiranjb9/fast-api-social-media.git

Move to fastapi folder 
cd fastapi

Install All Packages Needed
pip install fastapi[all]

Run Command
uvicorn main:app --reload

Check API's On
http://127.0.0.1:8000/docs 

Create a database in postgres then create a file name .env and write the following things in you file
DATABASE_HOSTNAME = localhost
DATABASE_PORT = 5432
DATABASE_PASSWORD = passward_that_you_set
DATABASE_NAME = name_of_database
DATABASE_USERNAME = User_name
SECRET_KEY = 09d25e094faa2556c818166b7a99f6f0f4c3b88e8d3e7 
ALGORITHM = HS256
ACCESS_TOKEN_EXPIRE_MINUTES = 60

Note: SECRET_KEY in this exmple is just a psudo key. You need to get a key for youself and you can get the SECRET_KEY from fastapi documantion
