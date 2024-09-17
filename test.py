import logging


print("Hello Word")
print("world hello")
logging.basicConfig(
    filename='app.log',      # Log file name
    level=logging.DEBUG,     # Log level
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

# Example usage
logger = logging.getLogger(__name__)

def main():
    logger.debug('This is a debug message')
    logger.info('This is an info message')
    logger.warning('This is a warning message')
    logger.error('This is an error message')
    logger.critical('This is a critical message')
    logger.info("this is test line")

if __name__ == '__main__':
    main()