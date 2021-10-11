# our base image
FROM amazonlinux:latest

# ENV variables
ENV STAGE=DEV
ENV TABLE_NAME=ABCDE
ENV REGION=us-east-1


# Install python and pip
RUN yum update -y && \
  yum install python37 -y && \
  curl -O https://bootstrap.pypa.io/get-pip.py && \
  python3 get-pip.py --user && \
  ~/.local/bin/pip install boto3

# copy files required for the app to run
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/db
COPY src ./

# run the application
#CMD ["ls"] 
#CMD ["python3", "test.py"]
#CMD ["python3", "cli.py", "--stage", ${STAGE}, "--table-name", "${TABLE_NAME}", "--region", "${REGION}" ]
CMD python3 cli.py --stage $STAGE --table-name $TABLE_NAME --region $REGION


