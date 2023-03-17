from flask import Flask, request, jsonify, render_template
import os
import yaml
from openapi_spec_validator import validate_spec

app = Flask(__name__)
data_folder = "data"
data_file = "data.yaml"
openapi_file = "openapi.yaml"

@app.route('/')
def root():
    return render_template('index.html')

@app.route('/api/yaml', methods=['GET'])
def get_yaml():
    with open(os.path.join(data_folder, data_file), 'r') as file:
        yaml_content = file.read()
    return yaml_content

@app.route('/api/yaml', methods=['POST'])
def save_yaml():
    yaml_data = request.data.decode('utf-8')
    try:
        parsed_yaml = yaml.safe_load(yaml_data)
        
        with open(os.path.join(data_folder, openapi_file), 'r') as file:
            openapi_yaml = yaml.safe_load(file)
        
        validate_spec(openapi_yaml)

        with open(os.path.join(data_folder, data_file), 'w') as file:
            file.write(yaml_data)

        return jsonify(status="success", message="YAML data saved successfully.")
    except Exception as e:
        return jsonify(status="error", message=str(e)), 400

if __name__ == "__main__":
    app.run(debug=True)
