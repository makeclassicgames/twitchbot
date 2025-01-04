FROM python:3.7-slim
RUN pip install pipenv && mkdir /twitchbot
WORKDIR /twitchbot
COPY . /twitchbot
RUN pipenv install
CMD ["pipenv", "run", "startbot"]
