from tkinter.messagebox import showinfo

from heif_to_jpg.get_directory import get_directory
from heif_to_jpg.convert_directory import convert_directory


def main() -> None:

    # Get directories
    heif_dir = get_directory(
        file_dialog_title="*.heif Input Directory",
    )

    jpeg_dir = get_directory(
        file_dialog_title="*.jpeg Output Directory",
    )

    # Convert directory
    convert_directory(
        source_dir=heif_dir,
        target_dir=jpeg_dir,
    )

    showinfo(
        title="Success",
        message="Done!",
    )


if __name__ == "__main__":

    main()
