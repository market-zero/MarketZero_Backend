from typing import List

from pydantic import BaseModel


# 상품 정보
class Item(BaseModel):
    id: int  # 상품 고유 id
    title: str  # 상품의 이름
    image: str  # 상품 이미지 url
    description: str  # 상품 설명
    tags: List[
        str
    ]  # 상품 태그: ["brand-new", "recommend", "zero-sugar", "zero-kcal", "zero-gluten", "zero-caffeine", "zero-alcohol"]
    price: int  # 상품 가격

    class Config:
        json_schema_extra = {
            "example": {
                "title": "롯데칠성음료 펩시제로슈거 라임향 355ml",
                "image": "https://shopping-phinf.pstatic.net/main_3374125/33741256619.20220728160715.jpg?type=f640",
                "description": "사람들이 선호하는 대표적인 zero 음료입니다.",
                "tags": ["recommend", "zero-sugar"],
                "price": 310,
            }
        }
