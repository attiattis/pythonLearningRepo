from flask import Flask
from flask import *
import pickle
import base64
class Student:
    def __init__(self):
        self.name = "vyshak"
        self.ROLE = "USESR"
    def status(self):
        return(f"Hello {self.name} . You are having {self.ROLE} privilages.")
app = Flask(__name__)

@app.route("/login")
def hello():
    serializedString = request.cookies.get('serialized')
    serializedString = base64.b64decode(serializedString)
    print("Deserializing : ",serializedString)
    studentObject = pickle.loads(serializedString) # deserializing
    return studentObject.status()
@app.route("/")
def serializing():
    serializedString = pickle.dumps(Student() ) # serializing 
    # with open('test_pickle.pkl', 'wb') as pickle_out:
    #     pickle.dumps(Student() ,pickle_out) 
    serializedString = base64.b64encode(serializedString)
    print("Serialized string is : ",serializedString)
    # pickle.dumps(serializedString, Student() )
        
    response = make_response( render_template("login.html") )
    response.set_cookie( "serialized", serializedString )
    return response
    # return studentObject.status()

@app.route('/register', methods=['GET'])
def secondFunction():
    return "Second function"

if __name__ == "__main__":
    app.run()
    
#b'\x80\x04\x95?\x00\x00\x00\x00\x00\x00\x00\x8c\x08__main__\x94\x8c\x07Student\x94\x93\x94)\x81\x94}\x94(\x8c\x04name\x94\x8c\x06vyshak\x94\x8c\x04ROLE\x94\x8c\x05USESR\x94ub.'