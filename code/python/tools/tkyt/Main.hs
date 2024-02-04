{-# LANGUAGE DeriveGeneric #-}

module Main where
import Data.Aeson
import Data.Text (Text)
import GHC.Generics

data Person = Person { name :: Text, age :: Int } deriving Show

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

main :: IO ()
main = do
        contents <- readFile "educative.txt"

        putStrLn "Hello, Haskell!"
