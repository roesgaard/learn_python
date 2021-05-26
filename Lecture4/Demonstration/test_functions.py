import requests


def return_request() -> requests.Response:
    """
    Get response from httpbin
    :return response:
    """
    response = requests.get('https://httpbin.org/ip')
    return response


def return_ip(response: requests.Response) -> str:
    """
    Extract IP string from request Response
    :param response:
    :return str:
    """
    ip = response.json()['origin']
    return ip
