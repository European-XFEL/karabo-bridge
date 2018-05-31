import argparse
from karabo_bridge.simulation import start_gen

def main(argv=None):
    ap = argparse.ArgumentParser(
        prog="karabo-bridge-server-sim",
        description="Run a Karabo bridge server producing simulated data.")
    ap.add_argument('port', help="TCP port the server will bind")
    ap.add_argument('--protocol', default='latest',
                    choices=['1.0', '2.1', 'latest'])
    ap.add_argument('--detector', default='AGIPD',
                    choices=['AGIPD', 'LPD'],
                    help="Which kind of detector to simulate")
    ap.add_argument('--serialisation', default='msgpack',
                    choices=['msgpack', 'pickle'])
    args = ap.parse_args(argv)
    start_gen(args.port, args.serialisation, args.protocol, args.detector)