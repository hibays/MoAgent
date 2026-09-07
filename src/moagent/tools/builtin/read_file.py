__all__ = ["read_file"]

from pathlib import Path


def read_file_raw(
    file: Path, line_ranges: int | slice | None, encoding="utf-8"
)->str:
	"""Get file context, full or in-range.

    Args:
        file: The file you want to read
        line_ranges: line ranges, int means a line, slice means line ranges, None means full file.
		encoding="utf-8": 编码，默认是utf8

    Returns:
        The file str
    """
	raw_data = file.read_text(encoding=encoding)
	if isinstance(line_ranges, slice):
		data = raw_data.splitlines(keepends=True).__getitem__(line_ranges)
		data.join("\n")
	else:
		data = raw_data
	return data


def read_file(file: str, line_ranges: str, encoding="utf-8")->str:
	"""Get file context, full or in-range.

    Args:
        file: The file path you want to read
        line_ranges: line ranges, int means a line, slice (`23-78`) means line ranges, empty means full file.
		encoding="utf-8": 编码，默认是utf8

    Returns:
        The file str
    """
	s = None
	
	if "-" in line_ranges:
		l1, l2 = line_ranges.split("-")
		s = slice(l1, l2)
	elif line_ranges.__len__() != 0:
		s = slice(int(line_ranges))
	return read_file_raw(Path(file), s, encoding=encoding)
