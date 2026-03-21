# Configuration Settings

## Google Gemini
# The API key for accessing Google Gemini services.
GOOGLE_GEMINI_API_KEY = 'your_api_key_here'

## Flask Settings
# The secret key for Flask applications.
SECRET_KEY = 'your_secret_key_here'

# Debug mode: Set to True for development, False for production.
DEBUG = True

# Allowed hosts for the application.
ALLOWED_HOSTS = ['*']

## Injection Process Parameters
# Parameters to configure the injection process.
INJECTION_TIMEOUT = 30  # in seconds
MAX_INJECTION_RETRIES = 3

## Material Configurations
# Configuration for materials used in processing.
MATERIALS = {
    'default': {
        'type': 'json',
        'path': '/path/to/materials.json'
    },
    'other': {
        'type': 'xml',
        'path': '/path/to/materials.xml'
    }
}