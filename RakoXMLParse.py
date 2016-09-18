try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET

rako = ET.ElementTree(file='rako.xml')

rooms = rako.findall('rooms/Room')
print('Room count:', len(rooms))

for room in rooms:
    print('Room', room.find('Title').text)
    print(' ID', room.get("id"))
    print(' Type', room.find('Type').text)
    channels = room.findall('Channel')
    print(' Channels:', len(channels))
    for channel in channels:        
        print(' ID', channel.get("id"))
        print(' Name', channel.find('Name').text)


