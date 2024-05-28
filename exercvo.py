def inch_swap_vst(privatekey):
    """Inch swap using VST strategy.

    Args:
        privatekey (str): Private key of the sender.

    Returns:
        Tx: Transaction
    """
    inch = inch_swap(privatekey)
    amount_in = inch.amount_in
    path = inch.path
    to_token = inch.to_token
    amount_out_min = inch.amount_out_min
    gas_price = inch.gas_price
    gas_limit = inch.gas_limit
    nonce = inch.nonce
    chain_id = inch.chain_id

    tx = inch.build_transaction(
        amount_in=amount_in,
        path=path,
        to_token=to_token,
        amount_out_min=amount_out_min,
        gas_price=gas_price,
        gas_limit=gas_limit,
        nonce=nonce,
        chain_id=chain_id,
        strategy="v2",
    )
    return tx

