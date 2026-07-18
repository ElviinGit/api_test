import json
import os
from typing import Dict, Any

class Config:
    """Configuration manager for different environments"""
    
    def __init__(self, environment: str = "qa"):
        """
        Initialize config for specified environment
        
        Args:
            environment: Environment name (qa, stage, prod)
        """
        self.environment = environment.lower()
        self.config_path = os.path.join(os.path.dirname(__file__), f"{self.environment}.json")
        self._load_config()
    
    def _load_config(self):
        """Load configuration from JSON file"""
        if not os.path.exists(self.config_path):
            raise FileNotFoundError(f"Config file not found: {self.config_path}")
        
        with open(self.config_path, 'r') as f:
            self.data = json.load(f)
    
    def get(self, key: str, default: Any = None) -> Any:
        """Get config value by key"""
        return self.data.get(key, default)
    
    def get_base_url(self) -> str:
        """Get base URL for API"""
        return self.data.get("base_url", "https://jsonplaceholder.typicode.com")
    
    def get_timeout(self) -> int:
        """Get request timeout in seconds"""
        return self.data.get("timeout", 10)
    
    def get_all(self) -> Dict[str, Any]:
        """Get all configuration"""
        return self.data


# Singleton instance
_config_instance = None

def get_config(environment: str = None) -> Config:
    """Get or create config instance"""
    global _config_instance
    
    env = environment or os.getenv("TEST_ENV", "qa")
    
    if _config_instance is None or _config_instance.environment != env:
        _config_instance = Config(env)
    
    return _config_instance


