from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    result = {
        "store_name": "송도 센트럴점",
        "market_type": "주거+상업 혼합",
        "area_size": "32평",
        "score": 68,
        "level": "보통",
        "scores": [
            {"name": "중앙매대", "score": 52, "level": "미흡", "color": "#ef4444"},
            {"name": "음료 쇼케이스", "score": 61, "level": "보통", "color": "#f59e0b"},
            {"name": "냉장평대", "score": 84, "level": "우수", "color": "#10b981"},
            {"name": "벽면매대", "score": 58, "level": "미흡", "color": "#ef4444"},
            {"name": "케이크 쇼케이스", "score": 72, "level": "보통", "color": "#f59e0b"},
            {"name": "외관/홍보물", "score": 79, "level": "보통", "color": "#f59e0b"},
        ],
        "top3": [
            {"rank": 1, "name": "중앙매대", "score": 52},
            {"rank": 2, "name": "음료 쇼케이스", "score": 61},
            {"rank": 3, "name": "벽면매대", "score": 58},
        ],
        "detail": {
            "name": "중앙매대",
            "score": 52,
            "level": "미흡",
            "score_items": [
                {"name": "전략상품 노출", "max": 30, "score": 10},
                {"name": "세트 구성", "max": 20, "score": 5},
                {"name": "POP 시인성", "max": 15, "score": 7},
                {"name": "카테고리 정리", "max": 20, "score": 15},
                {"name": "고객 동선/접근성", "max": 15, "score": 15},
            ],
            "minus": [
                {"title": "전략상품 전면 배치 부족", "desc": "베스트 상품이 후면에 있어 시선이 분산됩니다.", "score": "-15점"},
                {"title": "세트 구성 부족", "desc": "세트상품 연계 구매 유도가 약합니다.", "score": "-10점"},
                {"title": "POP 시인성 부족", "desc": "가격/프로모션 POP가 부족합니다.", "score": "-8점"},
            ],
            "reference": [
                "베스트 상품 전면 배치",
                "세트 상품 집중 구성",
                "POP 시인성 강화",
                "상품군 구획 정리",
            ],
        },
        "actions_now": [
            "전략상품 매대 전면 재배치",
            "세트 상품 POP 추가",
            "가격/프로모션 POP 부착",
        ],
        "actions_week": [
            "세트 상품 구성 확대",
            "매대 카테고리 정리",
            "매대 청결 및 동선 개선",
        ],
    }

    return templates.TemplateResponse(
        request,
        "index.html",
        {"result": result}
    )