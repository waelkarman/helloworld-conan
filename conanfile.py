from conans import ConanFile, CMake

class HelloWorldConan(ConanFile):
    name = "HelloWorld"
    version = "1.0"
    license = "MIT"
    author = "Your Name <your.email@example.com>"
    description = "Simple Hello World C++ project"
    topics = ("conan", "hello world", "cpp")
    settings = "os", "compiler", "build_type", "arch"
    requires = []  # Nessuna dipendenza esterna
    generators = "cmake"  # Usa CMake come generatore

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        self.copy("*", dst="bin", src="bin")

    def package_info(self):
        self.cpp_info.bindirs = ["bin"]
