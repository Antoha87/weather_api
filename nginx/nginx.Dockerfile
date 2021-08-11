FROM nginx:1.19.2-alpine
WORKDIR /app
COPY /nginx /app
COPY /nginx/default.conf /etc/nginx/conf.d/default.conf
