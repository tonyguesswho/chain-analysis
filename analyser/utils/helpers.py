from buidl.psbt import PSBT


def decode_psbt(psbt_base64):
    try:
        psbt = PSBT.parse_base64(psbt_base64)
        return {"status": psbt.validate(), "data": psbt}
    except:
      return {"status": False, "message": "Invalid PSBT"}

def check_address_reuse(psbt_base64):
    decoded_psbt = decode_psbt(psbt_base64)
    if not decoded_psbt["status"]:
        return {"status": False, "message": "Invalid PSBT"}
    # check address reuse
    inputs = decoded_psbt["data"].psbt_ins
    inputsAddresses = []

    for idx, val  in enumerate(inputs):
        add = val.prev_tx.tx_outs[val.tx_in.prev_index].script_pubkey.address()
        inputsAddresses.append(add)
    outputs = decoded_psbt["data"].tx_obj.tx_outs
    outputsAddress = []

    for val  in outputs:
        outputsAddress.append(val.script_pubkey.address())

    for val in outputsAddress:
        if val in inputsAddresses:
            return {"status": True, "message": "Address reuse detected", "inputs": inputsAddresses, "outputs": outputsAddress}
    return {"status": False, "inputs": inputsAddresses, "outputs": outputsAddress, "message": "No address reuse detected"}


import bitcoin


def common_inputs(psbtBase64: str) -> bool:
    # Decode the base64-encoded PSBT
    decodedPsbt = decode_psbt(psbtBase64)

    # Error check
    if not decodedPsbt['status'] or not decodedPsbt['data']:
        return False

    psbt = decodedPsbt['data']
    # Get the transaction's inputs
    inputs = psbt.psbt_ins


    # Get the transaction's outputs
    outputs = psbt.tx_obj.tx_outs

    inputAmounts = []
    outputAmounts = []
    # Edge cases
    if len(outputs) == 1 or len(inputs) == 1:
        result = {"status": True, "message":"Common Inputs Detected", "inputs":inputAmounts, "outputs":outputAmounts}
        return result

    # Get the amount of the inputs


    for idx, val in enumerate(inputs):
        psbt_prev_tx_out = val.prev_tx.tx_outs[val.tx_in.prev_index]
        inputAmounts.append(psbt_prev_tx_out.amount)
    print(inputAmounts, "inputAmounts")
    # Get the amount of the outputs
    outputAmounts = [output.amount for output in outputs]

    print(outputAmounts, "outputAmounts")

    # Sort the inputs and outputs in ascending order
    outputAmounts.sort()
    inputAmounts.sort()

    result = {"status": True, "message":"Common Inputs Detected", "inputs":inputAmounts, "outputs":outputAmounts}
    for output in outputAmounts:
        for input in inputAmounts:
            # Check if the output amount is less than or equal to the input.
            # If yes, then the input is enough to spend the output.
            # Other inputs might not be from the same wallet. If it's greater
            # than the input, then the output is likely to be from the same wallet.
            if output <= input:
                result = {"status": False, "message":"No Common Inputs Detected", "inputs":inputAmounts, "outputs":outputAmounts}
            else:
                result = {"status": True, "message":"Common Inputs Detected", "inputs":inputAmounts, "outputs":outputAmounts}

    return result
