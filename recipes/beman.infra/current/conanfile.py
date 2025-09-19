from conan import ConanFile
from conan.tools.files import copy, get
import os

class BemanConan(ConanFile):
    name = "beman.infra"
    package_type = "build-scripts"
    version = "1.0.0"
    url = "https://github.com/bemanproject/infra"

    def source(self):
        get(self, **self.conan_data["sources"][self.version], strip_root=True)

    def package(self):
        copy(self, pattern="*.cmake", src=os.path.join(self.source_folder, "cmake"), dst=os.path.join(self.package_folder, "cmake"))

    def package_info(self):
        self.cpp_info.builddirs = ["cmake"]
        self.cpp_info.set_property("cmake_file_name", "beman-install-library")