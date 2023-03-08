from functools import partial

from utils import lambda_handler
from ping import parse as ping_parse, upload as ping_upload
from speed import parse as speed_parse, upload as speed_upload
from latencyload import parse as load_parse, upload as load_upload


ping_handler = partial(lambda_handler, ping_parse, ping_upload)
speed_handler = partial(lambda_handler, speed_parse, speed_upload)
load_handler = partial(lambda_handler, load_parse, load_upload)










