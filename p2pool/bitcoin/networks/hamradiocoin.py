import os
import platform

from twisted.internet import defer

from .. import data, helper
from p2pool.util import pack


P2P_PREFIX = '04050504'.decode('hex')
P2P_PORT = 15537
ADDRESS_VERSION = 0
RPC_PORT = 15538
RPC_CHECK = defer.inlineCallbacks(lambda bitcoind: defer.returnValue(
            'hamradiocoinaddress' in (yield bitcoind.rpc_help()) and
            not (yield bitcoind.rpc_getinfo())['testnet']
        ))
SUBSIDY_FUNC = lambda height: 20*100000000
POW_FUNC = data.hash256
BLOCK_PERIOD = 120 # s
SYMBOL = 'HAM'
CONF_FILE_FUNC = lambda: os.path.join(os.path.join(os.environ['APPDATA'], 'HamRadioCoin') if platform.system() == 'Windows' else os.path.expanduser('~/Library/Application Support/HamRadioCoin/') if platform.system() == 'Darwin' else os.path.expanduser('~/.hamradiocoin'), 'hamradiocoin.conf')
BLOCK_EXPLORER_URL_PREFIX = 'https://www.blockexperts.com/ham/hash/'
ADDRESS_EXPLORER_URL_PREFIX = 'https://www.blockexperts.com/ham/address/'
TX_EXPLORER_URL_PREFIX = 'https://www.blockexperts.com/ham/tx/'
SANE_TARGET_RANGE = (2**256//2**32//1000 - 1, 2**256//2**32 - 1)
DUMB_SCRYPT_DIFF = 1
DUST_THRESHOLD = 1e8
