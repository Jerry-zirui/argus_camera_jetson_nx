cmake_minimum_required(VERSION 3.5)
project(argus_camera LANGUAGES CUDA CXX)

set(CMAKE_MODULE_PATH ${CMAKE_MODULE_PATH} ${CMAKE_SOURCE_DIR}/cmake)
set(CMAKE_CXX_STANDARD 11)

set(TegraMM_ROOT /usr/src/jetson_multimedia_api)

 # set packages
set(TegraMM_INCLUDE_DIRS ${TegraMM_ROOT}/include ${TegraMM_ROOT}/include/libjpeg-8b /usr/include/libdrm)
set(TegraMM_INCLUDES ${TegraMM_INCLUDE_DIRS})
  
find_library(ARGUS_LIBRARY NAMES nvargus HINTS /usr/lib/${CMAKE_LIBRARY_ARCHITECTURE}/tegra)
find_library(V4L2_LIBRARY NAMES v4l2 HINTS /usr/lib/${CMAKE_LIBRARY_ARCHITECTURE}/tegra)
find_library(EGL_LIBRARY EGL HINTS /usr/lib/aarch64-linux-gnu/tegra)
find_library(DRM_LIBRARY drm HINTS /usr/lib/aarch64-linux-gnu/tegra)

set(TegraMM_LIBRARY_DIRS /usr/lib/aarch64-linux-gnu/tegra /usr/lib/aarch64-linux-gnu)
set(TegraMM_LIBRARIES ${ARGUS_LIBRARY} ${V4L2_LIBRARY} ${EGL_LIBRARY} ${DRM_LIBRARY} X11 GLESv2)
file(GLOB TegraMM_COMMON_SOURCES ${TegraMM_ROOT}/samples/common/classes/*.cpp)

include_directories(${TegraMM_INCLUDE_DIRS})
link_directories(${TegraMM_LIBRARY_DIRS})


add_library(argus_camera SHARED
  src/ArgusCamera.cpp
  ${TegraMM_COMMON_SOURCES}
)

message("TegraMM_INCLUDE_DIRS")
message("${TegraMM_INCLUDE_DIRS}")
include_directories(${TegraMM_INCLUDE_DIRS})

target_link_libraries(argus_camera ${TegraMM_LIBRARIES})

set_target_properties(argus_camera PROPERTIES PUBLIC_HEADER 
  "src/ArgusCamera.hpp"
)

install(TARGETS argus_camera
  RUNTIME DESTINATION bin
  LIBRARY DESTINATION lib
  ARCHIVE DESTINATION lib/static
  PUBLIC_HEADER DESTINATION include/argus_camera)

