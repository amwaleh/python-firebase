'''
    Install the firebase package using Git repo
    pip install git+git://github.com/ozgur/python-firebase.git
    This will reduce the number of error you will encounter
'''

from firebase import firebase
import requests


class FirebaseCls(object):
    '''Simple class of how to connect to firebase post and list data'''

    def __init__(self, url):
        self.url = url
        # Connect to the firebase serve
        self.firebase = firebase.FirebaseApplication(self.url, None)

    def get_object(self, path='/'):
        # Get a list of all data in a given route
        result = self.firebase.get(path, None)
        return result

    def post_object(self, path, data):
        # Post data to a given  route
        new_user = [{'name': 'craig'}, {'name': 'police'}]
        result = self.firebase.post('/pole',{'data': new_user, 'connection': 'get this done with'},
                                    {'print': 'pretty'}, {'X_FANCY_HEADER': 'VERY FANCY'})
        return result


fb = FirebaseCls('https://boiling-fire-5734.firebaseio.com')
b = fb.post_object('pole', {'car': 'suv', 'number': 3})
print b == None
