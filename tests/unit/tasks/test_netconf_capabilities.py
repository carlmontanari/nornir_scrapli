from scrapli_netconf import NetconfDriver


def test_netconf_get_capabilities(nornir_netconf, monkeypatch):
    from nornir_scrapli.tasks import netconf_capabilities

    def mock_open(cls):
        cls.server_capabilities = ["racecar"]
        pass

    monkeypatch.setattr(NetconfDriver, "open", mock_open)

    result = nornir_netconf.run(task=netconf_capabilities)
    assert result["sea-ios-1"].result == ["racecar"]
    assert result["sea-ios-1"].failed is False
    assert result["sea-ios-1"].changed is False
