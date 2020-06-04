from conans import ConanFile


class Recipe(ConanFile):
    name = "LibB"
    version = "1.0"

    requires = "LibC/[^1.3.0-dev, include_prerelease=True]@demo/testing"
