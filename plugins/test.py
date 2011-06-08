import time
import hgd

def hgd_hook_init(ctx):
    """ test members """

    hgd.dprint(hgd.D_WARN, "testing dprint()");

    print("")
    print(80 * "-")
    print("HGD Scripting backend test!")
    print(80 * "-")

    print("HGD version is: %s" % ctx.hgd_version)
    print("HGD component is: %s" % ctx.component)
    print("protocol version is: %d" % ctx.proto_version)
    print("debug level is: %d" % ctx.debug_level)
    print("playlist:")
    for i in ctx.get_playlist():
        print("  " + str(i))

    print(80 * "-")
    print("")

    return 0
