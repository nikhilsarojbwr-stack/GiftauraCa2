import qrcode
from qrcode.image.svg import SvgPathImage
from pathlib import Path
from datetime import datetime


# ============================================================
# CONFIGURATION
# ============================================================

OUTPUT_DIR = Path("qr_output")

PNG_BOX_SIZE = 20
SVG_BOX_SIZE = 10
BORDER = 4

ERROR_CORRECTION = qrcode.constants.ERROR_CORRECT_H


# ============================================================
# CREATE OUTPUT DIRECTORY
# ============================================================

OUTPUT_DIR.mkdir(
    parents=True,
    exist_ok=True
)


# ============================================================
# GET URL FROM USER
# ============================================================

print()
print("=" * 70)
print("              GOLD STAR JEWELLERY")
print("              QR CODE GENERATOR")
print("=" * 70)
print()

URL = input("Paste the URL here:\n> ").strip()


# ============================================================
# VALIDATE URL
# ============================================================

if not URL:
    raise SystemExit("\n❌ Error: No URL entered.")

if not (
    URL.startswith("https://")
    or URL.startswith("http://")
):
    raise SystemExit(
        "\n❌ Error: URL must start with http:// or https://"
    )


# ============================================================
# TIMESTAMP
# ============================================================

timestamp = datetime.now().strftime(
    "%Y%m%d_%H%M%S"
)


base_name = f"qr_{timestamp}"


png_path = OUTPUT_DIR / f"{base_name}.png"
svg_path = OUTPUT_DIR / f"{base_name}.svg"
txt_path = OUTPUT_DIR / f"{base_name}_data.txt"


# ============================================================
# CREATE QR OBJECT
# ============================================================

qr = qrcode.QRCode(
    version=None,
    error_correction=ERROR_CORRECTION,
    box_size=PNG_BOX_SIZE,
    border=BORDER
)


qr.add_data(URL)

qr.make(
    fit=True
)


# ============================================================
# GENERATE HIGH-RESOLUTION PNG
# ============================================================

png_image = qr.make_image(
    fill_color="black",
    back_color="white"
)


png_image.save(
    png_path
)


# ============================================================
# GENERATE VECTOR SVG
# ============================================================

svg_qr = qrcode.make(
    URL,
    image_factory=SvgPathImage,
    box_size=SVG_BOX_SIZE,
    border=BORDER
)


svg_qr.save(
    svg_path
)


# ============================================================
# SAVE QR DATA
# ============================================================

with open(
    txt_path,
    "w",
    encoding="utf-8"
) as file:

    file.write(
        "GOLD STAR JEWELLERY - QR CODE\n"
    )

    file.write(
        "=" * 50 + "\n\n"
    )

    file.write(
        f"Generated: "
        f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n"
    )

    file.write(
        "URL encoded in QR:\n"
    )

    file.write(
        URL + "\n"
    )

    file.write(
        f"\nQR Version: {qr.version}\n"
    )

    file.write(
        f"Modules: "
        f"{qr.modules_count} x "
        f"{qr.modules_count}\n"
    )

    file.write(
        "Error Correction: HIGH\n"
    )


# ============================================================
# SUCCESS INFORMATION
# ============================================================

print()
print("=" * 70)
print("                 ✅ QR CREATED")
print("=" * 70)

print()

print("URL:")
print(URL)

print()

print("OUTPUT FILES:")
print()

print(f"PNG : {png_path}")
print(f"SVG : {svg_path}")
print(f"DATA: {txt_path}")

print()

print("QR INFORMATION:")
print()

print(f"QR Version : {qr.version}")
print(
    f"Modules    : "
    f"{qr.modules_count} x "
    f"{qr.modules_count}"
)
print("Error      : HIGH")

print()

print("=" * 70)
print("The QR code is STATIC.")
print("It directly contains the URL you entered.")
print("=" * 70)
print()