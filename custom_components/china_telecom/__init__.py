DOMAIN = "china_telecom"

def setup(hass, config):
    hass.states.set('china_telecom.test', 'OK!')
    return True
