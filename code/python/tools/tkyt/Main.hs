{-# LANGUAGE DeriveGeneric #-}

module Main where

import Data.Aeson
import qualified Data.ByteString.Lazy as B
import Data.Text (Text, splitOn)
import GHC.Generics

{-
data YtpostSimple = YtpostSimple {
    cid :: Text,
    text :: Text,
    time :: Text,
    author :: Text,
    channel :: Text,
    votes :: Text, -- Maybe int?
    photo :: Text,
    heart :: Bool, -- Actually boolean
    reply :: Bool, -- Actually boolean
    time_parsed :: Float
} deriving (Generic , Show)
-}

data YtPostList = YtPostList
    { comments :: [YtPostSimple]
    }
    deriving (Show, Generic)

data YtPostSimple = YtPostSimple
    { cid :: Text
    , cidParent :: Maybe Text
    }
    deriving (Show, Generic)

instance FromJSON YtPostList

instance FromJSON YtPostSimple where
    parseJSON = withObject "Comment" $ \v -> do
        fullCid <- v .: "cid"
        let cidComponents = splitOn "." fullCid
        case cidComponents of
            [cid] -> pure $ YtPostSimple{cid = fullCid, cidParent = Nothing}
            [parent, cid] -> pure $ YtPostSimple{cid = fullCid, cidParent = Just parent}

main :: IO ()
main = do
    mPostList <- decodeFileStrict "simpletest2.json" :: IO (Maybe YtPostList)
    case mPostList of
        Nothing -> print "error in JSON"
        Just postList -> print postList


