{-# LANGUAGE OverloadedStrings #-}
{-# LANGUAGE DeriveGeneric #-}

module Main where
import Data.Aeson
import Data.Text (Text)
import GHC.Generics
import qualified Data.ByteString.Lazy as B

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

-- data Ytpostsimple = Ytpostsimple {
--     cid :: Text
-- } deriving (Generic , Show)

-- newtype Clist = Clist {unCmt :: [Ytpost]}


-- data Comments = Comments {
--         clist :: Array[Ytpost]
-- }
-- instance FromJSON Comments
-- instance FromJSON Clist

-- instance FromJSON Clist where
--    parseJSON (Object o) = Clist <$> (o .: "Clist")
--    parseJSON v = typeMismatch "Clist" v


instance FromJSON YtpostSimple


main :: IO ()
main = do
        contents <- B.readFile "simpletest.json"
        let mm = decode contents :: Maybe YtpostSimple
        case mm of
             Nothing -> print "error parsing JSON"
             Just m -> print mm -- "Maybe parsing JSON" ++ "toto"


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
