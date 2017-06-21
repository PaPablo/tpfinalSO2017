FROM python:3.3-onbuild
 
WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY . .

WORKDIR /usr/src/app/tpfinalso

RUN ["gunicorn", "tpfinalso.wsgi"]

EXPOSE 80
