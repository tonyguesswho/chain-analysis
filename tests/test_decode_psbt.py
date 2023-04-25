import pytest
from buidl.psbt import PSBT

from analyser.utils.helpers import decode_psbt


def test_decode_psbt():
    valid_psbt_base64 = "cHNidP8BAFICAAAAAdBFTdfGHrTaikzvaTKAhExJuVcGOREES1pMk+a4GaJAAAAAAAD9////AQBlzR0AAAAAFgAUH07rdLvAqWwab5nTbBda6Xg0Q98AAAAAAAEAhQIAAAABAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD/////BAK9AAD/////AgD5ApUAAAAAFgAUXe1tW5cd6c6fp5s7yQeZvGELmyYAAAAAAAAAACZqJKohqe3i9hw/cdHe/T+pmd+jaVN1XGkGiXmZYrSL69g2l06M+QAAAAABAR8A+QKVAAAAABYAFF3tbVuXHenOn6ebO8kHmbxhC5smAQhrAkcwRAIgZGDkxdepdIYHZEhITaZem41Rc/n99csk9RNxDrRDrKkCIE1MniWw0E5wyuVc1fhb7dkBsfwb2oGgGsNYMY8vgLFMASECEpeD7Cqlzuv2Yt1WI+NhvWXPNVQq+XzDTwk5RDEYs2UAAA==" # valid PSBT base64 string
    invalid_psbt_base64 = "invalid_psbt" # invalid PSBT base64 string

    # Test valid PSBT decoding
    result = decode_psbt(valid_psbt_base64)
    assert result["status"] == True

    # Test invalid PSBT decoding
    result = decode_psbt(invalid_psbt_base64)
    assert result["status"] == False
    assert result["message"] == "Invalid PSBT"

    # Test empty str
    result = decode_psbt("")
    assert result["status"] == False
    assert result["message"] == "Invalid PSBT"