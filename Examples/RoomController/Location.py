import geocoder

def getCurrentCity():
    try:
        g = geocoder.ip('me')
        return g.city
    except:
        return 'Unknown'