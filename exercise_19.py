from PIL import Image, ImageDraw

RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)


def french_flag(file_name: str, width: int = 300, height: int = 200) -> None:
    """
    Get french flag using PIL
    :param file_name: File name to save in
    :param width: Flag dimension width
    :param height: Flag dimension height
    """
    flag = Image.new("RGB", (width, height))
    p, q = width // 3, 2 * width // 3
    draw = ImageDraw.Draw(flag)
    draw.rectangle((0, 0, p, height), RED)
    draw.rectangle((p, 0, q, height), WHITE)
    draw.rectangle((q, 0, width, height), BLUE)
    flag.save(file_name)
