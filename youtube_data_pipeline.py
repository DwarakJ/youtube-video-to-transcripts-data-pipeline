import os
import time
import datetime
import logging
from helper_functions import getVideoIDs, getVideoTranscripts, transformData, createTextEmbeddings

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def log_time_taken(step_name, start_time, end_time):
	duration = end_time - start_time
	logging.info(f"{step_name} completed in {duration:.2f} seconds")

def run_step(step_name, step_function):
	logging.info(f"Starting {step_name}")
	start_time = time.time()
	try:
		step_function()
		end_time = time.time()
		log_time_taken(step_name, start_time, end_time)
	except Exception as e:
		logging.error(f"Error during {step_name}: {e}")

def main():
	logging.info("Starting data pipeline at " + datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
	logging.info("----------------------------------------------")

	run_step("Step 1: Extract video IDs", getVideoIDs)
	run_step("Step 2: Extract transcripts for videos", getVideoTranscripts)
	run_step("Step 3: Transform data", transformData)
	run_step("Step 4: Generate text embeddings", createTextEmbeddings)

	# Delete the intermediate files created for processing
	logging.info("Cleaning up intermediate files")
	try:
		os.remove("data/video-ids.csv")
		os.remove("data/video-index.csv")
	except Exception as e:
		logging.error(f"Error cleaning up intermediate files: {e}")

if __name__ == "__main__":
	main()