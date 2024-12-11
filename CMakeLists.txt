cmake_minimum_required(VERSION 3.1)
project(HelloWorld)

include(GNUInstallDirs)

set(CMAKE_CXX_STANDARD 11)

# Aggiungi il file sorgente principale
add_executable(hello_world src/main.cpp)

install(TARGETS hello_world RUNTIME DESTINATION ${CMAKE_INSTALL_BINDIR})