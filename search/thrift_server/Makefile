include Rules.mk

CXXFLAGS += -I./gen-cpp -I/usr/include/thrift -DHAVE_INTTYPES_H -DHAVE_NETINET_IN_H -D_FILE_OFFSET_BITS=64 -DSS_DOCID_BITS=256
GEN_SRC=./gen-cpp/Blacklist.cpp  ./gen-cpp/blacklist_constants.cpp ./gen-cpp/blacklist_types.cpp
GEN_OBJS = $(GEN_SRC:.cpp=.o)
CXXSRCS = $(wildcard *.cpp)
OBJS = $(CSRCS:.c=.o) $(CXXSRCS:.cpp=.o)

all: blserver

blserver: BlacklistServer.o Configuration.o ${GEN_OBJS}
	$(LD) -o $@ $^ $(LDFLAGS) -lthrift -lACE -lssplatform


.PHONY: clean
	

clean:
	rm $(OBJS) $(GEN_OBJS)
