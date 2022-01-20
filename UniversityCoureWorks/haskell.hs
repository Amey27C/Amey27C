-- REFERENCE 9x9 sudoku - This code was taken from the site https://gist.github.com/kristopherjohnson/46200d04db07736407bd. the original code is of 9x9 sudoku grid.
-- I adapted it from the above website and altered it into a 4x4 grid. I do not take any credit of  the code and I am acknowledged that the original work belongs to author of the code meantioned   in the website.
-- Website Accessed 2/12/2018

import Data.Array
-- Solve the example specified below
-- read example from input
main = do
   let solution = solve puzzleBoard
   printBoard solution

-- The elements on the board are represented by Ints in the range 0..4, where 0 represents "empty".
type Task2 = Int

-- A square is identified by a (row, column) pair
type Location = (Int, Int)

-- A sudoku board is a 4x4 matrix of marks
type Board = Array Location Task2

-- The sudoku board to be solved
puzzleBoard :: Board
puzzleBoard = array ((0, 0), (3, 3)) $ puzzleAssocs examplePuzzle

examplePuzzle :: [[Task2]]
examplePuzzle = [[3,4,0,0],
                 [2,0,3,0],
                 [0,3,0,2],
                 [0,0,1,3]]

-- Return first solution, or Nothing if no solutions found
solve :: Board -> Maybe Board
solve = headOrNothing . solutions

-- Return all solutions
solutions :: Board -> [Board]
solutions b = solutions' (emptyLocations b) b
 where
   -- Given list of empty locations on a board, pick an empty location,
   -- determine which elements can be put in that location, and then
   -- recursively find all solutions for that set of numbers.
   solutions' :: [Location] -> Board -> [Board]
   solutions' []     b = [b]
   solutions' (x:xs) b = concatMap (solutions' xs) candidateBoards
     where
       candidateTasks  = [m | m <- [1..4], isPossibleTask2 m x b]
       candidateBoards = map (\m -> copyWithTask2 m x b) candidateTasks

-- Return list of locations where value is 0
emptyLocations :: Board -> [Location]
emptyLocations b = [(row, col) | row <- [0..3], col <- [0..3], b ! (row, col) == 0]

-- Determine whether the specified task can be placed at specified position
isPossibleTask2 :: Task2 -> Location -> Board -> Bool
isPossibleTask2 m (row, col) b = notInRow && notInColumn && notInBox
 where
   notInRow    = notElem m $ b `tasksInRow` row
   notInColumn = notElem m $ b `tasksInColumn` col
   notInBox    = notElem m $ b `tasksIn2x2Box` (row, col)

-- Return board with specified value in specified Location
copyWithTask2 :: Task2 -> Location -> Board -> Board
copyWithTask2 task2 (row, col) b = b // [((row, col), task2)]

-- taskInRown returns the elements in the specified row
tasksInRow :: Board -> Int -> [Task2]
b `tasksInRow` row = [b ! loc | loc <- range((row, 0), (row, 3))]

-- tasksincolumn return the elements in the specified column
tasksInColumn ::  Board -> Int -> [Task2]
b `tasksInColumn` col = [b ! loc | loc <- range((0, col), (3, col))]

-- tasksIn2x2box returns the elements in the 2x2 box that includes the specified Location
tasksIn2x2Box :: Board -> Location -> [Task2]
b `tasksIn2x2Box` (row, col) = [b ! loc | loc <- locations]
 where
   row' = (row `div` 2) * 2
   col' = (col `div` 2) * 2
   locations = range((row', col'), (row' + 1, col' + 1))

-- Convert a list of rows of elements (as in examplePuzzle above) to a list of array associations
puzzleAssocs :: [[Task2]] -> [(Location, Task2)]
puzzleAssocs = concatMap rowAssocs . zip [0..3]
 where
   rowAssocs :: (Int, [Task2]) -> [((Int, Int), Task2)]
   rowAssocs (row, tasks) = colAssocs row $ zip [0..3] tasks

   colAssocs :: Int -> [(Int, Task2)] -> [((Int, Int), Task2)]
   colAssocs row cols = map (\(col, m) -> ((row, col), m)) cols

headOrNothing :: [a] -> Maybe a
headOrNothing []     = Nothing
headOrNothing (x:xs) = Just x
-- Prints the solution.
printBoard :: Maybe Board -> IO ()
printBoard Nothing  = putStrLn "No solution"
printBoard (Just b) = mapM_ putStrLn [show $ b `tasksInRow` row | row <- [0..3]]
