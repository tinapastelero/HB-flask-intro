from random import choice

from flask import Flask, request


# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza', 'oh-so-not-meh',
    'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful', 'smashing', 'lovely']


@app.route('/')
def start_here():
    """Home page."""

    return""" 
    <!DOCTYPE html>
    <html>
      <head>
      <title>Home Page</title>
      </head>

      <body>
        <p>Hi! This is the home page.</p>

        <p><a href="/hello">This is a link to the hello page.</a></p>
      <body>

    </html>"""

@app.route('/hello')
def say_hello():
    """Say hello and prompt for user's name."""

    return """
    <!doctype html>
    <html>
      <head>
        <title>Hi There!</title>
      </head>
      <body>
        <h1>Hi There!</h1>
        <form action="/diss">
          <label>What's your name? <input type="text" name="person"></label>
              <br>
          <label>Choose diss: </label>
          <select name="diss">
              <option value="slow">slow</option>
              <option value="smelly">smelly</option>
              <option value="boring">boring</option>
          </select>
              <br>
          <input type="submit">
        </form>

      </body>
    </html>
    """


@app.route('/greet')
def greet_person():
    """Get user by name."""

    player = request.args.get("person")
    compliment = request.args.get("compliment")

    compliment = choice(AWESOMENESS)

    return """
    <!doctype html>
    <html>
      <head>
        <title>A Compliment</title>
      </head>
      <body>
        Hi %s I think you're %s!

      </body>

    </html>
    """ % (player, choice(AWESOMENESS))


@app.route('/diss')
def diss_person():
    "Diss user."

    player = request.args.get("person")
    diss = request.args.get("diss")

    return """
    <!doctype html>
    <html>
        <head>
            <title>A Diss</title>
        </head>
        <body>
            Hi %s, I think you're %s!
        </body>
    </html>
    """ % (player, diss.upper())

if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads"
    # our web app if we change the code.
    app.run(debug=True)
