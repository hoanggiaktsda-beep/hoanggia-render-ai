# Triển khai Image Engine lên Hugging Face

Space: https://huggingface.co/spaces/hoanggiakt/hoanggia-image-engine

## Đã chuẩn bị
- Workflow chạy thủ công `Deploy Image Engine to Hugging Face`.
- Kiểm tra cú pháp Python và cấu hình Gradio trước khi upload.
- Chỉ upload ba file từ `image-engine/` lên thư mục gốc Space; không xóa file khác.
- Không đưa Hugging Face token vào GitHub source hoặc frontend.

## Bước chủ tài khoản cần thực hiện một lần
1. Mở https://huggingface.co/settings/tokens và tạo fine-grained token có quyền **write** cho đúng Space.
2. Mở https://github.com/hoanggiaktsda-beep/hoanggia-render-ai/settings/secrets/actions và chọn **New repository secret**.
3. Tên secret: `HF_TOKEN`. Dán token vào **GitHub Secrets** (không gửi token trong chat).
4. Mở https://github.com/hoanggiaktsda-beep/hoanggia-render-ai/actions/workflows/deploy-image-hf.yml, chọn **Run workflow** trên nhánh `main`.
5. Đợi workflow hoàn thành và mở Space để xem trạng thái build.

## Giới hạn
- Đây là app CPU baseline, chưa phải Render AI.
- SDK Gradio không tự kích hoạt ZeroGPU. Kiểm tra phần cứng trong Space Settings, không chọn GPU trả phí.
- Không kết nối frontend tới endpoint khi chưa xác minh API, quota và xử lý lỗi.
- Nếu không muốn tạo token, có thể upload thủ công `app.py`, `README.md`, `requirements.txt` vào Space.
