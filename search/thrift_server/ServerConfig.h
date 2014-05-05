#ifndef SERVERCONFIG_H_
#define SERVERCONFIG_H_

#include <string>

struct ServerConfig {
	std::string host;
	int port;

	std::string blFile;
};
#endif
