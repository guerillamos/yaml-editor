# YAML Editor Web Application

This web application allows users to load, edit, save, and validate YAML data against an OpenAPI specification.

## Overview

The YAML Editor web application is built using Python and Flask for the backend, and HTML, CSS, and JavaScript for the frontend.

The backend API reads and writes the YAML data to a file (`data.yaml`) and validates the content against an OpenAPI specification (`openapi.yaml`) before saving. The frontend provides a simple interface for users to edit the YAML data and save their changes.

## Features

- Load YAML data from the `data.yaml` file
- Edit YAML data in the browser using a textarea
- Save edited YAML data to the `data.yaml` file
- Validate the YAML data against the `openapi.yaml` OpenAPI specification before saving
- Display success or error messages upon saving the YAML data

## Installation and Usage

1. Make sure you have Python and pip installed on your system.
2. Install the required Python packages by running `pip install -r requirements.txt`.
3. Run the application using `python app.py`.
4. Open your web browser and navigate to `http://127.0.0.1:5000/` to access the YAML Editor web application.
