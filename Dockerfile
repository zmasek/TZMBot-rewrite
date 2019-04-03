FROM python:3.6-stretch

RUN apt-get update
RUN apt-get install libffi-dev libnacl-dev python3-dev -y

COPY Pipfile /
COPY Pipfile.lock /
COPY profile /

RUN pip install pipenv
RUN pipenv install --system

ENV DISCORD_TOKEN=ADDTOKEN
ENV DISCORD_ERROR_CHANNEL=ADDERRORCHANNEL
ENV DISCORD_DEV_ID=ADDDEVID

COPY TZMBot/ /TZMBot
WORKDIR /TZMBot

CMD ["python", "run.py"]
