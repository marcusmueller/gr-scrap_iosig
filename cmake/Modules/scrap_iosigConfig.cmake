INCLUDE(FindPkgConfig)
PKG_CHECK_MODULES(PC_SCRAP_IOSIG scrap_iosig)

FIND_PATH(
    SCRAP_IOSIG_INCLUDE_DIRS
    NAMES scrap_iosig/api.h
    HINTS $ENV{SCRAP_IOSIG_DIR}/include
        ${PC_SCRAP_IOSIG_INCLUDEDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/include
          /usr/local/include
          /usr/include
)

FIND_LIBRARY(
    SCRAP_IOSIG_LIBRARIES
    NAMES gnuradio-scrap_iosig
    HINTS $ENV{SCRAP_IOSIG_DIR}/lib
        ${PC_SCRAP_IOSIG_LIBDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/lib
          ${CMAKE_INSTALL_PREFIX}/lib64
          /usr/local/lib
          /usr/local/lib64
          /usr/lib
          /usr/lib64
)

INCLUDE(FindPackageHandleStandardArgs)
FIND_PACKAGE_HANDLE_STANDARD_ARGS(SCRAP_IOSIG DEFAULT_MSG SCRAP_IOSIG_LIBRARIES SCRAP_IOSIG_INCLUDE_DIRS)
MARK_AS_ADVANCED(SCRAP_IOSIG_LIBRARIES SCRAP_IOSIG_INCLUDE_DIRS)

