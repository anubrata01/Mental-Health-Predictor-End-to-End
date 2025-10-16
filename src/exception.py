import sys
def error_message_details(error, error_details :sys):
    _,_,exp_tb=error_details.exc_info() # exc_info gives type message and trackback object
    file_name = exp_tb.tb_frame.f_code.co_filename
    error_message = "Exception occurs in python script name [{0}] line number [{1}] error message [{2}]".format(
        file_name,exp_tb.tb_lineno,str(error)
    )
    return error_message

class CustomException(Exception):
    def __init__(self,error_message,error_details:sys):
        super().__init__(error_message)
        self.error_message = error_message_details(error_message,error_details=error_details)
    def __str__(self):
        return self.error_message