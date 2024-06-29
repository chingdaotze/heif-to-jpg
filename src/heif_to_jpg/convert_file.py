from pathlib import Path
from PIL import Image


def convert_file(
    source_path: Path,
    target_path: Path | None = None,
) -> None:

    heif_file = Image.open(
        fp=source_path,
    )

    jpeg_file = heif_file.convert(
        mode="RGB",
    )

    jpeg_file.save(
        fp=target_path,
    )
