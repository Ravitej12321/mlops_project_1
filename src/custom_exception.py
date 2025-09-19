import traceback
import sys


class CustomException(Exception):

    def __init__(self,error_message,error_details:sys):
        super().__init__(error_message)
        self.error_message = self.get_detailed_error_message(error_message,error_details)
    
    @staticmethod
    def get_detailed_error_message(error_message,error_details:sys):
        try:
            _, _ ,exc_tb = error_details.exc_info()
            filename = exc_tb.tb_frame.f_code.co_filename
            line_no = exc_tb.tb_lineno
        except Exception as e:
            exc_type, exc_value, exc_traceback = sys.exc_info()

        return f'Error in {filename}, line {line_no} : {error_message}'
    
    def __str__(self):
        return self.error_message