FROM python:3.6
MAINTAINER Seonwhee Jin <quarklep@naver.com>

RUN apt-get update
RUN rm -rf /var/lib/apt/lists/*

COPY . /scrap_text
RUN pip install -r /scrap_text/requirement.txt
WORKDIR /scrap_text
EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
