# Hugging Face ZeroGPU connection — deployment checklist

Status: **NOT CONNECTED**. This repository cannot provision Spaces without owner-authorized Hugging Face access.

## Spaces to create under your Hugging Face username

- `<HF_USERNAME>/hoanggia-image-engine`
- `<HF_USERNAME>/hoanggia-3d-engine`

Choose **Gradio** and **ZeroGPU** on each Space. Do not select paid hardware.

## Upload source files

For Image Space, upload the contents of `image-engine/` from branch `staging/zerogpu-engines-v0.1` into the root of the HF Space:
- `app.py`
- `README.md`
- `requirements.txt`

For 3D Space, similarly upload the contents of `3d-engine/`.

The current apps are **CPU-only staging baselines**. Image Space does not render using AI; 3D Space does not generate geometry. Do not represent them as GPU inference engines.

## Verify endpoints before frontend integration

After the Space is running:
1. Visit `https://huggingface.co/spaces/<HF_USERNAME>/hoanggia-image-engine` and the 3D equivalent.
2. Inspect each Space's **Use via API** page.
3. Verify the Gradio OpenAPI document at `https://<space-subdomain>.hf.space/gradio_api/openapi.json` (subdomain must be read from the actual Space, not guessed).
4. Test real uploads and output artifacts.
5. Check unauthenticated quota and rate limiting. Avoid embedding an HF write token or admin token in static HTML.
6. Add verified public Space IDs to the frontend only after the API contract is confirmed.

## ZeroGPU inference acceptance

- Use `@spaces.GPU` for actual GPU model inference.
- Select a model with suitable license and ZeroGPU compatibility.
- Image AI: verify genuine generated output and bounded GPU duration.
- 3D AI: verify real, nonempty GLB, normals, materials and viewer compatibility.
- Do not claim support for FBX/SKP/BLEND unless a tested conversion pipeline exists.
- No paid fallback.

Official docs:
- https://huggingface.co/docs/hub/spaces-zerogpu
- https://huggingface.co/docs/hub/spaces-api-endpoints
