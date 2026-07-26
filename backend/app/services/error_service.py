def format_error(error):


    return {

        "status":"failed",

        "error_type":
        type(error).__name__,

        "message":
        str(error)

    }