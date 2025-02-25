import os
import sys
from pathlib import Path

import backtrader as bt


def main():
    print(f"sys.argv[0] : {sys.argv[0]}")
    print(f"os.path.abspath(sys.argv[0] : {os.path.abspath(sys.argv[0])}")
    print(
        f"os.path.dirname(os.path.abspath(sys.argv[0])) : {os.path.dirname(os.path.abspath(sys.argv[0]))}"
    )

    modpath = os.path.dirname(os.path.abspath(sys.argv[0]))
    datapath = os.path.join(modpath, "../../datas/orcl-1995-2014.txt")

    print(f"os.path.join(modpath, '../../datas/orcl-1995-2014.txt') : {datapath}")


if __name__ == "__main__":
    main()
