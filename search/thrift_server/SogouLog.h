#ifndef __SogouLog_h__
#define __SogouLog_h__

#include <pthread.h>
#include <time.h>
#include <stdio.h>

#define SOGOU_LOG(levelstr, format_string, ...) \
{ \
  time_t __now__; \
  struct tm __tmnow__; \
  char __timestr__[64]; \
  time(&__now__); \
  localtime_r(&__now__, &__tmnow__); \
  strftime(__timestr__, sizeof(__timestr__), "%F %T", &__tmnow__); \
  fprintf(stderr, "[%s] [%s] [%08x] "format_string, #levelstr, __timestr__, (unsigned int)pthread_self(), ##__VA_ARGS__); \
} \

#define SOGOU_LOG_LINE(levelstr, format_string, ...) \
{ \
  time_t __now__; \
  struct tm __tmnow__; \
  char __timestr__[64]; \
  time(&__now__); \
  localtime_r(&__now__, &__tmnow__); \
  strftime(__timestr__, sizeof(__timestr__), "%F %T", &__tmnow__); \
  fprintf(stderr, "[%s] [%s] [%08x] "format_string"\n", #levelstr, __timestr__, (unsigned int)pthread_self(), ##__VA_ARGS__); \
} \

#endif 
