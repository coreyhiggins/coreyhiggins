"""Generate both public mastheads: profile banner and repo header.

Type is converted to vector paths so it renders identically everywhere.
"""
import re
from pathlib import Path
from typetopath import Face

ROOT = Path(r"D:\Wynfall-Workspace")
FONT_DIR = ROOT / "repos/wynfall-site/node_modules/@fontsource/playfair-display/files"
FEATHER = ROOT / "repos/wynfall-site/public/brand/wynfall-feather-ivory.svg"
OUT_DIR = Path(__file__).with_name("out")
OUT_DIR.mkdir(exist_ok=True)

CYAN = "#5FE8FF"          # Wynfall company chrome, exclusively (brand law)
INK_TOP, INK_BOT = "#080B0F", "#0D131A"
IVORY, PAPER = "#F7F5EF", "#FBFAF6"
NAME_C, ROLE_C = "#F2EFE7", "#9DAEBD"
MUTED, TAG_C = "#76858F", "#7E8D99"
INK_FOR_TEXT = "#0B0F14"
INK_MUTED = "#6B6257"

reg = Face(str(FONT_DIR / "playfair-display-latin-400-normal.woff"))
ital = Face(str(FONT_DIR / "playfair-display-latin-400-italic.woff"))

raw = FEATHER.read_text(encoding="utf-8")
MASK = re.search(r"<defs>(.*?)</defs>", raw, re.S).group(1)
BODY = re.search(r"(<g transform=.*?)(?=</svg>)", raw, re.S).group(1)
BODY_IVORY = BODY.replace('fill="#f7f5ef"', f'fill="{IVORY}"')
BODY_INK = BODY.replace('fill="#f7f5ef"', f'fill="{INK_FOR_TEXT}"')
VB = "87 34 338 444"


def profile_banner():
    W, H, PAD = 1500, 420, 96
    kick, ks, ktr = "WYNFALL STUDIOS", 20, 0.30
    kick_d, _ = reg.path(kick, PAD + 34, 95, ks, ktr * reg.upm)
    name_d, name_w = reg.path("Corey Higgins", PAD, 232, 104)
    role_d, role_w = ital.path("Founder and head of engineering", PAD, 296, 43)
    tag_d, tag_w = reg.path("Models, inference, and the tools around them.", PAD, 374, 23, 0.012 * reg.upm)


    fw, fh, fx, fy = 404, 531, 1186, -58

    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" aria-label="Corey Higgins, founder and head of engineering at Wynfall Studios">
  <defs>
    <linearGradient id="ground" x1="0" y1="0" x2="0.4" y2="1">
      <stop offset="0" stop-color="{INK_TOP}"/><stop offset="1" stop-color="{INK_BOT}"/>
    </linearGradient>
    <radialGradient id="lift" cx="0.2" cy="0.26" r="0.78">
      <stop offset="0" stop-color="#18222E" stop-opacity="0.9"/><stop offset="1" stop-color="#080B0F" stop-opacity="0"/>
    </radialGradient>
    <radialGradient id="cool" cx="0.86" cy="0.1" r="0.5">
      <stop offset="0" stop-color="{CYAN}" stop-opacity="0.055"/><stop offset="1" stop-color="{CYAN}" stop-opacity="0"/>
    </radialGradient>
    <linearGradient id="rule" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0" stop-color="{CYAN}" stop-opacity="0.95"/>
      <stop offset="0.62" stop-color="{CYAN}" stop-opacity="0.28"/>
      <stop offset="1" stop-color="{CYAN}" stop-opacity="0"/>
    </linearGradient>
    <filter id="grain" x="0" y="0" width="100%" height="100%">
      <feTurbulence type="fractalNoise" baseFrequency="0.9" numOctaves="2" stitchTiles="stitch"/>
      <feColorMatrix type="saturate" values="0"/>
    </filter>
    {MASK}
  </defs>

  <rect width="{W}" height="{H}" fill="url(#ground)"/>
  <rect width="{W}" height="{H}" fill="url(#lift)"/>
  <rect width="{W}" height="{H}" fill="url(#cool)"/>

  <svg x="{fx}" y="{fy}" width="{fw}" height="{fh}" viewBox="{VB}" opacity="0.17" preserveAspectRatio="xMidYMid meet">{BODY_IVORY}</svg>
  <svg x="{PAD}" y="74" width="17" height="22" viewBox="{VB}" preserveAspectRatio="xMidYMid meet">{BODY_IVORY}</svg>

  <path d="{kick_d}" fill="{MUTED}"/>
  <path d="{name_d}" fill="{NAME_C}"/>
  <path d="{role_d}" fill="{ROLE_C}"/>
  <rect x="{PAD}" y="326" width="112" height="2" fill="url(#rule)"/>
  <path d="{tag_d}" fill="{TAG_C}"/>
  <rect width="{W}" height="{H}" filter="url(#grain)" opacity="0.032"/>
</svg>
"""


def repo_header():
    """Ivory header for the release-notes repo. Editorial, not a second dark banner."""
    W, H, PAD = 1500, 300, 96
    TEXT_X = PAD + 168          # mark owns the left column, type starts here
    name_d, name_w = reg.path("Wynfall", TEXT_X, 172, 96)
    sub_d, sub_w = ital.path("Release notes, and the public record of what ships.", TEXT_X + 2, 226, 27)

    fw, fh, fx, fy = 150, 197, PAD - 4, 40

    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" aria-label="Wynfall: release notes, and the public record of what ships">
  <defs>
    <linearGradient id="paper" x1="0" y1="0" x2="0.6" y2="1">
      <stop offset="0" stop-color="{PAPER}"/><stop offset="1" stop-color="#F2EEE4"/>
    </linearGradient>
    <linearGradient id="rule2" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0" stop-color="{INK_FOR_TEXT}" stop-opacity="0.55"/>
      <stop offset="0.7" stop-color="{INK_FOR_TEXT}" stop-opacity="0.12"/>
      <stop offset="1" stop-color="{INK_FOR_TEXT}" stop-opacity="0"/>
    </linearGradient>
    <filter id="grain2" x="0" y="0" width="100%" height="100%">
      <feTurbulence type="fractalNoise" baseFrequency="0.9" numOctaves="2" stitchTiles="stitch"/>
      <feColorMatrix type="saturate" values="0"/>
    </filter>
    {MASK}
  </defs>

  <rect width="{W}" height="{H}" fill="url(#paper)"/>
  <svg x="{fx}" y="{fy}" width="{fw}" height="{fh}" viewBox="{VB}" preserveAspectRatio="xMidYMid meet">{BODY_INK}</svg>

  <path d="{name_d}" fill="{INK_FOR_TEXT}"/>
  <path d="{sub_d}" fill="{INK_MUTED}"/>
  <rect x="{TEXT_X + 2}" y="254" width="150" height="2" fill="url(#rule2)"/>
  <rect width="{W}" height="{H}" filter="url(#grain2)" opacity="0.028"/>
</svg>
"""


if __name__ == "__main__":
    p = OUT_DIR / "banner.svg"
    p.write_text(profile_banner(), encoding="utf-8")
    r = OUT_DIR / "header.svg"
    r.write_text(repo_header(), encoding="utf-8")
    print(f"{p} {p.stat().st_size} bytes")
    print(f"{r} {r.stat().st_size} bytes")
