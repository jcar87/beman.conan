from conan import ConanFile
from conan.tools.build import check_min_cppstd
from conan.tools.cmake import CMake, cmake_layout
from conan.tools.files import get, rmdir
import os


class BemanOptionalConan(ConanFile):
    name = "beman.optional"
    version = "1.0.0"
    url = "https://github.com/bemanproject/optional"
    description = "std::optional extensions adopted for C++26"
    package_type = "header-library"
    settings = "os", "arch", "compiler", "build_type"
    generators = "CMakeToolchain", "CMakeDeps"

    def layout(self):
        cmake_layout(self, src_folder="src")

    def validate(self):
        check_min_cppstd(self, 20)

    def package_id(self):
        self.info.clear()

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
        rmdir(self, os.path.join(self.package_folder, "lib", "cmake")) # (the project's generated cmake config is currently broken)
        rmdir(self, os.path.join(self.package_folder, "bin")) # don't package the sample executables
        
    def package_info(self):
        self.cpp_info.set_property("cmake_file_name", "BemanOptional")
        self.cpp_info.set_property("cmake_target_name", "Beman::Optional::beman_optional")
