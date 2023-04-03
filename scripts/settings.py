# -*- coding: utf-8 -*-
# Time       : 2022/2/15 17:42
# Author     : 0x7C2f
# Github     : https://github.com/0x7C2f
# Description:
import os
from dataclasses import dataclass
from os.path import join

__all__ = ["config"]


@dataclass
class Config:
    dir_database: str = "datas"

    HCAPTCHA_DEMO_API = "https://{}"
    NO_OF_TABS = 1;
    DELAY = 160;
    ENABLE_RECAPTCHA_FAUCET = False;
    ENABLE_HCAPTCHA_FAUCET = True;
    CLOSE_ALL_OTHER_WINDOWS = True
    FAUCETPAY_EMAIL = "cw_2049080@outlook.com"
    bitcoin = "17SnGheZZTzBoKY6J1GWPfZb1Ny7ZP6yE4"
    binance = "0xEBe0A4e8e46bcE0A31095e295b2c7A4308969e72"
    bitcoincash = "bitcoincash:qqalc9q5svqnh942tp824e3mqnnzcql56vczw7sqf0"
    dash = "XieKAAwx7rUAtCksqweLej22bgiegAUrjR"
    dogecoin = "D8xe499GSmF98fGaxPQpX4us333v9pf3QS"
    digibyte = "DQFYjUJjCwDKjgCHeFncHtKpBG9m9ThL9n"
    ethereum = "0xf4a7163daA3deb816E21B893ff8D159fDd4135Cf"
    feyorra = "0xf4a7163daA3deb816E21B893ff8D159fDd4135Cf"
    litecoin = "ltc1q7jvy0x6psvjyxtmvxsj0zac5vu5cncy50jf36r"
    solana = "EzSf7ydSwzXDsHPFmFBwwLwvAtBL9nxR11rcoanq8N7w"
    tron = "TY59Z46m6K1zKxauu99jQ4j2wy9kHzWn7o"
    tether = "TY59Z46m6K1zKxauu99jQ4j2wy9kHzWn7o"
    zcash = "t1PfPNL76xJc8RCv45MLNACSD3MLVeUvNkF"

    SITE_KEYS = {
        "emoticonfaucet": "emoticonfaucet.com",
    }

    # https://www.wappalyzer.com/technologies/security/hcaptcha/
    HCAPTCHA_DEMO_SITES = [
        # [√] label: Tags follow point-in-time changes
        HCAPTCHA_DEMO_API.format(SITE_KEYS["emoticonfaucet"]),
    ]

    def __post_init__(self):
        os.makedirs(self.dir_database, exist_ok=True)
        self.path_objects_yaml = join(self.dir_database, "objects.yaml")


config = Config()
