![Ironhack logo](https://i.imgur.com/1QgrNNw.png)

## Introduction

On this lab, you will create your very first own API using Flask. You'll lern how to set up a server, stop it, and abstract your code by using endpoints.

### Iteration 1

Start a server. For you to be able to do that, go to `your-code/main.ipynb` and on a notebook cell, you'll have to:

1. Import the necessary modules in Flask:

```python
from flask import Flask, request, jsonify
```

2. Initialize the Flask app:

```python
app = Flask(__name__)
```

3. Make sure you start the app:

```python
app.run(port=9000, debug=True)
```

4. Your notebook cell should look like this:

```python
from flask import Flask, request, jsonify
app = Flask(__name__)

if __name__ == "__main__":
     app.run(port=9000, debug=True)
```

5. When running, you will get a message on notebooks

```markdown
- Serving Flask app '**main**' (lazy loading)
- Environment: production
  WARNING: This is a development server. Do not use it in a production deployment.
  Use a production WSGI server instead.
- Debug mode: on
```

Also, you'll get: ` * Running on http://127.0.0.1:9000 (Press CTRL+C to quit)`. Click the link to open that adress on the browser.

### Iteration 2

Create an endpoint that returns "Hello world!". For that, you'll need two things:
1 - The endopint

```python
@app.route("/")
```

2 - The function used by that endpoint

```python
def hello_world():
    return "Hello world!"
```

Include these two pieces of code between the code generated on iterations 2 and 3.

Make sure your code is still running and go to your browser and refresh. You should see "Hello world!".

### Iteration 3

Create an endpoint that returns a random number from 0 to 10.

- Endpoint: "/random-number"
- Function: def random_int
- Result: a stringified int

### Iteration 4

Run this on VSCode

- Stop your jupyter notebook
- Create a directory within your lab so that it has this structure:

```bash
your-code/
    main.ipynb
.gitignore
README.md

small-api/
    main.py
    config/
        sql_connection.py # for now empty
    tools/
        sql_queries.py #for now empty
```

- Copy your code from your jupyter notebook into your `main.py`
- From your terminal, run `python main.py`
- In that terminal, you'll get feedback of your prints and the errors.
- After the server is up and running you'll be able to go into your browser and access the endpoints you defined.

## Submission

Upon completion, add your deliverables to git. Then commit git and push your branch to the remote.
