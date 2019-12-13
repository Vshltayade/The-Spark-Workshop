from typing import DefaultDict, Tuple
from datetime import datetime

default_date = "1970-01-01T00:00:00Z"


def to_epochs(time_string):
    parsed_time = datetime.strptime(time_string, "%Y-%m-%dT%H:%M:%S%z")
    return int(parsed_time.timestamp())

def get_common_field(meta_pairs: DefaultDict[str, str]):
    warc_type = meta_pairs.get("WARC-Type", "")
    target_uri = meta_pairs.get("WARC-Target-URI", "")
    record_id = meta_pairs.get("WARC-Record-ID", "")
    content_type = meta_pairs.get("Content-Type", "")
    block_digest = meta_pairs.get("WARC-Block-Digest", "")
    date = meta_pairs.get("WARC-Date", default_date)
    date_s = to_epochs(date)
    content_length = int(meta_pairs.get("Content-Length", "-1"))
    return warc_type, target_uri, record_id, content_type, block_digest, date_s, content_length

class Warc_Record:
    def __init__(self, meta_pairs: DefaultDict[str, str], response_meta: Tuple[str, str, int], source_html: str):
        warc_type, target_uri, record_id, content_type, block_digest, date_s, content_length = get_common_field(meta_pairs)
        self.warc_type = warc_type
        self.target_uri = target_uri
        self.record_id = record_id
        self.content_type = content_type
        self.block_digest = block_digest
        self.date_s = date_s
        self.content_length = content_length

        self.info_id = meta_pairs.get("WARC-Warcinfo-ID", "")
        self.concurrent_to = meta_pairs.get("WARC-Concurrent-To", "")
        self.ip = meta_pairs.get("WARC-IP-Address", "")
        self.payload_digest = meta_pairs.get("WARC-Payload-Digest", "")
        self.payload_type = meta_pairs.get("WARC-Identified-Payload-Type", "")
        self.html_content_type = response_meta[0]
        self.language = response_meta[1]
        self.html_length = response_meta[2]
        self.html_source = source_html


class Wet_Record:
    def __init__(self, meta_pairs: DefaultDict[str, str], source_html: str):
        warc_type, target_uri, record_id, content_type, block_digest, date_s, content_length = get_common_field(meta_pairs)
        self.warc_type = warc_type
        self.target_uri = target_uri
        self.record_id = record_id
        self.content_type = content_type
        self.block_digest = block_digest
        self.date_s = date_s
        self.content_length = content_length
        self.plain_text = source_html
        self.refers_to = meta_pairs.get("WARC-Refers-To", "")