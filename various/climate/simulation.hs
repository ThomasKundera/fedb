import System.Info
import System.Environment

main = do
    print os
    print arch
    print compilerName
    print compilerVersion
    getArgs >>= print
    getProgName >>= print
    getEnvironment >>= print    
