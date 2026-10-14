"""Explicit packaged-app smoke check; never runs during normal startup."""
import json
from pathlib import Path
import traceback


def run_self_test(app_class, destination):
    result = {}
    root = None
    try:
        from PIL import Image
        from core.paths import border_paths
        from core.rendering import render_token, TokenSettings, Slice, read_image
        root = app_class()
        root.withdraw()
        root.update()
        result['interface'] = 'ok'
        borders = border_paths()
        result['border_count'] = len(borders)
        assert borders
        border = read_image(next(iter(borders.values())))
        image = render_token(Image.new('RGBA', (100, 200), 'red'), border, 256,
                             TokenSettings(advanced=True, slices=[Slice(20, 30) for _ in range(4)]))
        assert image.size == (256, 256) and image.mode == 'RGBA'
        result['composition'] = 'ok'
        import rembg
        import onnxruntime
        result['ai_imports'] = 'ok'
        result['success'] = True
    except Exception:
        result['success'] = False
        result['error'] = traceback.format_exc()
    finally:
        if root is not None:
            root.destroy()
    Path(destination).write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding='utf-8')
    return 0 if result['success'] else 1
