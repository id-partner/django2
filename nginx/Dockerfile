FROM nginx

RUN rm /etc/nginx/conf.d/default.conf

COPY listing.conf /etc/nginx/conf.d

RUN mkdir /etc/nginx/ssl
COPY ./ssl/*/etc/nginx/ssl/