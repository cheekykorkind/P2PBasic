import struct;

class Ethernet:
    def __init__(self, raw=None):
        if raw != None:
            self._dst = raw[:6];
            self._src = raw[6:12];
            self._type = raw[12:14];

    @property
    def dst(self):
        dst = struct.unpack('!BBBBBB',self._dst);
        return '%02x:%02x:%02x:%02x:%02x:%02x' % dst;

    @dst.setter
    def dst(self,dst):
        if '-' in dst:
            dst = dst.split('-');
        elif ':' in dst:
            dst = dst.split(':');
        dst = ''.join(dst);
        self._dst = bytes.fromhex(dex);

    @property
    def src(self):
        src = struct.unpack('!BBBBBB',self._src);
        return '%02x:%02x:%02x:%02x:%02x:%02x' % src;

    @src.setter
    def src(self,src):
        if '-' in src:
            src = src.split('-');
        elif ':' in src:
            src = src.split(':');
        src = ''.join(src);
        self._src = bytes.fromhex(src);

    @property
    def type(self):
        (type,) = struct.unpack('!H', self._type);
        return type;

    @type.setter
    def type(self, type):
        self._type = struct.pack('!H',type);
