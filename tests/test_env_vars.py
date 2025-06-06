import os
from dotenv import load_dotenv


load_dotenv()

def test_env_neo4j():
    assert os.getenv("NEO4J_HOST") is not None, "NEO4J_HOST is missing"
    assert os.getenv("NEO4J_PORT") is not None, "NEO4J_PORT is missing"
    assert os.getenv("NEO4J_USER") is not None, "NEO4J_USER is missing"
    assert os.getenv("NEO4J_PASSWORD") is not None, "NEO4J_PASSWORD is missing"


def test_env_mysql():
    assert os.getenv("MYSQL_HOST") is not None, "MYSQL_HOST is missing"
    assert os.getenv("MYSQL_PORT") is not None, "MYSQL_PORT is missing"
    assert os.getenv("MYSQL_USER") is not None, "MYSQL_USER is missing"
    assert os.getenv("MYSQL_PASSWORD") is not None, "MYSQL_PASSWORD is missing"
    assert os.getenv("MYSQL_ROOT_PASSWORD") is not None, "MYSQL_ROOT_PASSWORD is missing"
    assert os.getenv("MYSQL_DATABASE") is not None, "MYSQL_DATABASE is missing"

def test_env_matlab():
    assert os.getenv("MATLAB_MAC_ADDRESS") is not None, "MATLAB_MAC_ADDRESS is missing"
    assert os.getenv("MLM_LICENSE_FILE") is not None, "MLM_LICENSE_FILE is missing"
    assert os.getenv("MATLAB_LICENSE_PATH") is not None, "MATLAB_LICENSE_PATH is missing"
    assert os.getenv("MATLAB_REMOTE_PATH") is not None, "MATLAB_REMOTE_PATH is missing"
