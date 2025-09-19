### Conan recipes for Beman project


Clone folder and add as local recipes index:

```
git clone https://github.com/jcar87/beman.conan.git
conan remote add beman ./beman.conan
```

Note: Conan Center needs to be configured as a remote as well

Build and run example project:

Note: make sure Conan's `compiler.cppstd` is C++20 or higher

```
cd examples/optional
conan install . -s compiler.cppstd=gnu20
cmake --preset conan-release
cmake --build --preset conan-release
./build/Release/example
```