#Base image
FROM python:3.11

#copy application codebase
COPY ./ /var/web/patient
RUN ls -lrth /var/web/patient

#Install application python packages
WORKDIR /var/web/patient
RUN pip3 install --upgrade pip
RUN pip3 install --no-cache-dir -r requirements.txt


EXPOSE 8080 5000