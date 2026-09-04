"""Generate shareable Windows + macOS promo images from project-owned artwork."""

from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter, ImageFont


ROOT = Path(__file__).resolve().parents[1]
FONT_CANDIDATES = [
    Path(r"C:\Windows\Fonts\msyhbd.ttc"),
    Path(r"C:\Windows\Fonts\msyh.ttc"),
    Path("/System/Library/Fonts/PingFang.ttc"),
    Path("/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc"),
]


def font(size: int, bold: bool = False) -> ImageFont.FreeTypeFont:
    candidates = FONT_CANDIDATES if bold else FONT_CANDIDATES[1:] + FONT_CANDIDATES[:1]
    selected = next((item for item in candidates if item.exists()), None)
    if not selected:
        raise FileNotFoundError("No CJK font found for promo image generation")
    index = 0
    return ImageFont.truetype(str(selected), size=size, index=index)


def cover(image: Image.Image, size: tuple[int, int]) -> Image.Image:
    scale = max(size[0] / image.width, size[1] / image.height)
    resized = image.resize((round(image.width * scale), round(image.height * scale)), Image.Resampling.LANCZOS)
    left = (resized.width - size[0]) // 2
    top = (resized.height - size[1]) // 2
    return resized.crop((left, top, left + size[0], top + size[1]))


def render(width: int, height: int, output: str) -> None:
    scale = width / 1200
    image = Image.new("RGB", (width, height), "#120f18")
    draw = ImageDraw.Draw(image)

    top = (31, 22, 42)
    bottom = (13, 10, 18)
    for y in range(height):
        t = y / max(1, height - 1)
        color = tuple(round(a + (b - a) * t) for a, b in zip(top, bottom))
        draw.line((0, y, width, y), fill=color)

    glow = Image.new("RGBA", image.size, (0, 0, 0, 0))
    glow_draw = ImageDraw.Draw(glow)
    glow_draw.ellipse(
        (round(width * 0.48), round(-height * 0.4), round(width * 1.18), round(height * 0.85)),
        fill=(125, 77, 167, 105),
    )
    glow = glow.filter(ImageFilter.GaussianBlur(round(105 * scale)))
    image = Image.alpha_composite(image.convert("RGBA"), glow)
    draw = ImageDraw.Draw(image)

    margin = round(72 * scale)
    icon = Image.open(ROOT / "icon.png").convert("RGBA")
    icon_size = round(72 * scale)
    icon.thumbnail((icon_size, icon_size), Image.Resampling.LANCZOS)
    image.alpha_composite(icon, (margin, margin))
    draw.text((margin + round(88 * scale), margin + round(4 * scale)), "月云了", font=font(round(26 * scale), True), fill="#fffaf0")
    draw.text((margin + round(88 * scale), margin + round(42 * scale)), "桌面常驻中", font=font(round(14 * scale)), fill="#9f90aa")

    badge_box = (margin, round(190 * scale), round(430 * scale), round(242 * scale))
    draw.rounded_rectangle(badge_box, radius=round(13 * scale), fill="#30203f", outline="#6c4b86", width=max(1, round(1 * scale)))
    draw.text((margin + round(20 * scale), round(202 * scale)), "WINDOWS  +  macOS", font=font(round(19 * scale), True), fill="#e7d5f7")

    title_font = font(round(58 * scale), True)
    draw.multiline_text((margin, round(274 * scale)), "现在，他也\n住进 Mac 了。", font=title_font, fill="#fffaf0", spacing=round(10 * scale))
    draw.text((margin, round(438 * scale)), "会陪你，也会在该休息的时候来管你。", font=font(round(20 * scale)), fill="#cbbfd7")
    draw.text((margin, height - round(76 * scale)), "v0.1.0-beta.3  ·  朋友测试版", font=font(round(15 * scale)), fill="#8f809d")

    stage = (round(700 * scale), round(60 * scale), width - margin, height - round(48 * scale))
    shadow = Image.new("RGBA", image.size, (0, 0, 0, 0))
    shadow_draw = ImageDraw.Draw(shadow)
    shadow_draw.rounded_rectangle((stage[0], stage[1] + round(20 * scale), stage[2], stage[3] + round(20 * scale)), radius=round(32 * scale), fill=(0, 0, 0, 105))
    shadow = shadow.filter(ImageFilter.GaussianBlur(round(30 * scale)))
    image = Image.alpha_composite(image, shadow)
    draw = ImageDraw.Draw(image)
    draw.rounded_rectangle(stage, radius=round(32 * scale), fill="#3d2a50", outline="#6b4c82", width=max(1, round(1 * scale)))

    menu_height = round(44 * scale)
    draw.rounded_rectangle((stage[0], stage[1], stage[2], stage[1] + menu_height), radius=round(32 * scale), fill="#21172b")
    draw.rectangle((stage[0], stage[1] + menu_height // 2, stage[2], stage[1] + menu_height), fill="#21172b")
    draw.text((stage[0] + round(20 * scale), stage[1] + round(11 * scale)), "99   月云了桌宠", font=font(round(12 * scale), True), fill="#d9cce4")
    draw.text((stage[2] - round(70 * scale), stage[1] + round(11 * scale)), "09:09", font=font(round(12 * scale)), fill="#b7a8c3")

    speech = (stage[0] + round(28 * scale), stage[1] + round(78 * scale), stage[2] - round(28 * scale), stage[1] + round(132 * scale))
    draw.rounded_rectangle(speech, radius=round(14 * scale), fill="#2b2036")
    draw.text((speech[0] + round(18 * scale), speech[1] + round(13 * scale)), "换台电脑，也甩不掉我。", font=font(round(16 * scale), True), fill="#f4e9fd")

    pet = Image.open(ROOT / "pet-preview.png").convert("RGBA")
    pet_box_size = (round((stage[2] - stage[0]) * 1.02), round((stage[3] - stage[1]) * 0.78))
    pet = cover(pet, pet_box_size)
    image.alpha_composite(pet, (stage[2] - pet.width + round(18 * scale), stage[3] - pet.height + round(8 * scale)))

    draw = ImageDraw.Draw(image)
    draw.text((stage[0] + round(24 * scale), stage[3] - round(34 * scale)), "APPLE SILICON + INTEL", font=font(round(11 * scale), True), fill="#9f8bad")
    image.convert("RGB").save(ROOT / output, quality=94, optimize=True)


if __name__ == "__main__":
    render(1200, 630, "social-preview.png")
    render(1600, 900, "promo-windows-macos.png")
