import os
import logging

class Log(object):
    def write_log(self, text: str, path: str, class_name: str) -> None:
        logging.basicConfig(filename=path + '/exception.log', level=logging.ERROR)
        logging.error(f'Exception occurred: {text} at class: {class_name}')
    
    def refresh_log(self, path: str) -> None:
        pass
            
            
    