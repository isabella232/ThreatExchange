# Copyright (c) Facebook, Inc. and its affiliates. All Rights Reserved

"""
Typed representations (dataclasses only) for interfacing with the
threatexchange API.
"""

from datetime import datetime
from dateutil.parser import parse
from dataclasses import dataclass


def _parse_datetime_from_iso_8601(datestr: str) -> datetime:
    """
    Parses strings representing date like 2019-05-20T16:44:47+0000 from the
    graph api into datetime objects.
    """
    return parse(datestr)


@dataclass
class ThreatPrivacyGroup:
    id: str
    name: str
    description: str
    members_can_see: bool
    members_can_use: bool
    last_updated: datetime

    @classmethod
    def from_graph_api_dict(cls, d: dict) -> "ThreatPrivacyGroup":
        return cls(
            d["id"],
            d["name"],
            d["description"],
            bool(d["members_can_see"]),
            bool(d["members_can_use"]),
            bool(d["threat_updates_enabled"]),
            _parse_datetime_from_iso_8601(d["last_updated"]),
        )
