#! /usr/bin/python3.7
import os, yaml, time
from classes.gitlab import gitlab_api

if __name__ == "__main__":

    username    = 'test'
    email       = 'test@example.com'
    password    = 't4too7'
    first_name  = 'test'
    last_name   = 'test'

# class for working with users 
    gitlab = gitlab_api()
    gitlab.auth()
    gitlab.user_create( password    = password, 
                        username    = username, 
                        first_name  = first_name, 
                        last_name   = last_name,
                        email       = email
                        )

    gitlab.user_delete(username)
    gitlab.user_deactivate(username)
