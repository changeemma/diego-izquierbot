#!/usr/bin/env python3
#

from gatoway.gatoway import Gatoway
from scripts.gatomon_cfg import *

import logging


def main():

    logging.info("")
    logging.info("/*********************** GATOMON ***********************/")
    logging.info("")
    logging.info(f" Interval: {GATOMON_WANGW_CHECK_INTERVAL}s")
    logging.info("")

    gw = Gatoway(
        gateway=GATOMON_WANGW_GATEWAY,
        alarm_threshold=GATOMON_WANGW_ALARM_THRESHOLD,
        dismiss_threshold=GATOMON_WANGW_DISMISS_THRESHOLD,
        check_interval=GATOMON_WANGW_CHECK_INTERVAL,
    )

    logging.info(f" Gateway: {gw.gateway}")
    logging.info(f" Fetching status...")
    logging.info(f"{gw.printStatus()}")
    logging.info("")

    logging.info("")
    logging.info("/*********************************************************/")
    logging.info("")

    # checking loop
    logging.info("")
    logging.info(" BEGINING GATOMON MONITOR...")
    logging.info("")
    try:
        gw.monitor()
    finally:
        logging.info("")
        logging.info(" EXITING GATOMON MONITOR...")
        logging.info("")


if __name__ == "__main__":
    logging.basicConfig(
        filename=GATOMON_WANGW_LOGFILE,
        level=logging.INFO,
        filemode="a",
        format="[%(asctime)s] [%(levelname)s] [gatomon-wangw] %(message)s",
    )
    main()
