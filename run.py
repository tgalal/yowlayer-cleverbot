from yowsup.stacks import YowStackBuilder
from yowsup.layers.network import YowNetworkLayer
from yowsup.layers.auth import AuthError
from yowsup.layers import YowLayerEvent
from yowsup.layers import YowParallelLayer
from yowsup.common.tools import StorageTools
from yowsup_ext.layers.cleverbot.layer import YowCleverBotLayer
from yowsup_ext.layers.store import YowStorageLayer

import sys
import logging

logging.basicConfig(level = logging.DEBUG)
logger = logging.getLogger(__name__)

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: run.py username password")
        sys.exit(1)
    credentials = (sys.argv[1], sys.argv[2])
    stackBuilder = YowStackBuilder()
    phoneStorage =  StorageTools.getStorageForPhone(credentials[0])
    stackBuilder.setProp(YowStorageLayer.PROP_DB_PATH, StorageTools.constructPath(phoneStorage, "yowstore.db"))
    stack = stackBuilder\
        .pushDefaultLayers(True)\
        .push(YowStorageLayer)\
        .push(YowCleverBotLayer)\
        .build()

    stack.setCredentials(credentials)
    logger.info("Starting")
    stack.broadcastEvent(YowLayerEvent(YowNetworkLayer.EVENT_STATE_CONNECT))

    try:
        stack.loop(timeout = 0.5, discrete = 0.5)
    except AuthError as e:
        print("Auth Error, reason %s" % e)
    except KeyboardInterrupt:
        print("\nYowsdown")
        sys.exit(0)
