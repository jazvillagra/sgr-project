import Data.Map
import System.Environment
import System.Exit

main :: IO ()
main = getArgs >>= parse >>= putStr . tac

tac = unlines . reverse . lines


salas = [
	("Sala 101",20,"Habilitada"),
	("Sala Conferencias 1",200,"Inhabilitada"),
	("Sala Conferencias 2",150,"Habilitada")
	]
findKey :: (Eq k) => k -> [(k,v)] -> Maybe v
findKey key [] = Nothing
findKey key ((k,v):xs) = if key == k
                            then Just v
                            else findKey key xs


