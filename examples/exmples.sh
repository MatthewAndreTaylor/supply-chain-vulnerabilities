#!/bin/bash

pip download mattyt
unzip mattyt-69.69.69-py3-none-any.whl -d wheel_work

# Manipulate files in wheel_work as needed

python - <<'EOF'
from pathlib import Path
p = next(Path("wheel_work").glob("*.dist-info/METADATA"))
p.write_text(p.read_text().replace("Version: 69.69.69", "Version: 69.69.69+patched"))
EOF

pip install wheel
python -m wheel pack wheel_work

# Inspect that the new wheel is valid and contains modifications
pip install mattyt-69.69.69-py3-none-any.whl  --target .