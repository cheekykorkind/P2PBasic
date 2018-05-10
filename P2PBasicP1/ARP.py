import struct;

class ARP:
    def __init__(self, raw=None):
        if raw != None:
            self._hwType = raw[0:2];
            self._protocolType = raw[2:4];
            self._hwSize = raw[4];
            self._protocolSize = raw[5];
            self._opcode = raw[6:8];
            self._senderMac = raw[8:14];
            self._senderIp = raw[14:18];
            self._targetMac = raw[18:24];
            self._targetIp = raw[24:28];

    @property
    def hwType(self):
        return self._hwType;

    @hwType.setter
    def hwType(self, hwType):
        self._hwType = struct.unpack('!H',hwType);

    @property
    def protocolType(self):
        return self._protocolType;

    @protocolType.setter
    def protocolType(self, protocolType):
        self._protocolType = struct.unpack('!H',protocolType);

    @property
    def hwSize(self):
        return self._hwSize;

    @hwSize.setter
    def hwSize(self, hwSize):
        self._hwSize = struct.unpack('!H',hwSize);

    @property
    def protocolSize(self):
        return self._protocolSize;

    @protocolSize.setter
    def protocolSize(self, protocolSize):
        self._protocolSize = struct.unpack('!H',protocolSize);

    @property
    def opcode(self):
        return self._opcode;

    @opcode.setter
    def opcode(self, opcode):
        self._opcode = struct.unpack('!H',opcode);

    @property
    def senderMac(self):
        senderMac = struct.unpack('!BBBBBB', self._senderMac);
        return '%02x:%02x:%02x:%02x:%02x:%02x' % senderMac;

    @senderMac.setter
    def senderMac(self, senderMac):
        if '-' in senderMac:
            senderMac = senderMac.split('-');
        elif ':' in senderMac:
            senderMac = senderMac.split(':');

        senderMac = ''.join(senderMac);
        self._senderMac = bytes.fromhex(senderMac);

    @property
    def senderIp(self):
        senderIp = struct.unpack('!BBBB', self._senderIp);
        return '%d.%d.%d.%d' % senderIp;

    @senderIp.setter
    def senderIp(self, senderIp):
        if '-' in senderIp:
            senderIp = senderIp.split('-');
        elif ':' in senderIp:
            senderIp = senderIp.split(':');

        senderIp = ''.join(senderIp);
        self._senderIp = bytes.fromhex(senderIp);

    @property
    def targetMac(self):
        targetMac = struct.unpack('!BBBBBB', self._targetMac);
        return '%02x:%02x:%02x:%02x:%02x:%02x' % targetMac;

    @targetMac.setter
    def targetMac(self, targetMac):
        if '-' in targetMac:
            targetMac = targetMac.split('-');
        elif ':' in targetMac:
            targetMac = targetMac.split(':');

        targetMac = ''.join(targetMac);
        self._targetMac = bytes.fromhex(targetMac);

    @property
    def targetIp(self):
        targetIp = struct.unpack('!BBBB', self._targetIp);
        return '%d.%d.%d.%d' % targetIp;

    @targetIp.setter
    def targetIp(self, targetIp):
        if '-' in targetIp:
            targetIp = targetIp.split('-');
        elif ':' in targetIp:
            targetIp = targetIp.split(':');

        targetIp = ''.join(targetIp);
        self._targetIp = bytes.fromhex(targetIp);
