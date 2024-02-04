{-# LANGUAGE OverloadedStrings #-}
{-# LANGUAGE DeriveGeneric #-}

module Main where
import Data.Aeson
import Data.Text (Text)
import GHC.Generics
import qualified Data.ByteString.Lazy as B

data Ytpost = Ytpost {
    cid :: Text,
    text :: Text,
    time :: Text,
    author :: Text,
    channel :: Text,
    votes :: Int,
    photo :: Text,
    heart :: Text, -- Actually boolean
    reply :: Text, -- Actually boolean
    time_parsed :: Float
} deriving Generic


instance FromJSON Ytpost

main :: IO ()
main = do
        contents <- B.readFile "DR1qnvMDh4w.json"
        let mm = decode contents :: Maybe Ytpost
        case mm of
             Nothing -> print "error parsing JSON"
             Just m -> print "Maybe parsing JSON"
