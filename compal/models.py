"""Objects used by CH7465LG"""
from dataclasses import dataclass
from enum import Enum
from typing import Optional, List


@dataclass
class SystemInfo:
    docsis_mode: Optional[str] = None
    hardware_version: Optional[str] = None
    mac_address: Optional[str] = None
    serial_number: Optional[str] = None
    uptime: Optional[int] = None
    network_access: Optional[str] = None


@dataclass
class BandSetting:
    radio: Optional[int] = None
    bss_enable: Optional[int] = None
    ssid: Optional[str] = None
    hidden: Optional[str] = None
    bandwidth: Optional[int] = None
    tx_rate: Optional[int] = None
    tx_mode: Optional[int] = None
    security: Optional[int] = None
    multicast_rate: Optional[int] = None
    channel: Optional[int] = None
    pre_shared_key: Optional[str] = None
    re_key: Optional[str] = None
    wpa_algorithm: Optional[int] = None


@dataclass
class RadioSettings:
    nv_country: Optional[int] = None
    band_mode: Optional[int] = None
    channel_range: Optional[int] = None
    bss_coexistence: Optional[int] = None
    son_admin_status: Optional[int] = None
    smart_wifi: Optional[int] = None
    radio_2g: Optional[BandSetting] = None
    radio_5g: Optional[BandSetting] = None


@dataclass
class GuestNetworkEnabling:
    enabled: Optional[bool] = None
    guest_mac: Optional[str] = None


@dataclass
class GuestNetworkProperties:
    ssid: Optional[str] = None
    hidden: Optional[int] = None
    re_key: Optional[int] = None
    security: Optional[int] = None
    pre_shared_key: Optional[str] = None
    wpa_algorithm: Optional[int] = None


@dataclass
class GuestNetworkSettings:
    enabling_2g: GuestNetworkEnabling
    enabling_5g: GuestNetworkEnabling
    properties: GuestNetworkProperties


class FilterAction(Enum):
    """
    Filter action, used by internet access filters
    """

    add = 1
    delete = 2
    enable = 3


class NatMode(Enum):
    """
    Values for NAT-Mode
    """

    enabled = 1
    disabled = 2


@dataclass
class PortForward:
    local_ip: Optional[str] = None
    ext_port: Optional[int] = None
    int_port: Optional[int] = None
    proto: Optional[str] = None
    enabled: Optional[bool] = None
    delete: Optional[bool] = None
    idd: Optional[str] = None
    id: Optional[str] = None
    lan_ip: Optional[str] = None


class Proto(Enum):
    """
    protocol (from form): 1 = tcp, 2 = udp, 3 = both
    """

    tcp = 1
    udp = 2
    both = 3


class TimerMode(Enum):
    """
    Timermodes used for internet access filtering
    """

    generaltime = 1
    dailytime = 2
