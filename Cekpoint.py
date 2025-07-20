import requests
from web3 import Web3
import time
import random
from eth_account.messages import encode_defunct
import config

w3 = Web3(Web3.HTTPProvider(config.RPC_URL))
API_URL = "https://api.pharosnetwork.xyz"

def sign_message(private_key, message="pharos"):
    acct = w3.eth.account.from_key(private_key)
    msg = encode_defunct(text=message)
    signed = acct.sign_message(msg)
    return signed.signature.hex()

def login_with_private_key(private_key):
    address = w3.eth.account.from_key(private_key).address
    signature = sign_message(private_key)
    url = f"{API_URL}/user/login?address={address}&signature={signature}"
    headers = {
        "Origin": "https://testnet.pharosnetwork.xyz",
        "Referer": "https://testnet.pharosnetwork.xyz"
    }
    try:
        response = requests.post(url, headers=headers)
        data = response.json()
        return data.get("data", {}).get("jwt")
    except Exception as e:
        print(f"Gagal login untuk {address}: {e}")
        return None

def get_profile_info(address, bearer_token):
    url = f"{API_URL}/user/profile?address={address}"
    headers = {
        'Authorization': f'Bearer {bearer_token}',
        'Origin': 'https://testnet.pharosnetwork.xyz',
        'Referer': 'https://testnet.pharosnetwork.xyz'
    }
    try:
        res = requests.get(url, headers=headers)
        if res.ok:
            data = res.json()
            poin = data.get("data", {}).get("user_info", {}).get("TotalPoints", 0)
            return poin
        else:
            print(f"Gagal ambil profil untuk {address}, status code: {res.status_code}")
            return 0
    except Exception as e:
        print(f"Gagal ambil profil untuk {address}: {e}")
        return 0

def main():
    try:
        with open("privateKeys.txt", "r") as f:
            private_keys = [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print("File privateKeys.txt tidak ditemukan.")
        return

    total_points = 0

    for pk in private_keys:
        if not pk.startswith("0x"):
            pk = "0x" + pk

        try:
            account = w3.eth.account.from_key(pk)
            address = account.address
        except Exception as e:
            print(f"Private key tidak valid: {e}")
            continue

        token = login_with_private_key(pk)
        if not token:
            print(f"Login gagal untuk {address}")
            continue

        poin = get_profile_info(address, token)
        total_points += poin
        print(f"{address} : {poin}")

        time.sleep(random.uniform(1, 2))

    print("\nTotal poin semua akun:", total_points)

if __name__ == "__main__":
    main()
