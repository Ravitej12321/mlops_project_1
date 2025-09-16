import os 
import pandas as pd
from src.logger import get_logger
from src.custom_exception import CustomException
import yaml

logger = get_logger(__name__)

def read_yaml(filepath):
    try:
        if not os.path.exists(filepath):
            raise FileNotFoundError(f'file is not found in given path {filepath}')
        with open(filepath,'r') as yaml_file:
            config = yaml.safe_load(yaml_file)
            logger.info('successfully read the YAML file')
            return config
    except Exception as e:
        logger.error('Error while reading YAML file')
        raise CustomException(f'Failed to read YAML file')

def load_data(path):
    try:
        logger.info("Loading data")
        return pd.read_csv(path)
    except Exception as e:
        logger.error(f"Error loading the data {e}")
    
        raise CustomException("Failed to load data" , e)