import logging

def get_logger(name="ha_meeting_summarizer"):
    """
    Returns a configured logger for the HA Meeting Summarizer project.

    Parameters:
        name (str): Name of the logger (default: "ha_meeting_summarizer")

    Returns:
        logging.Logger: Configured logger instance with INFO level and stream handler
    """
    logger = logging.getLogger(name)

    # Avoid adding multiple handlers if logger is requested multiple times
    if not logger.handlers:
        handler = logging.StreamHandler()
        formatter = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s")
        handler.setFormatter(formatter)
        logger.addHandler(handler)

    logger.setLevel(logging.INFO)
    return logger
