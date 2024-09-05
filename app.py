import polars as pl
import os
from log import Log
from exception import CustomException

class Midas(BaseException):
    def __init__(self):
        self.current_path = os.getcwd()
        self.log_path = self.current_path + '/log'
        self.input_path = self.current_path + '/input'
        self.output_path = self.current_path + '/output'
    
    def __initialize_directories(self) -> None:
        
        try:
            if not os.path.exists(self.log_path):
                os.mkdir(self.log_path)
            if not os.path.exists(self.input_path):
                os.mkdir(self.input_path)
            if not os.path.exists(self.output_path):
                os.mkdir(self.output_path)
        except Exception as e:
            #CustomException.custom_exception(e)
            Log.write_log(Log, e, self.log_path, __name__)
            
    def convert_excel_to_csv(self) -> bool:
        pass
            
    
    def main(self) -> None:
        self.__initialize_directories()
    
if __name__ == '__main__':
    App = Midas()
    App.main()