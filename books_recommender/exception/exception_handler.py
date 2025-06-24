
import sys

class AppException(Exception):
      """
 Organization : iNeuron Intelligence Private Limited
 AppException is a custom exception class that extends the built-in Exception class.
 It is used to handle exceptions in a more detailed manner by capturing the error message and the context
    of where the error occurred (file name and line number).
    """
def __init__(self, error_message: Exception, error_detail: sys):
        super().__init__(error_message)
        self.error_message = AppException.get_detailed_error_message(error_message=error_message, error_detail=error_detail)

@staticmethod
def get_detailed_error_message(error_message: Exception, error_detail: sys) -> str:
        """
        error: Exception: The exception that occurred.
        error_detail: sys: The sys module, which provides access to system-specific parameters and functions.
        Returns a detailed error message that includes the file name and line number where the error occurred.
        """
        _, _, exc_tb = error_detail.exc_info()
        # Extracting file name  from the traceback
        file_name = exc_tb.tb_frame.f_code.co_filename

        # Extracting line number from the traceback
        line_number = exc_tb.tb_lineno
        # Preparing the error message
        error_message = f"Error occurred in script: [{file_name}] at line number: [{line_number}] with error message: [{str(error_message)}]"
        return error_message
def __repr__(self):
        return AppException.__name__.str__()

def __str__(self):
        return  self.error_message    
