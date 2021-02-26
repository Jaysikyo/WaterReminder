"""
Defines the Config class that loads and holds all configuration variables.

:author: Jacob Singleton
"""

from pathlib import Path
from yaml import (
    load as load_yaml,
    BaseLoader as YamlBaseLoader
)


class Config:
    """
    Object that loads and holds all configuration variables.
    """

    @staticmethod
    def get_yaml_data(config_path: Path) -> dict:
        """
        :param config_path: The Path object to the configuration file.
        :return: The data inside of the configuration file represented by a dictionary.
        """

        with open(config_path) as file:
            return load_yaml(file, Loader=YamlBaseLoader)

    @staticmethod
    def log_invalid_value(variable: str, value: object) -> None:
        """
        Logs to the console that there was an error loading a configuration value and that
        it has been set to its default value.

        :param config_path: The Path object for the configuration file.
        :param variable: The variable name in the configuration file that is incorrect.
        :param value: The default value of the variable that is being used instead.
        """

        print(
            '',
            f'ERROR: Missing or incorrect value for {variable}.',
            f'       {variable}={value} is being used by default.',
            '',
            sep='\n'
        )

    def __init__(self, config_path: Path):
        """
        Loads the configuration file and its values.

        :param config_path: The Path object to the configuration file.
        """

        try:
            yaml_data: dict = Config.get_yaml_data(config_path)

            self.load_variable(yaml_data, 'audio-path', 'audio_path', str, 'reminder-audio/')

            self.load_variable(yaml_data, 'minimum-interval', 'min_interval', int, 60)
            self.load_variable(yaml_data, 'maximum-interval', 'max_interval', int, 90)

            print('\'config.yml\' has been loaded!')
        except:
            self.load_defaults()

            print(
                f'Unable to load configuration values from {config_path.name}.',
                'Default values are being used instead:'
                '\n'.join([f'  {attr}={value}' for attr, value in self.__dict__]),
                sep='\n'
            )

    def load_variable(self, yaml_data: dict, config_var: str, var_name: str, required_type: object,
                      default: object) -> None:
        """
        Attempts to load a value from the configuration file.
        If the value is missing or an incorrect type, its default
        value is set and an error message is logged.

        :param yaml_data: The dictionary representation of the configuration file.
        :param config_var: The name of the variable in the configuration file.
        :param var_name: The name the variable should be saved as inside of this class.
        :param required_type: The required type of the variable in the configuration file.
        :param default: The default value of the variable if it is missing or incorrect.
        """

        if config_var in yaml_data:
            try:
                self.__dict__[var_name] = required_type(yaml_data[config_var])
                return
            except ValueError:  # Raised if unable to convert to required type.
                pass

        self.__dict__[var_name] = default

        Config.log_invalid_value(config_var, default)

    def load_defaults(self) -> None:
        """
        Sets the configuration values to their defaults.
        """

        self.audio_path = 'reminder-audio/'

        self.min_interval = 60
        self.max_interval = 90
