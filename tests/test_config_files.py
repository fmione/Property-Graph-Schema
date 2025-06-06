import os

def test_controller_config_file_not_exists():
    file_path = "dags/config_matlab.json"
    assert os.path.isfile(file_path), f"File not found: {file_path}"


def test_emulator_config_file_not_exists():
    file_path = "dags/scripts/lib/emulator2/EMULATOR_config.json"
    assert os.path.isfile(file_path), f"File not found: {file_path}"
   