// This autogenerated skeleton file illustrates how to build a server.
// You should copy it to another filename to avoid overwriting it.

#include "Blacklist.h"
#include <protocol/TBinaryProtocol.h>
#include <server/TSimpleServer.h>
#include <transport/TServerSocket.h>
#include <transport/TBufferTransports.h>

using namespace ::apache::thrift;
using namespace ::apache::thrift::protocol;
using namespace ::apache::thrift::transport;
using namespace ::apache::thrift::server;

using boost::shared_ptr;

using namespace  ::blacklist;

class BlacklistHandler : virtual public BlacklistIf {
 public:
  BlacklistHandler() {
    // Your initialization goes here
  }

  void filter(std::string& _return, const std::string& inStr, const std::string& mf, const std::string& picfilter1) {
    // Your implementation goes here
    printf("filter\n");
  }

  void getdocid(std::string& _return, const std::string& url) {
    // Your implementation goes here
    printf("getdocid\n");
  }

};

int main(int argc, char **argv) {
  int port = 9090;
  shared_ptr<BlacklistHandler> handler(new BlacklistHandler());
  shared_ptr<TProcessor> processor(new BlacklistProcessor(handler));
  shared_ptr<TServerTransport> serverTransport(new TServerSocket(port));
  shared_ptr<TTransportFactory> transportFactory(new TBufferedTransportFactory());
  shared_ptr<TProtocolFactory> protocolFactory(new TBinaryProtocolFactory());

  TSimpleServer server(processor, serverTransport, transportFactory, protocolFactory);
  server.serve();
  return 0;
}

