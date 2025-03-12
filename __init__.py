DOMAIN = "ha_china_telecom"

def setup(hass, config):
    hass.states.set('ha_china_telecom.test', 'OK!')
    return True
