import time
import os

from prometheus_client import Counter, Gauge, Histogram
from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint
from prometheus_client import CONTENT_TYPE_LATEST, REGISTRY, CollectorRegistry, generate_latest
from prometheus_client.multiprocess import MultiProcessCollector
from starlette.requests import Request
from starlette.responses import Response
from starlette.types import ASGIApp

REQUESTS = Counter("http_requests_total", "HTTP Request total", ["route", "status", "method"])
REQUESTS_TIME = Histogram("http_request_duration_seconds", "HTTP Request duration", ['route', 'method'])



class PrometheusMiddleware(BaseHTTPMiddleware):
    def __init__(self, app: ASGIApp) -> None:
        super().__init__(app)

    async def dispatch(self, request: Request, call_next: RequestResponseEndpoint) -> Response:

        method, route = request.method, request['path']
        if route == "/metrics":
            return await call_next(request)

        before_time = time.perf_counter()
        response = await call_next(request)
        after_time = time.perf_counter()

        REQUESTS.labels(method=method, status=response.status_code, route=route).inc()
        REQUESTS_TIME.labels(method=method, route=route).observe(after_time - before_time)

        return response

def metrics(request: Request) -> Response:
    if "prometheus_multiproc_dir" in os.environ:
        registry = CollectorRegistry()
        MultiProcessCollector(registry)
    else:
        registry = REGISTRY

    return Response(generate_latest(registry), media_type=CONTENT_TYPE_LATEST)
        