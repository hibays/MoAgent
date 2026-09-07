__all__ = ["edit"]
from pathlib import Path
def edit(
		file: Path,
		old_content: str,
		new_content: str,
		encoding="utf-8"
)->str:
	"""Edit file content.

    Args:
        file: The file you want to edit
        content: The content you want to edit
		encoding="utf-8": 编码，默认是utf8

    Returns:
        The file str
    """

	raw_data = file.read_text(encoding=encoding)
	if old_content not in raw_data:
		raise ValueError(f"Old content not found in file: {file}")
	data = raw_data.replace(old_content, new_content)
	file.write_text(data, encoding=encoding)
	return data