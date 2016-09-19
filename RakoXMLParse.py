try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET
class RakoRoom:
    """docstring for RakoRoom."""
    roomCount = 0
    def __init__(self, id, name):
        super(RakoRoom, self).__init__()
        self.id = id
        self.name = name
        self.scene = 0

        RakoRoom.roomCount +=1

    def setScene(arg):
        pass

rako = ET.ElementTree(file='rako.xml')

RakoRooms = []

rooms = rako.findall('rooms/Room')
print('Room count:', len(rooms))

for room in rooms:
    roomTitle=('Room', room.find('Title').text)
    roomID=(' ID', room.get("id"))
    roomType=(' Type', room.find('Type').text)
    channels = room.findall('Channel')
    roomChannelsNum=(' Channels:', len(channels))
    for channel in channels:
        channelID=(' ID', channel.get("id"))
        channelName=(' Name', channel.find('Name').text)
    RakoRooms.append(RakoRoom(roomID,roomTitle))

for obj in RakoRooms:
    print (obj.name)
