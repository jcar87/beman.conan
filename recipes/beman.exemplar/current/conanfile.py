from conan import ConanFile
from conan.tools.build import check_min_cppstd
from conan.tools.cmake import CMake, cmake_layout
from conan.tools.files import get
import os


class BemanExemplarConan(ConanFile):
    name = "beman.exemplar"
    version = "2.2.1"
    url = "https://github.com/bemanproject/exemplar"
    description = "A Beman Library Exemplar"
    package_type = "library"
    settings = "os", "arch", "compiler", "build_type"
    generators = "CMakeToolchain", "CMakeDeps"
    options = {"shared": [True, False]}
    default_options = {"shared": False}

    def layout(self):
        cmake_layout(self, src_folder="src")

    def validate(self):
        check_min_cppstd(self, 17)

    def requirements(self):
        self.test_requires("gtest/[^1.17.0]")
        self.tool_requires("beman.infra/[*]")

    def source(self):
        get(self, **self.conan_data["sources"][self.version], strip_root=True)

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()
        cmake.test()

    def package(self):
        cmake = CMake(self)
        cmake.install()
        
    def package_info(self):
        self.cpp_info.libs = ["beman.exemplar"]

        # CMakeDeps: use the generated config files instead
        self.cpp_info.set_property("cmake_find_mode", "none")
        self.cpp_info.builddirs.append(os.path.join("lib", "cmake", "beman.exemplar"))