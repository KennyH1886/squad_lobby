FROM python:3.9

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

ENV PORT=8501
# Define environment variable
ENV STREAMLIT_SERVER_PORT=8501

LABEL service.name="squad-lobby-app"
EXPOSE 8501
# CMD ["streamlit", "run", "stack-heap.py", "--server.port", "$PORT", "--server.headless", "true"]



# # Define environment variable
# ENV STREAMLIT_SERVER_PORT=8501

# # Run study_buddy2.py when the container launches
CMD ["streamlit", "run", "main.py", "--server.port", "8501", "--server.headless", "true", "--server.enableCORS=False"]
