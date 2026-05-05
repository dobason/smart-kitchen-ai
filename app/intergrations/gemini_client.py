from google import genai
from typing import Optional
from app.core.config import settings

client = genai.Client(api_key=settings.GEMINI_API_KEY)

async def generate_recipe_from_ingredients(ingredients: list[str], preferences: dict, lang: Optional[str] = "vi") -> str:
    system_instruction = (
        "Bạn là đầu bếp Việt Nam chuyên nghiệp. Bạn là một bếp trưởng sáng tạo. "
        "Dựa vào danh sách nguyên liệu và các bước nấu, BẮT BUỘC phải đặt một CÁI TÊN CỤ THỂ, "
        "HẤP DẪN VÀ CHÍNH XÁC cho món ăn (Ví dụ: Bò xào dưa leo cá cơm, Cơm rang thập cẩm, Salad healthy...). "
        "TUYỆT ĐỐI KHÔNG được sử dụng các tên chung chung như 'Công thức AI', 'Món ăn mới', 'Recipe'. "
        "Tên món ăn phải được trả về trong trường name của JSON. "
        "Bạn bắt buộc phải điền đầy đủ thông tin vào các trường name, ingredients, steps, time. Tuyệt đối không được để null. "
        "Luôn luôn trả kết quả 100% bằng Tiếng Việt, "
        "kể cả tên nguyên liệu, đơn vị đo lường và các bước hướng dẫn. "
        "Không bao giờ dùng Tiếng Anh trong phản hồi."
    )

    prompt = f"""
{system_instruction}

Nguyên liệu người dùng cung cấp:
{ingredients}

Tùy chọn của người dùng:
{preferences}

Nhiệm vụ:
- Gợi ý MỘT món ăn phù hợp nhất với các nguyên liệu trên.
- Liệt kê đầy đủ nguyên liệu cần dùng kèm định lượng cụ thể.
- Hướng dẫn các bước nấu rõ ràng, dễ thực hiện.
- Toàn bộ phản hồi phải bằng Tiếng Việt.

Chỉ trả về một JSON hợp lệ với cấu trúc sau (không có markdown, không có giải thích thêm):
{{
    "name": "Tên món ăn bằng Tiếng Việt",
    "ingredients": [
        {{"name": "Tên nguyên liệu", "amount": "Định lượng (vd: 300g, 2 muỗng canh)"}},
        {{"name": "Tên nguyên liệu khác", "amount": "Định lượng"}}
    ],
    "steps": [
        "Bước 1: Mô tả bằng Tiếng Việt.",
        "Bước 2: Mô tả bằng Tiếng Việt.",
        "Bước 3: Mô tả bằng Tiếng Việt."
    ],
    "time": "Thời gian nấu (vd: 30 phút)"
}}
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt)

    return response.text