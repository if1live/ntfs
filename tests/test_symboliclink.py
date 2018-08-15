import os
from ntfsutils.symboliclink import create
from tests.common import TestDir

class TestSymbolicLink(TestDir):
    def test(self):
        link = 'symboliclink'
        contents = 'bar'
        
        try:
            create(self.FOO, link)
            assert os.path.islink(link) == True
        except OSError as e:
            if str(e) == 'symbolic link privilege not held':
                print(e)
                return
            else:
                raise e
        
        with open(link, 'r') as fd:
            self.assertEqual(fd.read(), self.FOO_CONTENTS)

        with open(self.FOO, 'w') as fd:
            fd.write(contents)

        with open(link, 'r') as fd:
            self.assertEqual(fd.read(), contents)

       