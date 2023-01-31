FROM python:3.7

ENV GROUP_NUMBER 35

COPY docker.py .

RUN python3 docker.py 

EXPOSE 9080

CMD ["python3", "./practica_creativa2/bookinfo/src/productpage/productpage.py", "9080"]
