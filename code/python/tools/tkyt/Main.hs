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

{-
{
    "comments": [
        {
            "cid": "UgwVfk4Uuvs9LmTlsIJ4AaABAg",
            "text": "Pour voir des preuves",
            "time": "il y a 2 mois (modifié)",
            "author": "@LesicsFR",
            "channel": "UC7XvuBMRYoBdjKPIBOxt6XQ",
            "votes": "63",
            "photo": "https://yt3.ggpht.com/ytc/AIf8zZQl_U_avM0A3JY3fpq79FHDK-QGVXdtQH2fPJEA=s176-c-k-c0x00ffffff-no-rj",
            "heart": false,
            "reply": false,
            "time_parsed": 1700831647.498626
        },
        ...
        ]
}
-}
