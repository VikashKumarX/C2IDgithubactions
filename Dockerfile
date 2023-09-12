FROM python:3.9
WOKDIR /app
COPY . /app
RUN pip install flask
Expose 8080
Entrypoint['python']			
CMD['app.py']



	
