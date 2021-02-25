# FROM nginx:1.19.6

# COPY mibs /usr/share/nginx/html
# COPY default.conf.template /etc/nginx/templates/

FROM registry.access.redhat.com/ubi8/ubi

RUN curl -fsSL https://goss.rocks/install | GOSS_VER=v0.3.13 sh

RUN cd /tmp ;\
    dnf install tzdata curl wget nc python3.8 python3-pip procps-ng -y ;\
    dnf update -y

COPY entrypoint.sh /work/entrypoint.sh
COPY dist/*.whl /tmp
COPY config.yaml /work/config.yaml
COPY lookups /work/lookups
COPY mibs /work/mibs
RUN pip3.8 install $(ls /tmp/*.whl); rm -f /tmp/*.whl

EXPOSE 5000
WORKDIR /work
ENTRYPOINT [ "/work/entrypoint.sh" ]