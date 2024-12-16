from typing import Dict, Text, Any 
import requests

from django.core.cache import cache





class APIHandler:
    """
    This class manipulates and abstracts the 
    entire code implementation of the requests library.
    """

    def __init__(self, base_URL: Text) -> None:
        self.__base_URL: Text = base_URL
        self.__path: Text = ""


    @property
    def URL(self) -> str:
        return self.__base_URL


    @property
    def path(self, path: Text="") -> str:
        return self.__path


    @property
    def full_URL_REST(self) -> str:
        return f"{self.URL}/{self.path}"


    @URL.setter
    def set_URL(self, new_URL: Text) -> None:
        self.__base_URL = new_URL


    @path.setter
    def set_path(self, new_path: Text) -> None:
        self.__path = new_path


    @full_URL_REST.setter
    def set_full_URL_REST(self, new_full_URL_REST: Any) -> Exception:
        """
        It is only possible to change this variable indirectly
        by modifying the set_path and set_URL directly.
        """
        raise Exception("ERROR: Element does not support this type of input.")


    def json_requests_response(self, query_params: Dict = {}) -> dict:
        """
        The json request response uses the data provided
        of set_path and set_URL and a dictionary of REST URL parameters, then you
        I need them to use this function. This function returns
        the response from the request library. Does not contain cache. 
        """
        try:
            response = requests.get(self.full_URL_REST, params=query_params)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            return {"requests.utils.error": f"{e}"}


    def json_requests_with_cache(self, query_params: Dict = {}) -> dict:
        """The json request response uses the data provided
        of set_path and set_URL and a dictionary of REST URL parameters, then you
        I need them to use this function. This function returns
        the response from the request library. contain cache. """
        cache_key = "response_with_cache" 
        cached_data = cache.get(cache_key)

        if cached_data:
            # Returns from cache if data is used
            return cached_data

        try:
            response = requests.get(self.full_URL_REST, params=query_params)
            response.raise_for_status()
            data = response.json()
            cache.set(cache_key, data, timeout=60)
            return data
        except requests.exceptions.RequestException as e:
            return {"requests.utils.cache.error": f"{e}"}


    def log_requests_response(self, query_params: Dict = {}) -> str:
        """
        Assembled for debugging is a function that requires URL 
        parameters and uses json_requests_response for responses. 
        Does not contain cache.
        """
        print(str(self.json_requests_response(query_params)))
