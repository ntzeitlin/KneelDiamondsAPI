import json
from http.server import HTTPServer
from nss_handler import HandleRequests, status

from views import get_all_orders


class JSONServer(HandleRequests):
    """Server class to handle incoming HTTP requests for kneel diamonds"""

    def do_GET(self):
        """Handle GET requests from a client"""

        response_body = ""
        url = self.parse_url(self.path)

        if url["requested_resource"] == "orders":
            response_body = get_all_orders()
            return self.response(response_body, status.HTTP_200_SUCCESS.value)


def main():
    host = ""
    port = 8000
    HTTPServer((host, port), JSONServer).serve_forever()


if __name__ == "__main__":
    main()
