import os
from json import loads, dumps
from config import PLAYER_CONFIG_DIR


class ConfigManager:
    def __init__(self) -> None:
        self.config = {
            'playerSkin': 'default',
            'bestScore': 0,
            'bestScoreDate': '',
            'lastScore': 0,
            'lastScoreDate': ''
        }

    def change_setting(self, setting_name: str, value) -> None:
        try:
            self.config[setting_name] = value
            with open(PLAYER_CONFIG_DIR, 'w') as file:
                file.write(dumps(self.config))
        except:
            pass

    def update_config(self) -> None:
        try:
            with open(PLAYER_CONFIG_DIR, 'w') as file:
                file.write(dumps(self.config))
        except:
            pass

    def get_config(self) -> None:
        if os.path.isfile(PLAYER_CONFIG_DIR):
            try:
                with open(PLAYER_CONFIG_DIR, 'r') as file:
                    config_json = loads(file.read())
                    self.config = config_json
            except:
                pass
        else:
            self.update_config()


player_config = ConfigManager()
player_config.get_config()
