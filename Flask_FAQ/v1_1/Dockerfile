FROM python:3.11

# set a directory for the app
WORKDIR /usr/src/app

# copy all the files to the container
COPY . .

# install dependencies
#RUN pip install --no-cache-dir -r requirements.txt

# Use Below command to solve "SSL CERTIFICATE VERIFY FAILED" because network block some website
# Refer link : https://www.listendata.com/2019/04/connection-error-ssl-certificate-failed.html
RUN pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org -r requirements.txt

# tell the port number the container should expose
EXPOSE 80

# run the command
CMD ["python", "./app.py"]
