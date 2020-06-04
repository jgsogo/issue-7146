conan remove LibC*
conan remove LibB/1.0@demo/testing --force

conan create libC.py LibC/1.6.7-dev.0+master.g1fea313@demo/testing
conan create libC.py LibC/1.6.6+master.g34a1cfb@demo/testing

conan export libB.py LibB/1.0@demo/testing

# Action!
