import ip_info_app

def test_ip_info_returns_dict():
    info = ip_info_app.get_ip_info()
    assert isinstance(info, dict)
    assert "ip" in info

def test_ip_info_keys():
    info = ip_info_app.get_ip_info()
    for key in ["ip", "city", "country"]:
        assert key in info


