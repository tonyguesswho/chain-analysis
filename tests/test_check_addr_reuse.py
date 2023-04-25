import pytest

from analyser.utils.helpers import check_address_reuse


@pytest.mark.parametrize("psbt_base64, expected_result", [
    ("cHNidP8BAFICAAAAAdBFTdfGHrTaikzvaTKAhExJuVcGOREES1pMk+a4GaJAAAAAAAD9////AQAvaFkAAAAAFgAUXe1tW5cd6c6fp5s7yQeZvGELmyYAAAAAAAEAhQIAAAABAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD/////BAK9AAD/////AgD5ApUAAAAAFgAUXe1tW5cd6c6fp5s7yQeZvGELmyYAAAAAAAAAACZqJKohqe3i9hw/cdHe/T+pmd+jaVN1XGkGiXmZYrSL69g2l06M+QAAAAABAR8A+QKVAAAAABYAFF3tbVuXHenOn6ebO8kHmbxhC5smAQhrAkcwRAIgB6BbgRymkVNZZ8watf8OIrjUeKlR4Q3SPbsb5vlBUBACIBTeDjLV2+Yj/+vg26mXNbKZhmjj6Jt+4QqBQISEo9VZASECEpeD7Cqlzuv2Yt1WI+NhvWXPNVQq+XzDTwk5RDEYs2UAIgICEpeD7Cqlzuv2Yt1WI+NhvWXPNVQq+XzDTwk5RDEYs2UMio6FlQAAAAAAAAAAAA==",
     {"status": True, "message": "Address reuse detected", 'inputs': ['bc1qthkk6kuhrh5ua8a8nvaujpueh3sshxexm6m8q3'],
         'outputs': ['bc1qthkk6kuhrh5ua8a8nvaujpueh3sshxexm6m8q3']}),("cHNidP8BAFICAAAAAdBFTdfGHrTaikzvaTKAhExJuVcGOREES1pMk+a4GaJAAAAAAAD9////AQBlzR0AAAAAFgAUH07rdLvAqWwab5nTbBda6Xg0Q98AAAAAAAEAhQIAAAABAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD/////BAK9AAD/////AgD5ApUAAAAAFgAUXe1tW5cd6c6fp5s7yQeZvGELmyYAAAAAAAAAACZqJKohqe3i9hw/cdHe/T+pmd+jaVN1XGkGiXmZYrSL69g2l06M+QAAAAABAR8A+QKVAAAAABYAFF3tbVuXHenOn6ebO8kHmbxhC5smAQhrAkcwRAIgZGDkxdepdIYHZEhITaZem41Rc/n99csk9RNxDrRDrKkCIE1MniWw0E5wyuVc1fhb7dkBsfwb2oGgGsNYMY8vgLFMASECEpeD7Cqlzuv2Yt1WI+NhvWXPNVQq+XzDTwk5RDEYs2UAAA==",{'status': False, 'inputs': ['bc1qthkk6kuhrh5ua8a8nvaujpueh3sshxexm6m8q3'], 'outputs': ['bc1qra8wka9mcz5kcxn0n8fkc966a9urgs7lfs2208'], "message": "No address reuse detected"})
])
def test_check_address_reuse(psbt_base64, expected_result):
    result = check_address_reuse(psbt_base64)
    assert result == expected_result