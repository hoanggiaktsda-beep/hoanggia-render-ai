# HOANGGIA RENDER AI — Staging v0.1

**Status: prototype, NOT a deployed image-generation or 3D-generation service.**

## Boundaries
- Web: catalog of 12 modules; no fake processing.
- Image Engine: CPU baseline (resize and enhancement); **not AI rendering**.
- 3D Engine: input validation only; **not image-to-3D**.
- ZeroGPU Spaces are **not** provisioned by this repository.
- Never include Hugging Face tokens in this public repository or frontend code.
- Do not fall back to paid inference APIs.

## Create two Hugging Face Spaces
1. Under the project owner's Hugging Face account, create Gradio Spaces: `hoanggia-image-engine` and `hoanggia-3d-engine`.
2. Upload the contents of `image-engine/` and `3d-engine/` respectively to the **root** of each Space, including their `README.md` and `requirements.txt`.
3. Start with CPU smoke tests. A real GPU model and its `@spaces.GPU` execution must be separately validated under ZeroGPU quota.
4. For anonymous users, verify HF guest quotas, client API access, queue operation, CORS and abuse controls before publishing a direct website integration.
5. No claim of 3D export until a real nonempty GLB has been independently inspected in a viewer.

## Local smoke tests
```bash
python -m pip install -r image-engine/requirements.txt
python image-engine/app.py

python -m pip install -r 3d-engine/requirements.txt
python 3d-engine/app.py
```

## Acceptance gates
1. Python syntax and package builds pass.
2. Real image inference generates an artifact, with input/seed/runtime logged.
3. Real 3D inference produces valid mesh and downloadable GLB, with viewer inspection.
4. Image content, file size, guest quotas, retries, timeouts and isolation validated.
5. Desktop/mobile testing and ZeroGPU conditions confirmed.
6. Publish only after these checks and owner review.
