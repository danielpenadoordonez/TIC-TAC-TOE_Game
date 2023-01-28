FROM node:19-alpine3.16

COPY . /app

WORKDIR /app

RUN npm install && rm Dockerfile

EXPOSE 3000

CMD ["npm", "start"]