"""Draw profile chrome in the existing cyan / magenta theme.

The hero animation and the typing line stay as they are. These SVGs are the
section frames around them, plus a signal strip from the public contribution
calendar. Nothing here copies another profile's artwork.
"""

from __future__ import annotations

import json
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "assets"
LINKS = ASSETS / "links"

BG = "#060810"
CYAN = "#00E5FF"
MAGENTA = "#FF2D95"
TEXT = "#F4F7FF"
MUTED = "#A6B2CC"
LINE = "#16304a"
YELLOW = "#E6C200"

FONT = "ui-monospace, SFMono-Regular, Menlo, Consolas, monospace"


def svg_open(width: int, height: int, label: str) -> list[str]:
    return [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" role="img" aria-label="{label}">',
        f"<title>{label}</title>",
        f'<rect width="{width}" height="{height}" fill="{BG}"/>',
    ]


def write(path: Path, parts: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(parts) + "\n", encoding="utf-8")


def section_bar(name: str, index: str, title: str, accent: str) -> None:
    width, height = 960, 56
    parts = svg_open(width, height, title)
    parts += [
        f'<text x="8" y="36" fill="{accent}" font-family="{FONT}" font-size="22" letter-spacing="3">{index}  //  {title}</text>',
        f'<line x1="280" y1="30" x2="952" y2="30" stroke="{LINE}" stroke-width="1"/>',
        "</svg>",
    ]
    write(ASSETS / name, parts)


def link_button(name: str, label: str, accent: str) -> None:
    width, height = 320, 72
    parts = svg_open(width, height, label)
    parts += [
        f'<rect x="2" y="2" width="316" height="68" fill="{BG}" stroke="{accent}" stroke-width="1.5"/>',
        f'<path d="M2 14 V2 H14" fill="none" stroke="{accent}" stroke-width="2"/>',
        f'<path d="M306 2 H318 V14" fill="none" stroke="{accent}" stroke-width="2"/>',
        f'<path d="M2 58 V70 H14" fill="none" stroke="{accent}" stroke-width="2"/>',
        f'<path d="M306 70 H318 V58" fill="none" stroke="{accent}" stroke-width="2"/>',
        f'<text x="160" y="42" text-anchor="middle" fill="{accent}" font-family="{FONT}" font-size="16" letter-spacing="3">{label}</text>',
        "</svg>",
    ]
    write(LINKS / name, parts)


def about_panel() -> None:
    width, height = 960, 280
    parts = svg_open(width, height, "About Sham Solanki")
    parts += [
        f'<rect x="1" y="1" width="958" height="278" fill="none" stroke="{LINE}"/>',
        f'<path d="M1 16 V1 H16" fill="none" stroke="{CYAN}" stroke-width="2"/>',
        f'<path d="M944 1 H959 V16" fill="none" stroke="{MAGENTA}" stroke-width="2"/>',
        f'<path d="M1 264 V279 H16" fill="none" stroke="{CYAN}" stroke-width="2"/>',
        f'<path d="M944 279 H959 V264" fill="none" stroke="{MAGENTA}" stroke-width="2"/>',
        f'<text x="28" y="48" fill="{MAGENTA}" font-family="{FONT}" font-size="16">root@profile:~$</text>',
        f'<text x="196" y="48" fill="{CYAN}" font-family="{FONT}" font-size="16">whoami</text>',
        f'<text x="28" y="78" fill="{TEXT}" font-family="{FONT}" font-size="18">sham solanki</text>',
        f'<text x="28" y="122" fill="{MAGENTA}" font-family="{FONT}" font-size="16">root@profile:~$</text>',
        f'<text x="196" y="122" fill="{CYAN}" font-family="{FONT}" font-size="16">focus</text>',
        f'<text x="28" y="152" fill="{TEXT}" font-family="{FONT}" font-size="16">document retrieval  ·  voice workflows  ·  computer vision</text>',
        f'<text x="28" y="196" fill="{MAGENTA}" font-family="{FONT}" font-size="16">root@profile:~$</text>',
        f'<text x="196" y="196" fill="{CYAN}" font-family="{FONT}" font-size="16">learning</text>',
        f'<text x="28" y="226" fill="{TEXT}" font-family="{FONT}" font-size="16">services, postgres, docker, and metrics</text>',
        f'<rect x="28" y="244" width="10" height="16" fill="{CYAN}">',
        '<animate attributeName="opacity" values="1;0;1" dur="1.05s" repeatCount="indefinite"/>',
        "</rect>",
        "</svg>",
    ]
    write(ASSETS / "about.svg", parts)


def footer_panel() -> None:
    width, height = 960, 88
    parts = svg_open(width, height, "Open to internships and collaborations")
    parts += [
        f'<line x1="8" y1="8" x2="952" y2="8" stroke="{LINE}"/>',
        f'<circle cx="22" cy="48" r="5" fill="{CYAN}"/>',
        f'<text x="40" y="54" fill="{CYAN}" font-family="{FONT}" font-size="15" letter-spacing="2">PROFILE ONLINE</text>',
        f'<text x="952" y="54" text-anchor="end" fill="{MAGENTA}" font-family="{FONT}" font-size="15" letter-spacing="2">OPEN TO INTERNSHIPS</text>',
        "</svg>",
    ]
    write(ASSETS / "footer.svg", parts)


def open_site() -> None:
    width, height = 960, 64
    parts = svg_open(width, height, "Open the hosted site")
    parts += [
        f'<rect x="1" y="1" width="958" height="62" fill="{BG}" stroke="{CYAN}"/>',
        f'<text x="28" y="40" fill="{MUTED}" font-family="{FONT}" font-size="15">SYS://SITE</text>',
        f'<text x="500" y="40" text-anchor="middle" fill="{TEXT}" font-family="{FONT}" font-size="16" letter-spacing="2">OPEN THE HOSTED PAGE</text>',
        f'<text x="932" y="40" text-anchor="end" fill="{MAGENTA}" font-family="{FONT}" font-size="15">LIVE</text>',
        "</svg>",
    ]
    write(ASSETS / "open-site.svg", parts)


def signal_strip() -> None:
    url = "https://github-contributions-api.jogruber.de/v4/SamaelSama69?y=last"
    with urllib.request.urlopen(url, timeout=30) as response:
        payload = json.loads(response.read().decode("utf-8"))
    days = payload["contributions"]
    total = int(payload["total"]["lastYear"])
    busiest = max(days, key=lambda day: day["count"])
    peak = max(day["count"] for day in days) or 1

    width, height = 960, 210
    left, right, baseline = 24, 24, 168
    usable = 112
    slot = (width - left - right) / len(days)
    parts = svg_open(
        width,
        height,
        f"Signal: {total} contributions in the last year. Busiest day {busiest['date']} with {busiest['count']}.",
    )
    parts.append(
        f'<text x="24" y="32" fill="{CYAN}" font-family="{FONT}" font-size="16" letter-spacing="2">SIGNAL  //  {total} IN THE LAST YEAR</text>'
    )
    parts.append(
        f'<text x="936" y="32" text-anchor="end" fill="{MAGENTA}" font-family="{FONT}" font-size="14">BUSIEST {busiest["date"]} · {busiest["count"]}</text>'
    )
    for index, day in enumerate(days):
        count = day["count"]
        x = left + index * slot
        if count == 0:
            parts.append(
                f'<line x1="{x:.2f}" y1="{baseline}" x2="{x + max(slot - 0.6, 0.4):.2f}" y2="{baseline}" stroke="{LINE}" stroke-width="1"/>'
            )
            continue
        bar = 8 + (count / peak) * usable
        color = MAGENTA if count == peak else CYAN
        opacity = "1" if count >= peak * 0.5 else "0.55"
        y = baseline - bar
        parts.append(
            f'<rect x="{x:.2f}" y="{y:.2f}" width="{max(slot - 0.7, 0.6):.2f}" height="{bar:.2f}" fill="{color}" opacity="{opacity}"/>'
        )
    parts.append(
        f'<text x="24" y="196" fill="{MUTED}" font-family="{FONT}" font-size="13">each bar is one day · magenta marks the busiest day</text>'
    )
    parts.append("</svg>")
    write(ASSETS / "signal.svg", parts)


def main() -> None:
    section_bar("section-work.svg", "01", "WORK", CYAN)
    section_bar("section-about.svg", "02", "ABOUT", MAGENTA)
    section_bar("section-stack.svg", "03", "STACK", CYAN)
    section_bar("section-signal.svg", "04", "SIGNAL", MAGENTA)
    section_bar("section-contact.svg", "05", "CONTACT", CYAN)
    link_button("email.svg", "EMAIL", CYAN)
    link_button("linkedin.svg", "LINKEDIN", MAGENTA)
    link_button("portfolio.svg", "PORTFOLIO", CYAN)
    link_button("github.svg", "GITHUB", MAGENTA)
    about_panel()
    footer_panel()
    open_site()
    signal_strip()
    print("wrote profile assets")


if __name__ == "__main__":
    main()
