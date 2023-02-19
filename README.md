![Ironhack logo](https://i.imgur.com/1QgrNNw.png)

## Introduction

On this lab, you will create your very first own API using Flask. You'll lern how to set up a server, stop it, and abstract your code by using endpoints.

### Iteration 1

Start a server. For you to be able to do that, go to `your-code/main.ipynb` and on a notebook cell, you'll have to:

1. Import the necessary modules in Flask: `from flask import Flask, request, jsonify`
2. Initialize the Flask app: `app = Flask(__name__)`
3. Make sure you start the app: `app.run(port=9000, debug=True)`
4. Your notebook cell should look like this:

```python
from flask import Flask, request, jsonify
app = Flask(__name__)

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

Also, you'll get: ` * Running on http://127.0.0.1:8096 (Press CTRL+C to quit)`. Click the link to open that adress on the browser.

### Iteration 2

Change the debug to True/False

### Iteration 3

Create an endpoint that returns "Hello world!"

### Iteration 4

Create an endpoint that returns a random number

### Iteration 5

Run this on VSCode

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

## Deliverables

## Submission

Upon completion, add your deliverables to git. Then commit git and push your branch to the remote.

## Resources

[]()
