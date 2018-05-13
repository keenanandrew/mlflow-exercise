from __future__ import print_function

# import time
import sys

from mlflow import log_metric, log_parameter, log_output_files

if __name__ == "__main__":
    print("Running some other version of {}".format(sys.argv[0]))
    log_parameter("param1", 5)
    # time.sleep(5)
    log_metric("foo", 5)
    # time.sleep(5)
    log_metric("foo", 6)
    # time.sleep(5)
    log_metric("foo", 7)
    log_output_files("outputs")
