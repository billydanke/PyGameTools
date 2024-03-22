from phue import Bridge
import EventManager

hueBridgeIP = '192.168.1.70'
lightsList = []
bridge = Bridge(hueBridgeIP)

def ScanForLights():
    # Find all lights in the Hue system.
    lightsList = bridge.get_light_objects()