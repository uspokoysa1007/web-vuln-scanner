#!/usr/bin/env python3
"""web-vuln-scanner — scaffold."""

import argparse


def main() -> None:
    parser = argparse.ArgumentParser(description="web-vuln-scanner: SQLi/XSS scanner")
    parser.add_argument("url", help="target URL")
    args = parser.parse_args()
    print(f"web-vuln-scanner v0.1.0 — scaffold (target: {args.url})")
    # TODO:
    # - краулер и поиск форм
    # - SQLi: error-based и time-based payload'ы
    # - XSS: проверка отражения
    # - отчёты в тексте/JSON


if __name__ == "__main__":
    main()
