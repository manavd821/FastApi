import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path

def setup_logger():
    # === Folder 1 ===
    log_dir = Path("log")
    log_dir.mkdir(exist_ok=True)
    log_file = log_dir / "app.log"
    if not log_file.exists():
        log_file.touch()
    
    # === Folder 2 ===
    log_dir2 = Path("log2")
    log_dir2.mkdir(exist_ok=True)  # FIXED LINE
    log_file2 = log_dir2 / "app2.log"
    if not log_file2.exists():
        log_file2.touch()
    
    # === Handlers ===
    file_handler = logging.FileHandler(log_file)
    stream_handler = logging.StreamHandler()
    rotate_file_handler = RotatingFileHandler(
        log_file2,
        maxBytes=1024 * 1024 * 5,  # 5 MB
        backupCount=3
    )
    
    # === Formatter ===
    formatter = logging.Formatter(
        fmt="{asctime} - {name} - {levelname} {filename}:{funcName}:{lineno} - {message}",
        style="{"
    )
    
    for handler in (file_handler, stream_handler, rotate_file_handler):
        handler.setFormatter(formatter)
    
    # === Logger ===
    logger = logging.getLogger("mylogger")
    logger.setLevel(logging.DEBUG)
    logger.handlers.clear()
    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)
    logger.addHandler(rotate_file_handler)
    
    return logger

logger = setup_logger()
