# Step 1: Use an official light-weight Python runtime blueprint
FROM python:3.10-slim

# Step 2: Establish an isolated app working directory inside the container
WORKDIR /app

# Step 3: Upgrade system pip to prevent wheel compilation overheads
RUN pip install --no-cache-dir --upgrade pip

# Step 4: Copy over your local source scripts and assets
COPY . /app

# Step 5: Install project requirements 
RUN pip install --no-cache-dir -r requirements.txt

# Step 6: Expose Port 8080 for EC2 production deployment
EXPOSE 8080

# Step 7: Launch the application gateway controller on port 8080
CMD ["python3", "application.py"]
