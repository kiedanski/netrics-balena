FROM amazon/aws-cli
ARG BUCKET_NAME
ARG AWS_CERT
ARG AWS_SECRET

RUN amazon-linux-extras install epel -y && yum update -y && yum -y install inotify-tools

RUN mkdir -p /root/.aws
# RUN export AWS_CERT=$(cat /run/secrets/aws_cert); export AWS_SECR=$(cat /run/secrets/aws_secret); printf "[default]\naws_access_key_id=$AWS_CERT\naws_secret_access_key=$AWS_SECR\n" > /root/.aws/credentials
RUN printf "[default]\naws_access_key_id=$AWS_CERT\naws_secret_access_key=$AWS_SECRET\n" > /root/.aws/credentials
RUN printf "[default]\nregion=us-west-2\n" > /root/.aws/config

COPY upload /root/upload
RUN sed -i "s/bucket-name-replace/$BUCKET_NAME/" /root/upload

ENTRYPOINT ["/bin/sh", "/root/upload"]
#ENTRYPOINT ["/usr/bin/tail", "-f", "/dev/null"]

