import sys
from src.loggger import loggging

import os

def get_error_message(error_message,error_detail:sys):
   _,_,exc_tb=error_detail.exc_info()
   file_name=exc_tb.tb_frame.f_code.co_filename
   error_message=f"the error python script name [{0}] and error line number is [{1}] and error message [{2}]".format(file_name,exc_tb.tb_lineno,str(error))

   return error_message

class CustomException(Exception):
   def __init__(self,error_message,error_details:sys):
      super().__init__(error_message)
      self.error_message=get_error_message(error_message=error_message,error_detail=error_details)

   def __str__(self) -> str:
      return self.error_message
   
   

