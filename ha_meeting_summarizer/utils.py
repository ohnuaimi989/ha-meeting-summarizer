import logging

def get_logger(name="ha_meeting_summarizer"):
    """
    Returns a configured logger for the project.
    
    Parameters:
        name (str): Name of the logger (default "ha_meeting_summarizer")
    
    Returns:
        logging.Logger: Configured logger instance
    """
    logger = logging.getLogger(name)
    
    if not logger.handlers:  # avoid adding multiple handlers
        handler = logging.StreamHandler()
        handler.setFormatter(logging.Formatter(
            '%(asctime)s - %(levelname)s - %(message)s'
        ))
        logger.addHandler(handler)
    
    logger.setLevel(logging.INFO)
    return logger
