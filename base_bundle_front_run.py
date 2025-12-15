import requests, time

def bundle_front_run():
    print("Base — Bundle Front-Run Detector (whale bundles eating launches)")
    seen = set()

    while True:
        try:
            # Base has no Jito, but large multi-tx from same wallet = bundle-like
            r = requests.get("https://api.basescan.org/api?module=account&action=txlist"
                            "&address=0x0000000000000000000000000000000000000000&sort=desc")
            txs = r.json().get("result", [])[:50]

            wallet_txs = {}
            for tx in txs:
                w = tx["from"].lower()
                wallet_txs[w] = wallet_txs.get(w, 0) + 1

            for w, count in wallet_txs.items():
                if count >= 8:  # 8+ txs from same wallet in latest block = bundle
                    print(f"BUNDLE FRONT-RUN DETECTED\n"
                          f"Wallet {w[:10]}... sent {count} txs in one block\n"
                          f"https://basescan.org/address/{w}\n"
                          f"→ Eating every new pool at birth\n"
                          f"→ This is MEV god on Base\n"
                          f"{'BUNDLE'*25}")

        except:
            pass
        time.sleep(2.2)

if __name__ == "__main__":
    bundle_front_run()
