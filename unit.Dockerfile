FROM ubuntu:eoan
LABEL maintainer="brendel.vadim@gmail.com"
RUN groupadd unit && useradd -g unit unit && \
    apt update && apt install curl python3.7 python3-pip -y && \
    curl -sL https://nginx.org/keys/nginx_signing.key | apt-key add - && \
    echo "deb https://packages.nginx.org/unit/ubuntu/ eoan unit" >> /etc/apt/sources.list.d/unit.list && \
    echo "deb-src https://packages.nginx.org/unit/ubuntu/ eoan unit" >> /etc/apt/sources.list.d/unit.list && \
    apt update && \
    apt install unit -y && \
    apt install unit-dev unit-python3.7 -y && \ 
    pip3 install --upgrade flask flask-restful
STOPSIGNAL SIGTERM
COPY ./ /
WORKDIR /
EXPOSE 8080
RUN chgrp -R unit /project
RUN chown -R unit /project
RUN chmod -R g+rwx /project
RUN chmod +x /project/app/bp_estimate/ppgl2/PPG_L2
RUN ln -sf /dev/stdout /var/log/unit.log
# RUN ln -sf /dev/stdout /project/app/log/sklearn_bp_docker.log
RUN chmod +x /unit_files/entrypoint.sh
# ENTRYPOINT ["tail", "-f", "/dev/null"]
ENTRYPOINT ["/unit_files/entrypoint.sh"]
CMD ["unitd", "--no-daemon", "--control", "unix:/var/run/control.unit.sock"]