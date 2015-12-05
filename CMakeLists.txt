cmake_minimum_required (VERSION 2.6)

project (gco CXX)

set (GCO_VERSION_MAJOR 3)
set (GCO_VERSION_MINOR 0)
set (GCO_VERSION_PATCH 0)
set (GCO_VERSION_STRING ${GCO_VERSION_MAJOR}.${GCO_VERSION_MINOR}.${GCO_VERSION_PATCH})

set (SRCS GCoptimization.cpp graph.cpp LinkedBlockList.cpp maxflow.cpp)
set (HDRS block.h energy.h GCoptimization.h graph.h LinkedBlockList.h)

add_library (gco SHARED ${SRCS})
set_target_properties (gco PROPERTIES
    VERSION ${GCO_VERSION_STRING}
    SOVERSION ${GCO_VERSION_MAJOR}
)

install (TARGETS gco LIBRARY DESTINATION lib${LIB_SUFFIX})
install (FILES ${HDRS} DESTINATION include/gco)
