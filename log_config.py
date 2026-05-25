import logging 

file_handler = logging.FileHandler('logs/logs', encoding='utf-8')
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[logging.StreamHandler(), file_handler]
)

logger = logging.getLogger(__name__)