import os
from collections import namedtuple

SAMPLES_DIR = os.path.dirname(os.path.realpath(__file__))

Sample = namedtuple('Sample', 'path cut_place')

SAMPLES_LIST = [
    Sample("ok_button.png", min),
    Sample("shakeomat_header.png", max),
    Sample("open_coupon_title.png", min),
    Sample("open_coupon_header.png", max),

]


def get_samples_paths():
    return [Sample(os.path.join(SAMPLES_DIR, x.path), x.cut_place) for x in
            SAMPLES_LIST]
