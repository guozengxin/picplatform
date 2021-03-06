#
# Autogenerated by Thrift Compiler (0.8.0)
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#
#  options string: py
#

from thrift.Thrift import TType, TMessageType, TException
from ttypes import *
from thrift.Thrift import TProcessor
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol, TProtocol
try:
  from thrift.protocol import fastbinary
except:
  fastbinary = None


class Iface:
  def filter(self, inStr, mf, picfilter1):
    """
    Parameters:
     - inStr
     - mf
     - picfilter1
    """
    pass

  def getdocid(self, url):
    """
    Parameters:
     - url
    """
    pass


class Client(Iface):
  def __init__(self, iprot, oprot=None):
    self._iprot = self._oprot = iprot
    if oprot is not None:
      self._oprot = oprot
    self._seqid = 0

  def filter(self, inStr, mf, picfilter1):
    """
    Parameters:
     - inStr
     - mf
     - picfilter1
    """
    self.send_filter(inStr, mf, picfilter1)
    return self.recv_filter()

  def send_filter(self, inStr, mf, picfilter1):
    self._oprot.writeMessageBegin('filter', TMessageType.CALL, self._seqid)
    args = filter_args()
    args.inStr = inStr
    args.mf = mf
    args.picfilter1 = picfilter1
    args.write(self._oprot)
    self._oprot.writeMessageEnd()
    self._oprot.trans.flush()

  def recv_filter(self, ):
    (fname, mtype, rseqid) = self._iprot.readMessageBegin()
    if mtype == TMessageType.EXCEPTION:
      x = TApplicationException()
      x.read(self._iprot)
      self._iprot.readMessageEnd()
      raise x
    result = filter_result()
    result.read(self._iprot)
    self._iprot.readMessageEnd()
    if result.success is not None:
      return result.success
    raise TApplicationException(TApplicationException.MISSING_RESULT, "filter failed: unknown result");

  def getdocid(self, url):
    """
    Parameters:
     - url
    """
    self.send_getdocid(url)
    return self.recv_getdocid()

  def send_getdocid(self, url):
    self._oprot.writeMessageBegin('getdocid', TMessageType.CALL, self._seqid)
    args = getdocid_args()
    args.url = url
    args.write(self._oprot)
    self._oprot.writeMessageEnd()
    self._oprot.trans.flush()

  def recv_getdocid(self, ):
    (fname, mtype, rseqid) = self._iprot.readMessageBegin()
    if mtype == TMessageType.EXCEPTION:
      x = TApplicationException()
      x.read(self._iprot)
      self._iprot.readMessageEnd()
      raise x
    result = getdocid_result()
    result.read(self._iprot)
    self._iprot.readMessageEnd()
    if result.success is not None:
      return result.success
    raise TApplicationException(TApplicationException.MISSING_RESULT, "getdocid failed: unknown result");


class Processor(Iface, TProcessor):
  def __init__(self, handler):
    self._handler = handler
    self._processMap = {}
    self._processMap["filter"] = Processor.process_filter
    self._processMap["getdocid"] = Processor.process_getdocid

  def process(self, iprot, oprot):
    (name, type, seqid) = iprot.readMessageBegin()
    if name not in self._processMap:
      iprot.skip(TType.STRUCT)
      iprot.readMessageEnd()
      x = TApplicationException(TApplicationException.UNKNOWN_METHOD, 'Unknown function %s' % (name))
      oprot.writeMessageBegin(name, TMessageType.EXCEPTION, seqid)
      x.write(oprot)
      oprot.writeMessageEnd()
      oprot.trans.flush()
      return
    else:
      self._processMap[name](self, seqid, iprot, oprot)
    return True

  def process_filter(self, seqid, iprot, oprot):
    args = filter_args()
    args.read(iprot)
    iprot.readMessageEnd()
    result = filter_result()
    result.success = self._handler.filter(args.inStr, args.mf, args.picfilter1)
    oprot.writeMessageBegin("filter", TMessageType.REPLY, seqid)
    result.write(oprot)
    oprot.writeMessageEnd()
    oprot.trans.flush()

  def process_getdocid(self, seqid, iprot, oprot):
    args = getdocid_args()
    args.read(iprot)
    iprot.readMessageEnd()
    result = getdocid_result()
    result.success = self._handler.getdocid(args.url)
    oprot.writeMessageBegin("getdocid", TMessageType.REPLY, seqid)
    result.write(oprot)
    oprot.writeMessageEnd()
    oprot.trans.flush()


# HELPER FUNCTIONS AND STRUCTURES

class filter_args:
  """
  Attributes:
   - inStr
   - mf
   - picfilter1
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'inStr', None, None, ), # 1
    (2, TType.STRING, 'mf', None, None, ), # 2
    (3, TType.STRING, 'picfilter1', None, None, ), # 3
  )

  def __init__(self, inStr=None, mf=None, picfilter1=None,):
    self.inStr = inStr
    self.mf = mf
    self.picfilter1 = picfilter1

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRING:
          self.inStr = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRING:
          self.mf = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.STRING:
          self.picfilter1 = iprot.readString();
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('filter_args')
    if self.inStr is not None:
      oprot.writeFieldBegin('inStr', TType.STRING, 1)
      oprot.writeString(self.inStr)
      oprot.writeFieldEnd()
    if self.mf is not None:
      oprot.writeFieldBegin('mf', TType.STRING, 2)
      oprot.writeString(self.mf)
      oprot.writeFieldEnd()
    if self.picfilter1 is not None:
      oprot.writeFieldBegin('picfilter1', TType.STRING, 3)
      oprot.writeString(self.picfilter1)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class filter_result:
  """
  Attributes:
   - success
  """

  thrift_spec = (
    (0, TType.STRING, 'success', None, None, ), # 0
  )

  def __init__(self, success=None,):
    self.success = success

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 0:
        if ftype == TType.STRING:
          self.success = iprot.readString();
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('filter_result')
    if self.success is not None:
      oprot.writeFieldBegin('success', TType.STRING, 0)
      oprot.writeString(self.success)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class getdocid_args:
  """
  Attributes:
   - url
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'url', None, None, ), # 1
  )

  def __init__(self, url=None,):
    self.url = url

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRING:
          self.url = iprot.readString();
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('getdocid_args')
    if self.url is not None:
      oprot.writeFieldBegin('url', TType.STRING, 1)
      oprot.writeString(self.url)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class getdocid_result:
  """
  Attributes:
   - success
  """

  thrift_spec = (
    (0, TType.STRING, 'success', None, None, ), # 0
  )

  def __init__(self, success=None,):
    self.success = success

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 0:
        if ftype == TType.STRING:
          self.success = iprot.readString();
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('getdocid_result')
    if self.success is not None:
      oprot.writeFieldBegin('success', TType.STRING, 0)
      oprot.writeString(self.success)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)
