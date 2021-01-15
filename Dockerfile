FROM nginx:1.19.6

COPY mibs /usr/share/nginx/html
COPY default.conf.template /etc/nginx/templates/