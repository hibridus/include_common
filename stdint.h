#ifndef INCLUDE_COMMON_STDINT_H
#define INCLUDE_COMMON_STDINT_H

#ifdef __cplusplus
extern "C" {
#endif // __cplusplus

/* 8 bits */
typedef signed char   INT8;
typedef unsigned char UINT8, CHAR, BYTE, BOOL;

/* 16 bits */
typedef signed short   INT16;
typedef unsigned short UINT16, SHORT, WORD;

/* 32 bits */
typedef signed int   INT;
typedef unsigned int UINT, DWORD;

/* 64 bits */
typedef signed long long   INT64;
typedef unsigned long long UINT64, QWORD;

/* Pointers */
typedef void* PVOID, LPVOID;
typedef CHAR* STRING;

#ifdef __cplusplus
}
#endif // __cplusplus

#endif // INCLUDE_COMMON_STDINT_H