import codewars_test as test
from kata import mkdirp
import os


@test.describe("Making /tmp/directories/can/be/made/recursively")
def creating_dirs_test():

    @test.it('mkdirp("/tmp","directories","can","be","made","recursively")')
    def test_creating_new_dir():
        mkdirp("/tmp", "directories", "can", "be", "made", "recursively")
        test.expect(
            os.path.exists("/tmp/directories/can/be/made/recursively"),
            "/tmp/directories/can/be/made/recursively does not exist",
        )


@test.describe("Making /usr/share/man/man1 should be idempotent")
def already_existing_dir():

    @test.it('mkdirp("/","usr","share","man","man1")')
    def test_existing_dir():
        mkdirp("/", "usr", "share", "man", "man1")
        test.pass_()
