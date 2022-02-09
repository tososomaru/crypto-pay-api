import httpx


class Client:
    @staticmethod
    def fetch(url, headers, params):
        response = httpx.get(url, headers=headers, params=params)
        response_json = response.json()
        if response_json["ok"]:
            return response_json["result"]

        raise Exception(f"Bad request: {response_json['error']}")


class ApiClient(Client):
    def __init__(self, base_url, token):
        self.base_url = base_url
        self._headers = {"Crypto-Pay-API-Token": token}

    @staticmethod
    def _processing_params(params):
        if params:
            return {k: v for (k, v) in params.items() if v}

    def get(self, method, **params):
        return self.fetch(
            url=self.base_url + method,
            headers=self._headers,
            params=self._processing_params(params),
        )
