FROM node:19-alpine3.16 as build

COPY . /app

WORKDIR /app

RUN npm install 

RUN apk update && apk --no-cache add curl && sed -i s/localhost/tctctoe-api-svc/ package.json

# EXPOSE 3000

# CMD ["npm", "start"]

RUN npm run build

FROM nginx:alpine

COPY --from=build /app/build /usr/share/nginx/html

COPY nginx.conf /etc/nginx/nginx.conf

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"] 
