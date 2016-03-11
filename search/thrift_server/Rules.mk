.SUFFIXES: .d

CC := gcc
CXX	:= g++
LD := g++
AR := ar

NODEPS := clean

CFLAGS	+= -g -pipe -Wall \
  -Wextra \
  -Wno-unused-parameter \
  -Wno-missing-field-initializers \
  -Wmissing-include-dirs \
  -Wfloat-equal \
  -Wpointer-arith \
  -Wwrite-strings -Wshadow
CXXFLAGS += -g -pipe -Wall \
  -Wextra \
  -Wno-unused-parameter \
  -Wno-missing-field-initializers \
  -Wmissing-include-dirs \
  -Wfloat-equal \
  -Wpointer-arith \
  -Wwrite-strings -Wshadow

ifdef NDEBUG
	CFLAGS += -O2
	CXXFLAGS += -O2
endif

%.o: %.c
	$(CC) $(CPPFLAGS) $(CFLAGS) -c -o $@ $<

%.o: %.cpp
	$(CXX) $(CPPFLAGS) $(CXXFLAGS) -c -o $@ $<

%.o: %.cc
	$(CXX) $(CPPFLAGS) $(CXXFLAGS) -c -o $@ $<

%.d: %.c
	$(CC) $(CPPFLAGS) $(CFLAGS) -MM -MT $(<:.c=.o) -MF $@ $<

%.d: %.cpp
	$(CXX) $(CPPFLAGS) $(CXXFLAGS) -MM -MT $(<:.cpp=.o) -MF $@ $<

%.d: %.cc
	$(CXX) $(CPPFLAGS) $(CXXFLAGS) -MM -MT $(<:.cc=.o) -MF $@ $<

