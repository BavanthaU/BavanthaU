#!/usr/bin/env python3
"""
Generate an SVG badge showing the total commit contributions for the current calendar year.
Uses GitHub's GraphQL API via the GITHUB_TOKEN provided in the GitHub Actions environment.
"""

from __future__ import annotations

import datetime as dt
import json
import os
import sys
from pathlib import Path
from textwrap import dedent

import urllib.request


REPO_ROOT = Path(__file__).resolve().parents[1]
BADGE_PATH = REPO_ROOT / "assets" / "current_year_commits.svg"


def query_commit_total(token: str, login: str) -> int:
    """Return total commit contributions for the current calendar year."""
    now = dt.datetime.utcnow()
    start = dt.datetime(year=now.year, month=1, day=1)

    query = dedent(
        """
        query($login: String!, $from: DateTime!, $to: DateTime!) {
          user(login: $login) {
            contributionsCollection(from: $from, to: $to) {
              totalCommitContributions
            }
          }
        }
        """
    )

    payload = {
        "query": query,
        "variables": {
            "login": login,
            "from": start.isoformat() + "Z",
            "to": now.isoformat() + "Z",
        },
    }

    req = urllib.request.Request(
        url="https://api.github.com/graphql",
        data=json.dumps(payload).encode("utf-8"),
        headers={
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
            "User-Agent": "commit-badge-script",
        },
    )

    try:
        with urllib.request.urlopen(req) as resp:
            result = json.load(resp)
    except urllib.error.HTTPError as exc:
        raise RuntimeError(f"GitHub API request failed: {exc}") from exc

    if "errors" in result:
        raise RuntimeError(f"GitHub API returned errors: {result['errors']}")

    try:
        contributions = result["data"]["user"]["contributionsCollection"][
            "totalCommitContributions"
        ]
    except KeyError as exc:
        raise RuntimeError(f"Unexpected API response shape: {result}") from exc

    return int(contributions)


def render_badge(count: int) -> str:
    """Render a simple flat badge SVG."""
    label = "Commits (YTD)"
    value = str(count)
    label_width = max(95, 6 * len(label) + 20)
    value_width = max(70, 10 * len(value) + 20)
    total_width = label_width + value_width

    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{total_width}" height="28" role="img" aria-label="{label}: {value}">
  <linearGradient id="smooth" x2="0" y2="100%">
    <stop offset="0" stop-color="#bbb" stop-opacity=".1"/>
    <stop offset="1" stop-opacity=".1"/>
  </linearGradient>
  <mask id="round">
    <rect width="{total_width}" height="28" rx="4" fill="#fff"/>
  </mask>
  <g mask="url(#round)">
    <rect width="{label_width}" height="28" fill="#555"/>
    <rect x="{label_width}" width="{value_width}" height="28" fill="#0d6efd"/>
    <rect width="{total_width}" height="28" fill="url(#smooth)"/>
  </g>
  <g fill="#fff" text-anchor="middle" font-family="DejaVu Sans,Verdana,Geneva,sans-serif" text-rendering="geometricPrecision" font-size="14">
    <text x="{label_width / 2:.1f}" y="19">{label}</text>
    <text x="{label_width + value_width / 2:.1f}" y="19">{value}</text>
  </g>
</svg>
"""


def main() -> int:
    token = os.environ.get("GITHUB_TOKEN")
    login = os.environ.get("GITHUB_PROFILE_LOGIN") or os.environ.get("GITHUB_ACTOR")

    if not token:
        print("Environment variable GITHUB_TOKEN is required.", file=sys.stderr)
        return 1
    if not login:
        print("Unable to determine GitHub login.", file=sys.stderr)
        return 1

    count = query_commit_total(token, login)
    svg = render_badge(count)

    BADGE_PATH.parent.mkdir(parents=True, exist_ok=True)
    BADGE_PATH.write_text(svg, encoding="utf-8")

    print(f"Wrote badge with {count} commits to {BADGE_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
