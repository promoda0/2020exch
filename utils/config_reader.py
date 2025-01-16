# utils/config_reader.py
import yaml

def read_config():
    with open("resources/config.yaml", "r") as file:
        return yaml.safe_load(file)
