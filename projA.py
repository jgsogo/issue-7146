from conans import ConanFile


class Recipe(ConanFile):
    name = "ProjA"
    version = "1.0"

    def requirements(self):
        self.requires("LibB/1.0@demo/testing")
        self.requires("LibC/[>=1.6.5-dev <2.0.0-dev, include_prerelease=True]@demo/testing")
