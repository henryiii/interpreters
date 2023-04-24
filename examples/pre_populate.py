from test.support import interpreters
import textwrap as tw

def wait_for_request(): ...

def test_pre_populate():
    interp = interpreters.create()
    interp.run(tw.dedent("""
        import sys
        sys.path.insert(0, '.')
        import some_lib
        import an_expensive_module
        some_lib.set_up()
        """))
    wait_for_request()
    interp.run(tw.dedent("""
        some_lib.handle_request()
        """))