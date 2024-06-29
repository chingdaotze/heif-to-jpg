from pathlib import Path

from .convert_file import convert_file


def convert_directory(
    source_dir: Path,
    target_dir: Path | None = None,
) -> None:
    # Set target dir
    if target_dir is None:
        target_dir = source_dir

    # Get all *.heif files
    heif_files = source_dir.glob(
        pattern="*.[heif heic]*",
    )

    # Convert each *.jpeg file
    for heif_file in heif_files:

        jpeg_file = target_dir / f"{heif_file.stem}.jpg"

        convert_file(
            source_path=heif_file,
            target_path=jpeg_file,
        )
