rootsSeparation f a b n =
    let h = (b - a) / n
        helper x1 x2 =
            if x2 <= b then [(x1, x2) | f x1 * f x2 <= 0] ++ helper x2 (x2 + h) else []
    in helper a (a + h)

bisection f a b eps =
    let output x1 x2 steps = "Initial approximation: " ++ show (a, b) ++ " || " ++
                             "Number of steps: " ++ show steps ++ " || " ++
                             "Approximate solution: " ++ show ((x1 + x2) / 2) ++ " || " ++
                             "Last segment length: " ++ show (x2 - x1) ++ " || " ++
                             "|f(x)|: " ++ show (abs (f ((x2 + x1) / 2))) ++ "     ||     " in
    let helper x1 x2 steps = let c = (x1 + x2) / 2 in if f x1 * f c <= 0
        then if c - x1 > 2 * eps then helper x1 c (steps + 1) else output x1 c steps
        else if x2 - c > 2 * eps then helper c x2 (steps + 1) else output c x2 steps
    in helper a b 0

newton f a b eps f' =
    let output x1 x2 steps = "Initial approximation: " ++ show (a, b) ++ " || " ++
                             "Number of steps: " ++ show steps ++ " || " ++
                             "Approximate solution: " ++ show ((x1 + x2) / 2) ++ " || " ++
                             "Last segment length: " ++ show (x2 - x1) ++ " || " ++
                             "|f(x)|: " ++ show (abs (f x2)) ++ "     ||     " in
    let helper x0 steps = if abs (x0 - x) < eps
        then output x x0 steps
        else helper x (steps + 1) where x = x0 - f x0 / f' x0
    in helper ((b + a) / 2) 0

modificatedNewton f a b eps f' =
    let output x1 x2 steps = "Initial approximation: " ++ show (a, b) ++ " || " ++
                             "Number of steps: " ++ show steps ++ " || " ++
                             "Approximate solution: " ++ show ((x1 + x2) / 2) ++ " || " ++
                             "Last segment length: " ++ show (x2 - x1) ++ " || " ++
                             "|f(x)|: " ++ show (abs (f x2)) ++ "     ||     " in
    let helper init x0 steps = if abs (x0 - x) < eps
        then output x x0 steps
        else helper init x (steps + 1) where x = x0 - f x0 / f' init
    in helper ((b + a) / 2) ((b + a) / 2) 0

secant f a b eps =
    let output x1 x2 steps = "Initial approximation: " ++ show (a, b) ++ " || " ++
                             "Number of steps: " ++ show steps ++ " || " ++
                             "Approximate solution: " ++ show ((x1 + x2) / 2) ++ " || " ++
                             "Last segment length: " ++ show (x2 - x1) ++ " || " ++
                             "|f(x)|: " ++ show (abs (f x2)) ++ "     ||     " in
    let helper x1 x2 steps = if abs (x1 - x2) < eps
        then output x1 x2 steps
        else helper x2 (x1 - f x1 / (f x1 - f x2) * (x1 - x2)) (steps + 1)
    in helper ((b + a) / 2) ((b + a) / 4) 0

main = 
    let f x = 2 ** x - 2 * cos x
        f' x = 2 ** x * log 2 + 2 * sin x
        a = -8
        b = 10
        n = 100000
        eps = 10 ** (-12)
        ints = rootsSeparation f a b n
        in do
        putStrLn "Task: Find all roots with odd multiplicity of the equation f(x) = 0 from [A, B]."
        putStrLn "Parameters: f(x) = 2 ^ x - 2 * cos(x), A = -8, B = 10, Epsilon = 10^(-12)."
        putStrLn ("Intervals: " ++ show ints ++ ", their number: " ++ show (length ints))
        putStrLn " "
        putStrLn ("Bisection method: " ++ show (concatMap (\x -> uncurry (bisection f) x eps) ints))
        putStrLn " "
        putStrLn ("Newton method: " ++ show (concatMap (\x -> uncurry (newton f) x eps f') ints))
        putStrLn " "
        putStrLn ("Modificated Newton method: " ++ show (concatMap (\x -> uncurry (modificatedNewton f) x eps f') ints))
        putStrLn " "
        putStrLn ("Secant method: " ++ show (concatMap (\x -> uncurry (secant f) x eps) ints))
