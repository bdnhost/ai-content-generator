
from src.api.rest_api import app
from src.utils.config import load_config
from src.utils.logger import setup_logger
from src.database.db_manager import DatabaseManager
from src.scheduling.scheduler import Scheduler

logger = setup_logger(__name__)

def main():
    config = load_config('config.yaml')
    
    # Initialize database
    db_manager = DatabaseManager(config['database']['url'])
    db_manager.create_tables()

    # Initialize scheduler
    scheduler = Scheduler()
    scheduler.start()

    # Start the Flask app
    app.run(host=config['api']['host'], port=config['api']['port'])

if __name__ == "__main__":
    main()
