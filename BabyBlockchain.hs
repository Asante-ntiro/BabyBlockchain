
data Transaction = Transaction { from   :: String   -- Sender
                               , to     :: String   -- Receiver
                               , amount :: Float    -- How much they are paying
                               }

data Block = Block { index    :: Int           -- Index of the block
                   , txs      :: [Transaction] -- List of transactions in block
                   , hash     :: String        -- Hash of block
                   , prevHash :: String        -- Prev Hash of block
                   , nonce    :: Maybe Int     -- Nonce of block
                   }

