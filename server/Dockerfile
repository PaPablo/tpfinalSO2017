FROM python:3.4-onbuild
 
WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY . .

COPY start.sh /start.sh

WORKDIR /usr/src/app/tpfinalso

CMD ["/start.sh"]


EXPOSE 80
