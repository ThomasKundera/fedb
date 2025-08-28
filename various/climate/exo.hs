import Debug.Trace

elem2 :: (Eq a) => a -> [a] -> Bool

elem2 _ [] = False
elem2 e (x:xs) = (e == x) || (elem2 e xs)

nub :: (Eq a) => [a] -> [a]

inremove :: (Eq a) => a -> [a] -> [a] -> [a]
inremove _ l []= l
inremove e l (x:xs)
  | e == x    = inremove e l xs
  | otherwise = inremove e (x:l) xs


remove :: (Eq a) => a -> [a] -> [a]
remove e l  = inremove e [] l


nub []  = []
nub (x:xs)
  | elem2 x xs = nub xs
  | otherwise = x : nub xs
  


isAsc :: [Int] -> Bool

isAsc [] = True
isAsc [a] = True
-- isAsc [a,b] = a <= b
isAsc (x:y:xs) = (x <= y) && isAsc (y:xs)
  
-- printElements :: [String] -> IO()
-- printElements (x:xs) =  print x printElements xs

main = do
  print "coucou"
--  if elem2 3 [0,1,2,3,4]
--     then print "True"
--     else print "False"
  
--  print b where b=nub [1,2,3,4]
--  print b where b=nub [1,2,3,4,3,2,1,7]
  if isAsc [0,1,3,2,3,4]
     then print "True"
     else print "False"
  
