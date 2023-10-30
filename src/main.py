#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""a.ari-web.xyz"""

from warnings import filterwarnings as filter_warnings

from a import create_app


def main() -> int:
    """entry/main function"""

    create_app().run("127.0.0.1", 8080, True)

    return 0


if __name__ == "__main__":
    assert main.__annotations__.get("return") is int, "main() should return an integer"

    filter_warnings("error", category=Warning)
    raise SystemExit(main())
