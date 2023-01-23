FROM python:3.8

RUN git clone https://github.com/CDPS-ETSIT/practica_creativa2.git

COPY script2.py .

RUN python3 script2.py

ENV GROUP_NUMBER = 35

EXPOSE 9080

CMD ["python3", "./practica_creativa2/bookinfo/src/productpage/productpage_monolith.py", "9080"]
