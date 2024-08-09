# This project is further developed by taking the following project as a reference.
https://github.com/ShawhinT/data-pipeline-example

Thanks to Shawhin Talebi for creating an awesome data pipeline example.

# YouTube Data Pipeline

This project demonstrates an automated data pipeline for processing YouTube video data. The pipeline extracts video IDs, transcripts, transforms the data, and generates text embeddings using various helper functions.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Functions](#functions)
- [License](#license)

## Overview

The YouTube Data Pipeline project automates the extraction and processing of YouTube video data. It includes steps for extracting video IDs, fetching transcripts, transforming the data, and generating text embeddings.

## Features

- Extract video IDs from a YouTube channel.
- Fetch transcripts for the extracted video IDs.
- Transform the data by handling special strings and setting appropriate data types.
- Generate text embeddings for video titles and transcripts.

## Installation

1. Clone the repository:
	```sh
	git clone https://github.com/yourusername/youtube-data-pipeline.git
	cd youtube-data-pipeline
	```

2. Create a virtual environment and activate it:
	```sh
	python3 -m venv venv
	source venv/bin/activate
	```

3. Install the required dependencies:
	```sh
	pip install -r requirements.txt
	```

## Usage

1. Configure your YouTube API key in the `helper_functions.py` file:
	```python
	my_key = "YOUR_YOUTUBE_API_KEY"
	```

2. Run the main script to start the data pipeline:
	```sh
	python youtube_data_pipeline.py
	```

## Functions

### youtube_data_pipeline.py

- `log_time_taken(step_name, start_time, end_time)`: Logs the time taken for each step.
- `run_step(step_name, step_function)`: Runs a pipeline step and logs its start and end time.
- `main()`: Main function to run the entire data pipeline.

### helper_functions.py

- `get_video_records(response)`: Extracts YouTube video data from a GET request response.
- `getVideoIDs()`: Returns all video IDs for a specified YouTube channel.
- `extractTranscriptText(transcript)`: Extracts text from a transcript dictionary.
- `getVideoTranscripts()`: Extracts transcripts for all video IDs stored in a CSV file.
- `handleSpecialStrings(df)`: Replaces special character strings in video transcripts and titles.
- `setDatatypes(df)`: Changes data types of columns in a Polars data frame.
- `transformData()`: Preprocesses video data.
- `createTextEmbeddings()`: Generates text embeddings of video titles and transcripts.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
