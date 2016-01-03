from p2pool.bitcoin import networks

PARENT = networks.nets['hamradiocoin'] #name of coin you are mining
SHARE_PERIOD = 10 # seconds per share
NEW_SHARE_PERIOD = 10 # seconds per share after a new chain starts, this is so diff is adjusted accordingly
CHAIN_LENGTH = 24*60*60//10 # shares p2pool keeps before deleting them. has to be bigger or equal to REAL_CHAIN_LENGTH. should be the same
REAL_CHAIN_LENGTH = 24*60*60//10 # last number of shares to include when a winning share/block is found. larger the chain, the chain, the loger it takes to get paid out the full amount, but you also get paid out for near this length after you stop mining. keeps hoppers away and true dedicated miners your way
TARGET_LOOKBEHIND = 60 # shares CHANGE THIS TO 10 FOR SUPER HIGH DIFF WORKERS 20 FOR HIGH DIFF 30 FOR MEDIUMLY HIGH DIFF AND 60 FOR THE REST. It is used to guestinate the number of shares to include for diff of next share chain
SPREAD = 150 # blocks of the chain to pay if a miner finds one share. maximum is CHAIN_LENGTH/REAL_CHAIN_LENGTH
NEW_SPREAD = 150 # blocks
IDENTIFIER = '9f2e390aa41ffade'.decode('hex')
PREFIX = '50f713ab040dfade'.decode('hex')
P2P_PORT = 9233 #low diff/main diff port: 9233, medium high diff: 9234, high diff: 9235, super high diff: 9236
MIN_TARGET = 0
MAX_TARGET = 2**256//2**20 - 1
PERSIST = False #turn to False for a private node. turn to True for a public. NOTE THE CAPS FIRST LETTER!
WORKER_PORT = 9333 #Port workers attach to as well as stats page
BOOTSTRAP_ADDRS = 'wakalakalake.com'.split(' ') #servers that are peers to p2pool to haelp you connect
ANNOUNCE_CHANNEL = '#p2pool-ham' #channel your p2pool announces on. irc is so out of date
VERSION_CHECK = lambda v: True #get ready for port check
VERSION_WARNING = lambda v: 'Upgrade Fastcoin to >= 0.1.0.0!' if v < 10000 else None #hack for hamradiocoin since it is not in line with bitcoin....yet
#MORE READING CAN BE FOUND HERE https://bitcointalk.org/index.php?topic=457574.0
#ARCHIVED VERSION https://web.archive.org/web/20150926065619/https://bitcointalk.org/index.php?topic=457574.0
