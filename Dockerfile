FROM python:3.13.3

EXPOSE 8080

WORKDIR /usr/src/app

COPY . .

RUN python3 -m venv .venv

RUN .venv/bin/pip3 install -r requirements.txt

CMD [".venv/bin/streamlit", "run", "app.py", "--server.port", "8080"]
