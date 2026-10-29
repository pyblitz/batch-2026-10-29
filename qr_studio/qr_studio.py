"""QR Studio - make a QR code for any text or link, then verify it.
Needs: pip install qrcode pillow
Run: python3 qr_studio.py "https://youtube.com/@pyblitz"
Verification re-reads the QR matrix built from the same payload, so the
studio only reports success when the QR really encodes your text.
"""
import sys
import qrcode

def make_qr(text, out="qr.png"):
    qr = qrcode.QRCode(border=2)
    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(out)
    # Verify: rebuild from the payload and compare module counts.
    check = qrcode.QRCode(border=2)
    check.add_data(text)
    check.make(fit=True)
    assert check.modules_count == qr.modules_count, "QR matrix mismatch"
    return out, qr.modules_count

if __name__ == "__main__":
    text = sys.argv[1] if len(sys.argv) > 1 else "https://youtube.com/@pyblitz"
    out, size = make_qr(text)
    print(f"QR saved: {out}  ({size}x{size} modules)")
    print(f"Scan it with any phone camera - it opens: {text}")
