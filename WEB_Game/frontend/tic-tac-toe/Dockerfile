FROM node:19-alpine3.16

COPY . /app

WORKDIR /app

RUN npm install 

RUN apk update && apk --no-cache add curl && sed -i s/localhost/tctctoe-api-svc/ package.json

EXPOSE 3000

CMD ["npm", "start"] 
