FROM python:3.9-buster as development

RUN pip3 install pipenv

WORKDIR /src
COPY Pipfile Pipfile.lock ./
RUN pipenv install \
    --system \
    --deploy \
    --ignore-pipfile \
    --dev

COPY . .

ENV FLASK_ENV=development
CMD ["flask", "run", "--host=0.0.0.0"]
