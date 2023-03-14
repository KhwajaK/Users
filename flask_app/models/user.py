from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

class Users:
    DB = "users_schema"
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
                
    @classmethod
    def get_all(cls):
        query = """
        SELECT * FROM users;
        """
        results = connectToMySQL(cls.DB).query_db(query)
        users = []
        for user in results:
            users.append(cls(user))
        return users
    
    @classmethod
    def get_one(cls, data):
        query = """
        SELECT * FROM users WHERE id = %(id)s;
        """
        results = connectToMySQL(cls.DB).query_db(query, data)
        return cls(results[0])

    @classmethod
    def update(cls, data):
        query = """
        UPDATE users SET first_name = %(first_name)s, last_name = %(last_name)s, email = %(email)s WHERE id = %(id)s;
        """
        return connectToMySQL(cls.DB).query_db(query,data)

    @classmethod
    def save(cls, data):
            
            query = """
            INSERT into users (first_name, last_name, email, created_at, updated_at)
            VALUES (%(first_name)s, %(last_name)s, %(email)s, NOW(), NOW()); 
            """ 
            results = connectToMySQL(cls.DB).query_db(query, data)
            return results
    
    @classmethod
    def delete(cls, id):
        query= """
        DELETE FROM users WHERE id = %(id)s;
        """
        data = {"id": id}
        results = connectToMySQL(cls.DB).query_db(query, data)

    @staticmethod
    def validate_user(user):
        is_valid = True
        if len(user['first_name']) < 2:
            flash('First name must be at least two characters')
            is_valid=False
        if len(user['last_name']) <2:
            flash('Last name must be at least two characters')
            is_valid=False            
        if not EMAIL_REGEX.match(user['email']):
            flash('Invalid email address')
        return is_valid