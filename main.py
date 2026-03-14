#!/usr/bin/env python3
import sys
from src.search_agent import run


def main() -> None:
    question = " ".join(sys.argv[1:]) if len(sys.argv) > 1 else input("请输入你的问题: ").strip()
    if question:
        run(question)


if __name__ == "__main__":
    main()
