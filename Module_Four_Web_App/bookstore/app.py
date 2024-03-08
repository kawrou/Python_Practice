import os
from flask import Flask, request

# Create a new Flask app
app = Flask(__name__)

# == Your Routes Here ==
@app.route('/hello', methods=['GET'])
def hello():
    name = request.args['name'] # The value is 'David'

    # Send back a friendly greeting with the name
    return f"Hello {name}!"
# To make a request, run:
# curl "http://localhost:5001/hello?name=David"

@app.route('/goodbye', methods=['POST'])
def goodbye():
    name = request.form['name'] # The value is 'Alice'

    # Send back a fond farewell with the name
    return f"Goodbye {name}!"

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    message = request.form['message']

    return f'Thanks {name}, you sent this message: "{message}"'   

@app.route('/wave', methods=['GET'])
def wave():
    name = request.args['name']

    return f'I am waving at {name}'

@app.route('/count_vowels', methods=['POST'])
def count_vowels():
    text = request.form['text']
    vowels = 'aeiou'
    #new_text = [letter for letter in text if letter in vowels]
    #return f'There are {len(new_text)} vowels in "{text}"'
    vowel_count = sum([text.count(vowel) for vowel in vowels])
    return f'There are {vowel_count} vowels in "{text}"'

@app.route('/sort-names', methods=['POST'])
def sort_names():
    if 'names' not in request.form:
        return 'Please provide names', 400
    names = request.form['names']
    name_list = names.split(',')
    name_list.sort()
    return ",".join(name_list)
    
    # return_names = ""
    # for name in name_list:
    #     return_names += f"{name},"   
    # return return_names[0:-1]

@app.route('/add', methods=['GET'])
def add_name():
    if 'name' not in request.args:
        return "You did not input a name to add", 400
    new_name = request.args['name']
    names = 'Julia,Alice,Karim'
    names += f',{new_name}'
    return names

@app.route('/names', methods=['GET'])
def add_multiple_names_and_sort():
    new_names = request.args['add']
    names = 'Julia,Alice,Karim' + f",{new_names}"
    names_list = names.split(",")
    names_list.sort()
    return ", ".join(names_list)

# == Example Code Below ==

# GET /emoji
# Returns a emojiy face
# Try it:
#   ; curl http://127.0.0.1:5001/emoji
@app.route('/emoji', methods=['GET'])
def get_emoji():
    return ":)"

# This imports some more example routes for you to see how they work
# You can delete these lines if you don't need them.
from example_routes import apply_example_routes
apply_example_routes(app)

# == End Example Code ==

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))

