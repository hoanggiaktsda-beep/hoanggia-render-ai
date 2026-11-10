"""HOANGGIA 3D Engine - staging input validation only."""
import gradio as gr

MAX_PIXELS = 12_000_000

def inspect(image):
    if image is None:
        raise gr.Error("Vui lòng tải ảnh sản phẩm")
    if image.width * image.height > MAX_PIXELS:
        raise gr.Error("Ảnh quá lớn (tối đa 12 MP ở bản staging)")
    return f"Đã nhận ảnh {image.width}×{image.height}. Chưa tích hợp model Image-to-3D. Không tạo mesh giả."

with gr.Blocks(title="HOANGGIA 3D Engine — staging") as demo:
    gr.Markdown("# HOANGGIA 3D ENGINE — STAGING\nChưa kích hoạt tạo mesh. Không công bố 3D chưa kiểm thử.")
    image = gr.Image(type="pil", label="Ảnh sản phẩm")
    btn = gr.Button("Kiểm tra ảnh đầu vào")
    status = gr.Textbox(label="Trạng thái")
    btn.click(inspect, inputs=image, outputs=status, api_name="validate_input")

if __name__ == "__main__":
    demo.launch()
