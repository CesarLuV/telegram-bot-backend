# telegram-bot-backend
Backend written in FastAPI to provide Telegram API services for personal projects

# Installing requirements
1. Create a new virtual environment
2. Activate it
3. Update your pip3 tool:
```BASH
python3 -m pip install --upgrade pip
```
4. Install `pip-tools`
```BASH
pip3 install pip-tools
```
5. Compile the `requirements.in` file to generate a `requirements.txt` file with the latest version of *FastAPI* and it's dependencies.
```BASH
pip-compile
```
6. Install the dependencies from `requirements.txt`
```BASH
pip3 install -r requirements.txt
```

# Running the project
In a terminal, with the virtual environment activated, execute:
```BASH
uvicorn main:app --reload
```

# Interactive API docs (provided by Swagger UI)
In a web browser, go to: [Swager Docs](http://127.0.0.1:8000/docs).

## Alternative API docs (provided by ReDoc)
Or also, you could go to [ReDoc site](http://127.0.0.1:8000/redoc).