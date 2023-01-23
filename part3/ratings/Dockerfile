FROM node:12.18.1-slim

RUN git clone https://github.com/CDPS-ETSIT/practica_creativa2

WORKDIR /opt/microservices/

COPY /practica_creativa2/bookinfo/src/ratings/package.json .

COPY /practica_creativa2/bookinfo/src/ratings/ratings.js .

ENV SERVICE_VERSION v1  

RUN npm install package.json

EXPOSE 9080

CMD ["node", "ratings.js", "9080"]

