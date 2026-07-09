import requests
from utils.logger import logger
from config.config import get_config

class BaseApi:
    """Base class for all API endpoints"""
    
    def __init__(self, environment: str = None):
        """
        Initialize API client
        
        Args:
            environment: Environment to use (qa, stage, prod)
        """
        self.config = get_config(environment)
        self.base_url = self.config.get_base_url()
        self.timeout = self.config.get_timeout()

    def get(self, endpoint):
        """GET request"""
        url = f"{self.base_url}{endpoint}"
        logger.info(f"GET {url}")
        return requests.get(url, timeout=self.timeout)

    def post(self, endpoint, payload):
        """POST request"""
        url = f"{self.base_url}{endpoint}"
        logger.info(f"POST {url} with payload: {payload}")
        return requests.post(url, json=payload, timeout=self.timeout)

    def put(self, endpoint, payload):
        """PUT request"""
        url = f"{self.base_url}{endpoint}"
        logger.info(f"PUT {url} with payload: {payload}")
        return requests.put(url, json=payload, timeout=self.timeout)

    def patch(self, endpoint, payload):
        """PATCH request"""
        url = f"{self.base_url}{endpoint}"
        logger.info(f"PATCH {url} with payload: {payload}")
        return requests.patch(url, json=payload, timeout=self.timeout)

    def delete(self, endpoint):
        """DELETE request"""
        url = f"{self.base_url}{endpoint}"
        logger.info(f"DELETE {url}")
        return requests.delete(url, timeout=self.timeout)