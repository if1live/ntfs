import os
from ntfsutils.symboliclink import create
from tests.common import TestDir

class TestSymbolicLink(TestDir):
    def test(self):
        link = 'symboliclink'
        contents = 'bar'
        
        create(self.FOO, link)
        assert os.path.islink(link) == True
        
        with open(link, 'r') as fd:
            self.assertEqual(fd.read(), self.FOO_CONTENTS)

        with open(self.FOO, 'w') as fd:
            fd.write(contents)

        with open(link, 'r') as fd:
            self.assertEqual(fd.read(), contents)
