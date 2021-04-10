from app import create_app
from app.config import AppConfig


app_config = AppConfig()


if __name__ == '__main__':
    # nohup sudo python -u __main__.py &

    app = create_app()
    app.run(**app_config["flask"])

