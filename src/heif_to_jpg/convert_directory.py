from pathlib import Path

from .convert_file import convert_file


def convert_directory(
    source_dir: Path,
    target_dir: Path | None = None,
) -> None:
    # Set target dir
    if target_dir is None:
        target_dir = source_dir

    print(
        f"Source directory: '{source_dir}'\n"
        f"Target directory: '{target_dir}'\n"
        "Searching for *.heif and *.heic files in Source directory...",
    )

    # Get all *.heif files
    heif_files = [
        heif_file
        for heif_file in source_dir.glob(
            pattern="*.[heif heic]*",
        )
    ]

    # Convert each *.jpeg file
    heif_file_count = len(heif_files)

    print(
        f"Found {heif_file_count} HEIF files...",
    )

    for index, heif_file in enumerate(heif_files):

        print(
            f"Processing {index + 1} of {heif_file_count} ...",
        )

        jpeg_file = target_dir / f"{heif_file.stem}.jpg"

        convert_file(
            source_path=heif_file,
            target_path=jpeg_file,
        )
