import sys  # gives access to Python's exception/traceback internals via sys.exc_infoimport 
import logging  # for logging error messages (not used in this snippet but commonly used in exception handling)


def error_message_detail(error, error_detail: sys):
    # error_detail is expected to be the 'sys' module itself (passed in by the caller).
    # The type hint ': sys' is a bit unconventional — it's hinting "this should behave
    # like the sys module", but in practice it's always just the sys module passed directly.

    _, _, exc_tb = error_detail.exc_info()
    # sys.exc_info() returns a 3-tuple: (exception_type, exception_value, traceback_object).
    # We only care about the traceback object here, so the first two are discarded
    # using '_' as a throwaway variable name. exc_tb holds the traceback.

    file_name = exc_tb.tb_frame.f_code.co_filename
    # Walks into the traceback object to extract the source file name where the
    # exception was raised:
    #   tb_frame   -> the stack frame active when the exception occurred
    #   f_code     -> the code object being executed in that frame
    #   co_filename -> the filename associated with that code object

    error_message = "Error occurred in python script name [{0}] line number [{1}] error message [{2}]".format(
        file_name, exc_tb.tb_lineno, str(error))
    # Builds a human-readable error string combining:
    #   {0} -> the file where the error happened (file_name)
    #   {1} -> the exact line number (exc_tb.tb_lineno)
    #   {2} -> the actual error/exception message, cast to string (str(error))

    return error_message
    # Returns the formatted message so it can be logged, printed, or re-raised
    # with more context than the bare exception alone would provide.
    
class CustomException(Exception): # wraps the built-in Exception class to add more context to errors
    def __init__(self, error_message, error_detail): # wraps the base Exception constructor to include additional context
        super().__init__(error_message)  # init base Exception with the message
        self.error_message = error_message_detail(error_message, error_detail=error_detail)
        # store a detailed message (file, line, error) using the helper function
        
    def __str__(self):
        return self.error_message
        # when the exception is converted to a string (e.g., printed), return the detailed message
        
        
if __name__ == "__main__":
    try:
        a = 1 / 0  # This will raise a ZeroDivisionError
    except Exception as e:
        logging.info("Divide by Zero Error")
        raise CustomException(e,sys)
    