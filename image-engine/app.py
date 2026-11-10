"""HOANGGIA Image Engine - CPU-only staging baseline; no AI renderer."""
import gradio as gr
from PIL import Image, ImageEnhance

MAX_PIXELS = 12_000_000

def process(image, task, strength):
    if image is None:
        raise gr.Error("Vui lòng tải ảnh")
    if image.width * image.height > MAX_PIXELS:
        raise gr.Error("Ảnh quá lớn (tối đa 12 MP ở bản staging)")
    image = image.convert("RGB")
    if task == "Upscale (CPU baseline)":
        if max(image.size) > 4096:
            raise gr.Error("Ảnh quá lớn để upscale 2x trong bản staging")
        return image.resize((image.width * 2, image.height * 2), Image.Resampling.LANCZOS), "Nội suy CPU, không phải AI super-resolution"
    if task == "Enhance (CPU baseline)":
        output = ImageEnhance.Sharpness(image).enhance(1 + strength)
        output = ImageEnhance.Contrast(output).enhance(1 + strength / 2)
        return output, "Tăng nét và tương phản CPU, chưa phải AI render"
    raise gr.Error("Module này chưa có AI model, không xuất kết quả giả")

with gr.Blocks(title="HOANGGIA Image Engine — staging") as demo:
    gr.Markdown("# HOANGGIA IMAGE ENGINE — STAGING\nChỉ có baseline CPU; chưa bật AI render.")
    inp = gr.Image(type="pil", label="Ảnh nguồn")
    task = gr.Dropdown(["Upscale (CPU baseline)", "Enhance (CPU baseline)", "Render (chưa có model)", "Redesign (chưa có model)"], value="Upscale (CPU baseline)", label="Tác vụ")
    strength = gr.Slider(0, 1, value=0.3, label="Cường độ")
    btn = gr.Button("Xử lý")
    out = gr.Image(type="pil", label="Kết quả")
    status = gr.Textbox(label="Trạng thái")
    btn.click(process, [inp, task, strength], [out, status], api_name="cpu_baseline")

if __name__ == "__main__":
    demo.launch()
