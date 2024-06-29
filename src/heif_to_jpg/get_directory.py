from tkinter import (
    filedialog,
    messagebox,
)
from pathlib import Path


def get_directory(
    file_dialog_title: str,
) -> Path:

    print(
        "Prompting for directory... Awaiting user input.",
    )

    directory = filedialog.askdirectory(
        title=file_dialog_title,
    )

    if not directory:

        print(
            "No directory selected. Secondary prompt activated... Awaiting user input.",
        )

        proceed = messagebox.askyesno(
            title="Proceed?",
            message="No directory selected. Do you want to continue?",
        )

        if proceed:
            return get_directory(
                file_dialog_title=file_dialog_title,
            )

        else:
            exit()

    else:

        directory = Path(
            directory,
        )

        print(
            f"Selected directory: '{directory}'",
        )

        return directory
