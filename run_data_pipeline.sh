# Initialize the virtual environment
python3 -m venv venv

# Activate the virtual environment
source venv/bin/activate

# Install the required packages
python3 -m pip install -r requirements.txt

# Run the Kafka producer
python3 youtube_data_pipeline.py