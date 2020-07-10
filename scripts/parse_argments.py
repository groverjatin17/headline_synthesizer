import argparse


def get_new_channel():
    ap = argparse.ArgumentParser()
    ap.add_argument("-n", "--newsChannel", required=True,
                    help="Type of New Media to scrap")
    args = vars(ap.parse_args())
    return args['newsChannel']
