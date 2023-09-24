# import the function that will return an instance of a connection
from flask_app.config.mysqlconnection import connectToMySQL
# model the class after the friend table from our database
class Friend:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.occupation = data['occupation']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    # Now we use class methods to query our database
    @classmethod
    def get_all_friends(cls):
        query = "SELECT * FROM friends;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL('first_flask').query_db(query)
        # Create an empty list to append our instances of friends
        friends = []
        # Iterate over the db results and create instances of friends with cls.
        for friend in results:
            friends.append(cls(friend))
        return friends
        # added for the creation of the form
    @classmethod
    def save(cls, data):
        query = "INSERT INTO friends (first_name, last_name, occupation, created_at, updated_at) VALUES (%(first_name)s, %(last_name)s, %(occupation)s, NOW(), NOW());"
        return connectToMySQL('first_flask').query_db(query, data)
    
    # get a particular friend with the specified id
    @classmethod
    def get_one(cls, data):
        query= "SELECT * fROM friends WHERE id =%(id)s;"
        result=connectToMySQL('first_flask').query_db(query, data)
        return cls(result[0])
    
    @classmethod
    def update(cls, data):
        query= "UPDATE friends SET  first_name=%(first_name)s, last_name=%(last_name)s, occupation=%(occupation)s, updated_at = NOW() WHERE id=%(id)s;"
        return connectToMySQL('first_flask').query_db(query, data)
    
    @classmethod
    def remove(cls, data):
        query = "DELETE FROM friends WHERE id = %(id)s;"
        return connectToMySQL('first_flask').query_db(query, data)