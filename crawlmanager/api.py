from fastapi import APIRouter, FastAPI
from starlette.responses import UJSONResponse

from .crawl import CrawlManager
from .schema import *

app = FastAPI()
crawl_man = CrawlManager()
crawl_router = APIRouter()


# ============================================================================
@app.post("/crawls", response_model=CreateNewCrawlResponse, content_type=UJSONResponse)
async def create_crawl(new_crawl: CreateCrawlRequest):
    return await crawl_man.create_new(new_crawl)


@app.get("/crawls", response_model=CrawlInfosResponse, content_type=UJSONResponse)
async def get_all_crawls():
    return await crawl_man.get_all_crawls()


@crawl_router.put(
    "/{crawl_id}/urls",
    response_model=OperationSuccessResponse,
    content_type=UJSONResponse,
)
async def queue_urls(crawl_id: str, url_list: QueueUrlsRequest):
    crawl = await crawl_man.load_crawl(crawl_id)
    return await crawl.queue_urls(url_list.urls)


@crawl_router.get(
    "/{crawl_id}", response_model=CrawlInfoResponse, content_type=UJSONResponse
)
async def get_crawl(crawl_id: str):
    crawl = await crawl_man.load_crawl(crawl_id)
    return await crawl.get_info()


@crawl_router.get(
    "/{crawl_id}/urls", response_model=CrawlInfoUrlsResponse, content_type=UJSONResponse
)
async def get_crawl_urls(crawl_id: str):
    crawl = await crawl_man.load_crawl(crawl_id)
    return await crawl.get_info_urls()


@crawl_router.post(
    "/{crawl_id}/start", response_model=StartCrawlResponse, content_type=UJSONResponse
)
async def start_crawl(crawl_id: str, start_request: StartCrawlRequest):
    crawl = await crawl_man.load_crawl(crawl_id)
    return await crawl.start(start_request)


@crawl_router.post(
    "/{crawl_id}/stop",
    response_model=OperationSuccessResponse,
    content_type=UJSONResponse,
)
async def stop_crawl(crawl_id: str):
    crawl = await crawl_man.load_crawl(crawl_id)
    return await crawl.stop()


@crawl_router.get(
    "/{crawl_id}/done", response_model=CrawlDoneResponse, content_type=UJSONResponse
)
async def is_done_crawl(crawl_id: str):
    crawl = await crawl_man.load_crawl(crawl_id)
    return await crawl.is_done()


@crawl_router.delete(
    "/{crawl_id}", response_model=OperationSuccessResponse, content_type=UJSONResponse
)
async def delete_crawl(crawl_id: str):
    crawl = await crawl_man.load_crawl(crawl_id)
    return await crawl.delete()


app.include_router(crawl_router, prefix="/crawl", tags=["crawl"])
app.add_event_handler("startup", crawl_man.startup)
app.add_event_handler("shutdown", crawl_man.shutdown)
