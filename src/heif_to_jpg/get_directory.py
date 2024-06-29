from tkinter import (
    filedialog,
    messagebox,
)
from pathlib import Path


def get_directory(
    file_dialog_title: str,
) -> Path:

    directory = filedialog.askdirectory(
        title=file_dialog_title,
    )

    if not directory:
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
        return Path(
            directory,
        )
