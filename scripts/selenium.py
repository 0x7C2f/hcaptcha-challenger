# -*- coding: utf-8 -*-
# Time       : 2022/9/23 17:28
# Author     : 0x7C2f
# Github     : https://github.com/0x7C2f
# Description:
import time
import typing


from selenium.common.exceptions import (
    ElementNotInteractableException,
    ElementClickInterceptedException,
)
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

import hcaptcha_challenger as solver
from hcaptcha_challenger import HolyChallenger
from hcaptcha_challenger.exceptions import ChallengePassed

# Existing user data
email = "cw_2049080@outlook.com"
country = "United States"
headless = False
NO_OF_TABS = 1;
DELAY = 160;
ENABLE_RECAPTCHA_FAUCET = False;
ENABLE_HCAPTCHA_FAUCET = True;
CLOSE_ALL_OTHER_WINDOWS = True;
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

# Init local-side of the ModelHub
solver.install()

def hit_challenge(ctx, challenger: HolyChallenger, retries: int = 10) -> typing.Optional[str]:
    """
    Use `anti_checkbox()` `anti_hcaptcha()` to be flexible to challenges
    :param ctx:
    :param challenger:
    :param retries:
    :return:
    """
    if challenger.utils.face_the_checkbox(ctx):
        challenger.anti_checkbox(ctx)
        if res := challenger.utils.get_hcaptcha_response(ctx):
            return res

    for _ in range(retries):
        try:
            if (resp := challenger.anti_hcaptcha(ctx)) is None:
                continue
            if resp == challenger.CHALLENGE_SUCCESS:
                return challenger.utils.get_hcaptcha_response(ctx)
        except ChallengePassed:
            return challenger.utils.get_hcaptcha_response(ctx)
        challenger.utils.refresh(ctx)
        time.sleep(1)


def bytedance():
    # New Challenger
    challenger = solver.new_challenger(screenshot=True, debug=True)

    # Replace selenium.webdriver.Chrome with CTX
    ctx = solver.get_challenge_ctx(silence=headless)

    ctx.get("https://shortlinksfaucet.xyz/?p=instantpayingfaucets")

    
    ctx.quit()
if __name__ == "__main__":
    bytedance()
