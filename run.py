from app import create_app
from app.config.settings import settings
from mangum import Mangum
import uvicorn

app = create_app()
handler = Mangum(app) # This is for AWS Lambda

if __name__ == '__main__':
    try:
        uvicorn.run(
            app,
            host = settings.FAST_API_HOST,
            port = settings.FAST_API_PORT
        )
    except Exception as e:
        print(str(e))